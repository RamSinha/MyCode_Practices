package com.careem.streaming.examples.api.service.http.routes

import java.sql.Timestamp

import akka.http.scaladsl.server.Directives._
import com.careem.streaming.examples.api.repository.RepositoryFactory
import com.careem.streaming.examples.api.service.responseformat.ResponseProtocol._
import org.joda.time.DateTime
import org.joda.time.format.DateTimeFormat
import spray.json._

import scala.concurrent.ExecutionContext
import scala.util.{Failure, Success, Try}

trait ServiceRoutes {
  implicit def ec: ExecutionContext

  val formatter = DateTimeFormat.forPattern("yyyy-MM-dd HH:mm:ss")

  implicit def dateTimeToTS(dateTime: DateTime) = new Timestamp(dateTime.getMillis)

  val serviceRoutes = pathPrefix("metrics" / "v1") {
    path("ratio") {
      get {
        parameters("at") {
          (at) => {
            val countT = RepositoryFactory.tripRequestRepository.getCount(formatter.parseDateTime(at).minusMinutes(10), formatter.parseDateTime(at))
            val countD = RepositoryFactory.driverPingRepository.getCount(formatter.parseDateTime(at).minusMinutes(10), formatter.parseDateTime(at))
            onComplete(countT.flatMap(t => countD.map(d => Try {
              (t * 1.0) / d
            }))) {
              case Success(entity) => {
                val ratio = entity.toOption.map(value =>
                  HistoricalRatio(
                    formatter.parseDateTime(at).minusMinutes(10).toString,
                    at,
                    value.toString))
                  .getOrElse (
                  HistoricalRatio(
                    formatter.parseDateTime(at).minusMinutes(10).toString,
                    at,
                    "NA"))
                complete(ratio.toJson.toString)
              }
              case Failure(ex) => failWith(ex)
            }
          }
        }
      }
    } ~
      path("historicalRatio") {
        get {
          parameters("from", "to") {
            (from, to) => {
              val countT = RepositoryFactory.tripRequestRepository.getCount(formatter.parseDateTime(from), formatter.parseDateTime(to))
              val countD = RepositoryFactory.driverPingRepository.getCount(formatter.parseDateTime(from), formatter.parseDateTime(to))
              onComplete(countT.flatMap(t => countD.map(d => Try {
                (t * 1.0) / d
              }))) {
                case Success(entity) => {
                  val ratio = entity.toOption.map(value => HistoricalRatio(from, to, value.toString)) getOrElse (HistoricalRatio(from, to, "NA"))
                  complete(ratio.toJson.toString)
                }
                case Failure(ex) => failWith(ex)
              }
            }
          }
        }
      }
  }
}
