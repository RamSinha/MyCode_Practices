/*
 * ************************************************************************
 *  ADOBE CONFIDENTIAL
 *  ___________________
 *
 *   Copyright 2014 Adobe Systems Incorporated
 *   All Rights Reserved.
 *
 *  NOTICE:  All information contained herein is, and remains
 *  the property of Adobe Systems Incorporated and its suppliers,
 *  if any.  The intellectual and technical concepts contained
 *  herein are proprietary to Adobe Systems Incorporated and its
 *  suppliers and are protected by all applicable intellectual property
 *  laws, including trade secret and copyright laws.
 *  Dissemination of this information or reproduction of this material
 *  is strictly forbidden unless prior written permission is obtained
 *  from Adobe Systems Incorporated.
 * ************************************************************************
 */

package com.veon.ticket.service.core.api

import akka.actor.{Actor, Props, Terminated}
import akka.routing.ConsistentHashingRouter.ConsistentHashable
import com.veon.ticket.service.core.api.dao.JsonProtocol.{MovieAvailabilityInformation, MovieReservationInformation, RegisterMovie}
import com.veon.ticket.service.core.api.dao.Mediator
import com.veon.ticket.service.core.api.dao.JsonProtocol.RequestResponseProtocol.modelMovieAvailabilityInformationJson
import com.veon.ticket.service.core.api.dao.JsonProtocol.RequestResponseProtocol.modelMovieReservationInformationJson
import com.veon.ticket.service.core.api.dao.JsonProtocol.RequestResponseProtocol.modelRegisterMovieJson
import com.veon.ticket.service.core.api.dao.Mediator.BookTicketRequest
import com.veon.ticket.service.core.api.exceptions.{TicketReservationBadRequestException, TicketReservationException, TicketReservationPostgresException}
import com.veon.ticket.service.core.api.logging.LoggerFactory
import spray.http.HttpHeaders.RawHeader
import spray.http._
import spray.json._
import spray.routing._
import spray.util.LoggingContext
import akka.pattern.ask
import akka.util.Timeout

import scala.concurrent.ExecutionContext
import scala.concurrent.ExecutionContext.Implicits.global
import scala.util.{Failure, Success}

class ReservationAPIServiceActor extends Actor with ReservationAPIService {

  implicit def uncaughtExceptionHandler(implicit log: LoggingContext) =
    ExceptionHandler {
      case e: Exception => ctx =>
        LogExceptionAsError(e, unhandled = true, withStackTrace = true)
        ctx.complete(StatusCodes.InternalServerError, "Unhandled routing exception: " + e.toString)
    }

  def handleTimeouts: Receive = {
    case Timedout(req: HttpRequest) => {
      val logger = implicitly[LoggingContext]
      logger.warning("Timed out on request {} ", req.toString)
      sender ! HttpResponse(StatusCodes.InternalServerError, "Backend service timed out.")
    }
  }

  def actorRefFactory = context

  def receive =
    handleTimeouts orElse runRoute(routePublish)
}

trait ReservationAPIService extends HttpService {

  implicit val timeout = Timeout(10000)

  val acrHeadersName = {
    "access-control-request-headers"
  }

  val logger = {
    LoggerFactory.getLogger(this.getClass.getName)
  }

  val routePublish = {
    path("ticketreservation" / "v1") {
      optionalHeaderValueByName(acrHeadersName) { acrHeaders =>
        respondWithCORSHeaders("GET", acrHeaders) {
          options {
            complete("")
          } ~
            get {
              complete {
                "Reservation System Health Check API "
              }
            }
        }
      }
    } ~
      pathPrefix("ticketreservation" / "v1") {
        path("getAvailability") {
          optionalHeaderValueByName(acrHeadersName) { acrHeaders =>
            respondWithCORSHeaders("GET, POST", acrHeaders) {
              options {
                complete("")
              } ~
                get {
                  verifyContentType("application/json") {
                    clientIP { userAddress =>
                      entity(as[String]) { req =>
                        parameters("imdbId", "screenId") { (imdbId, screenId) =>
                          handleExceptions(reservationServiceExceptionHandler) {
                            respondWithMediaType(MediaTypes.`application/json`) {
                              respondWithStatus(StatusCodes.Accepted) {
                                detach() {
                                  val response = Mediator.getMovieDetail(imdbId, screenId)
                                  onComplete(response) {
                                    case Success(result) =>
                                      complete {
                                        result.toJson.toString
                                      }
                                    case Failure(ex) => {
                                      complete {
                                        ex
                                      }
                                    }
                                  }
                                }
                              }
                            }
                          }
                        }
                      }
                    }
                  }
                }
            }
          }
        }
      } ~
      pathPrefix("ticketreservation" / "v1") {
        path("makeReservation") {
          optionalHeaderValueByName(acrHeadersName) { acrHeaders =>
            respondWithCORSHeaders("GET, POST", acrHeaders) {
              options {
                complete("")
              } ~
                post {
                  extractRequest() { req =>

                    verifyContentType("application/json") {
                      clientIP { userAddress =>
                        entity(as[String]) { req =>
                          handleExceptions(reservationServiceExceptionHandler) {
                            respondWithMediaType(MediaTypes.`application/json`) {
                              respondWithStatus(StatusCodes.Accepted) {
                                detach() {
                                  val messg = req.parseJson.convertTo[MovieReservationInformation]
                                  val response = Mediator.dbHandleActor ? messg
                                  onComplete(response) {
                                    case Success(result) =>
                                      complete {
                                        result match {
                                          case Success(value) => {
                                            s"""
                                               |{
                                               |  "status" : "Reservation made $value"
                                               |}
                                        """.stripMargin
                                          }
                                          case Failure(ex) => {
                                            ex
                                          }
                                        }
                                      }
                                  }
                                }
                              }
                            }
                          }
                        }
                      }
                    }

                  }
                }
            }
          }
        }
      } ~
      pathPrefix("ticketreservation" / "v1") {
        path("registerMovie") {
          optionalHeaderValueByName(acrHeadersName) { acrHeaders =>
            respondWithCORSHeaders("POST", acrHeaders) {
              options {
                complete("")
              } ~
                post {
                  extractRequest() { req =>

                    verifyContentType("application/json") {
                      clientIP { userAddress =>
                        entity(as[String]) { req =>
                          handleExceptions(reservationServiceExceptionHandler) {
                            respondWithMediaType(MediaTypes.`application/json`) {
                              respondWithStatus(StatusCodes.Accepted) {
                                detach() {
                                  val messg = req.parseJson.convertTo[RegisterMovie]
                                  val response = Mediator.dbHandleActor ? messg
                                  onComplete(response) {
                                    case Success(result) =>
                                      complete {
                                        s"""
                                           |{
                                           |  "status" : "Registered movie $result"
                                           |}
                                        """.stripMargin
                                      }
                                    case Failure(ex) => {
                                      complete {
                                        ex
                                      }
                                    }
                                  }
                                }
                              }
                            }
                          }
                        }
                      }
                    }

                  }
                }
            }
          }
        }
      }
  }

  def extractRequest(): Directive1[HttpRequest] = extract(_.request)

  def reservationServiceExceptionHandler(implicit log: LoggingContext) =
    ExceptionHandler {

      case e: TicketReservationException => ctx =>
        val resp = new HttpResponse(StatusCodes.InternalServerError, "Ticket Reservation Exception: " + e.getMessage)
        ctx.complete(resp)

      case e: TicketReservationBadRequestException => ctx =>
        val resp = new HttpResponse(StatusCodes.BadRequest, "Ticket Reservation Bad Request Exception: " + e.getMessage)
        ctx.complete(resp)

      case e: TicketReservationPostgresException => ctx =>
        val resp = new HttpResponse(StatusCodes.InternalServerError, "Ticket Reservation Postgres Exception: " + e.getMessage)
        ctx.complete(resp)
    }


  def respondWithCORSHeaders(rawMethodList: String, acrHeaders: Option[String]) = {
    val rh = implicitly[RejectionHandler]
    respondWithCORSHeadersInner(rawMethodList, acrHeaders) & handleRejections(rh)
  }

  def respondWithCORSHeadersInner(rawMethodList: String, acrHeaders: Option[String]) =
    acrHeaders match {
      case None =>
        respondWithHeaders(
          RawHeader("Access-Control-Allow-Origin", "*"),
          RawHeader("Access-Control-Max-Age", "604800"),
          RawHeader("Access-Control-Allow-Credentials", "true"),
          RawHeader("Access-Control-Allow-Methods", rawMethodList)
        )
      case Some(headers) =>
        respondWithHeaders(
          RawHeader("Access-Control-Allow-Origin", "*"),
          RawHeader("Access-Control-Max-Age", "604800"),
          RawHeader("Access-Control-Allow-Credentials", "true"),
          RawHeader("Access-Control-Allow-Methods", rawMethodList),
          RawHeader("Access-Control-Allow-Headers", headers)
        )
    }


  def LogExceptionAsError(exc: Exception, unhandled: Boolean, withStackTrace: Boolean) = {
    val exString = s"${
      if (unhandled) "Unhandled exception:" else ""
    } ${
      if (withStackTrace) ExceptionExtensions.getExceptionMessageWithStackTraceFor(exc) else exc.getMessage
    }"
    logger.error(exString)
  }

  def verifyContentType(supported: String): Directive0 = pass

}
