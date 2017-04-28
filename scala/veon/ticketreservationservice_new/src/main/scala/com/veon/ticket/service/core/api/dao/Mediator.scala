package com.veon.ticket.service.core.api.dao

import java.util.concurrent.Executors

import akka.actor.{Actor, ActorRef, ActorSystem, Props}
import akka.routing.ConsistentHashingRouter
import akka.routing.ConsistentHashingRouter.ConsistentHashable
import com.typesafe.scalalogging.slf4j.Logger
import com.veon.ticket.service.core.api.dao.DAOSlick.MovieRecord
import com.veon.ticket.service.core.api.dao.JsonProtocol.{MovieAvailabilityInformation, MovieReservationInformation, RegisterMovie}
import com.veon.ticket.service.core.api.exceptions.{TicketReservationBadRequestException, TicketReservationException, TicketReservationPostgresException}
import com.veon.ticket.service.core.api.logging.LoggerFactory

import scala.concurrent.{ExecutionContext, Future, Promise}
import scala.slick.driver.PostgresDriver.simple._
import scala.util.{Failure, Success, Try}

object ActorSystemFactory {
  val system = ActorSystem("on-spray-can")
}


/**
  * This class contains logic interaction with postgres DB.
  * This also uses ConsistenHashingRouter so that request for different movieID and ScreenID combination can be served concurrently
  */
object Mediator {


  val dbHandleActor = ActorSystemFactory.system.actorOf(Props[ReservationTicketBookingActor].withRouter(ConsistentHashingRouter(10)), name = "reservationticketbookingactor")

  def initialiseTicketBookingActor(implicit system: ActorSystem) = {
    system.actorOf(Props[ReservationTicketBookingActor].withRouter(ConsistentHashingRouter(10)), name = "reservationticketbookingactor")
  }

  case class BookTicketRequest(movieId: String, screenId: String) extends ConsistentHashable {
    override def consistentHashKey: Any = movieId + screenId
  }

  class ReservationTicketBookingActor extends Actor {

    def receive = {
      case MovieReservationInformation(movieId, screenId) => sender ! Try {
        val (available, reserved) = getCurrentAvailableSeat(movieId, screenId)
        if (available > 0) {
          makeReservation(movieId, screenId, available - 1, reserved + 1)
          "Success"
        } else {
          "Seat not available"
        }

      }

      case RegisterMovie(movieId, availableSeats, screenId) => {
        sender !  {
          registerMovie(movieId, availableSeats, screenId)
          "Success"
        }
      }
    }
  }

  implicit val slick_pg_db_ec = ExecutionContext.fromExecutorService(Executors.newFixedThreadPool(50))

  final val connectionUrl = "jdbc:postgresql://localhost/postgres?"
  private val logger = Logger(LoggerFactory.getLogger(this.getClass.getName))

  def getSqlTimestamp() = {
    new java.sql.Timestamp(new org.joda.time.DateTime().getMillis);
  }

  def getCurrentAvailableSeat(movieId: String, screenId: String) = {
    Database.forURL(connectionUrl, driver = "org.postgresql.Driver") withSession {
      implicit session =>
        val movieRecords = TableQuery[DAOSlick.MovieRecordTable]

        Try(movieRecords.filter(record => record.movie_id === movieId && record.screen_id === screenId).firstOption) match {
          case Success(record) => {
            logger.info(s"Successfully retrieved detail for $record")
            record match {
              case Some(movieRecord) => (movieRecord.available_seats, movieRecord.reserved_seats)
              case None => throw new TicketReservationBadRequestException(s"Invalid movieid $movieId and screenid $screenId")
            }
          }
          case Failure(_) => throw new TicketReservationPostgresException(s"Failed to get details for movie_id: $movieId, screen_id: $screenId")
        }
    }
  }

  def registerMovie(imdbId: String, availlableSeats: Long, screenId: String): Unit = {
    Database.forURL(connectionUrl, driver = "org.postgresql.Driver") withSession {
      implicit session =>
        TableQuery[DAOSlick.MovieRecordTable] ++= MovieRecord(imdbId, screenId, availlableSeats, 0, getSqlTimestamp) :: Nil
    }
  }

  def makeReservation(movieId: String, screenId: String, availableSeat: Long, reservedSeat: Long) = {
    Database.forURL(connectionUrl, driver = "org.postgresql.Driver") withSession {
      implicit session =>
        val movieRecords = TableQuery[DAOSlick.MovieRecordTable]
        movieRecords.filter(record => record.movie_id === movieId && record.screen_id === screenId).map(record => (record.available_seats, record.reserved_seats)).update(availableSeat, reservedSeat)
    }
  }

  def getMovieDetail(movieId: String, screenId: String) = Future {

    Database.forURL(connectionUrl, driver = "org.postgresql.Driver") withSession {
      implicit session =>
        val movieRecords = TableQuery[DAOSlick.MovieRecordTable]

        Try(movieRecords.filter(record => record.movie_id === movieId && record.screen_id === screenId).firstOption) match {
          case Success(record) => {
            logger.info(s"Successfully retrieved detail for $record")
            record match {
              case Some(movieRecord) => MovieAvailabilityInformation(movieId, screenId, movieRecord.available_seats, movieRecord.reserved_seats)
              case None => throw new TicketReservationBadRequestException(s"Invalid movieid $movieId and screenid $screenId")
            }
          }
          case Failure(_) => throw new TicketReservationPostgresException(s"Failed to get details for movie_id: $movieId, screen_id: $screenId")
        }

    }
  }(slick_pg_db_ec)


}

