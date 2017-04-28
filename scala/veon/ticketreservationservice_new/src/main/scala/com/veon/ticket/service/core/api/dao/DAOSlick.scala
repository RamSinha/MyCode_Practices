package com.veon.ticket.service.core.api.dao

import java.sql.Timestamp

import akka.routing.ConsistentHashingRouter.ConsistentHashable
import com.typesafe.scalalogging.slf4j.Logger
import com.veon.ticket.service.core.api.logging.LoggerFactory
import spray.json.DefaultJsonProtocol

import scala.slick.driver.PostgresDriver.simple._

object JsonProtocol {

  case class MovieScreenInformation(imdbId: String, availableSeats: String, screenId: String)

  case class MovieReservationInformation(imdbId: String, screenId: String) extends ConsistentHashable {
    override def consistentHashKey: Any = imdbId + screenId
  }


  case class RegisterMovie(imdbId: String, availlableSeats: Long, screenId: String) extends ConsistentHashable {
    override def consistentHashKey: Any = imdbId + screenId
  }

  case class MovieAvailabilityInformation(imdbId: String, screenId: String, availableSeats: Long, reservedSeats: Long)

  object RequestResponseProtocol extends DefaultJsonProtocol {
    implicit val modelMovieScreenInformationJson = jsonFormat3(MovieScreenInformation.apply)
    implicit val modelMovieReservationInformationJson = jsonFormat2(MovieReservationInformation.apply)
    implicit val modelMovieAvailabilityInformationJson = jsonFormat4(MovieAvailabilityInformation.apply)
    implicit val modelRegisterMovieJson = jsonFormat3(RegisterMovie.apply)
  }

}


/**
  * This class contains all the DAO objects.
  * ORM framework is SLICK.
  */


object DAOSlick {

  private val logger = Logger(LoggerFactory.getLogger(this.getClass.getName))


  case class MovieRecord(movie_id: String, screen_id: String, available_seats: Long, reserved_seats: Long, timestamp: Timestamp)

  class MovieRecordTable(tag: Tag) extends Table[MovieRecord](tag, "tr_movie_record_table") {
    def movie_id = column[String]("movie_id", O.NotNull)

    def screen_id = column[String]("screen_id", O.NotNull)

    def available_seats = column[Long]("available_seats", O.NotNull)

    def reserved_seats = column[Long]("reserved_seats")

    def timestamp = column[Timestamp]("timestamp", O.NotNull, O.DBType("timestamp default now()"))

    def idx = index("movie_idx", movie_id)

    def * = (movie_id, screen_id, available_seats, reserved_seats, timestamp) <>(MovieRecord.tupled, MovieRecord.unapply)
  }

  case class MovieReservationRecord(movie_id: String, screen_id: String, timestamp: Timestamp)

  class MovieReservationRecordTable(tag: Tag) extends Table[MovieReservationRecord](tag, "tr_movie_reservation_record_table") {
    def movie_id = column[String]("movie_id", O.NotNull)

    def screen_id = column[String]("screen_id", O.NotNull)

    def timestamp = column[Timestamp]("timestamp", O.NotNull, O.DBType("timestamp default now()"))

    def * = (movie_id, screen_id, timestamp) <>(MovieReservationRecord.tupled, MovieReservationRecord.unapply)
  }


  def testrun: Unit = {
    val connectionUrl = Mediator.connectionUrl
    Database.forURL(connectionUrl, driver = "org.postgresql.Driver") withSession {
      implicit session =>
        val movierecordtable = TableQuery[MovieRecordTable]
      //movierecordtable.filter(x => x.movie_id === "1" && x.screen_id === "2" && x.available_seats > 0).map(r => (r.available_seats, r.reserved_seats)).update()

    }

  }

  def main(args: Array[String]) {

    val connectionUrl = Mediator.connectionUrl
    Database.forURL(connectionUrl, driver = "org.postgresql.Driver") withSession {
      implicit session =>
        val movierecordtable = TableQuery[MovieRecordTable]
        val moviereservationrecordtable = TableQuery[MovieReservationRecordTable]

        val schema = movierecordtable.ddl ++ moviereservationrecordtable.ddl
        schema.create
    }


  }

}