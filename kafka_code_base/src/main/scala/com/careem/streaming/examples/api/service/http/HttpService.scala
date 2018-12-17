package com.careem.streaming.examples.api.service.http

import akka.actor.ActorSystem
import akka.http.scaladsl.Http
import akka.http.scaladsl.model.StatusCodes._
import akka.http.scaladsl.model._
import akka.http.scaladsl.server.Directives._
import akka.http.scaladsl.server.{ExceptionHandler, Route}
import akka.stream.ActorMaterializer
import com.careem.streaming.examples.api.exceptions.{APIException, MalformedRequestException}
import com.careem.streaming.examples.api.service.http.routes.ServiceRoutes
trait HttpService extends ServiceRoutes {
  implicit def system: ActorSystem

  implicit def materializer: ActorMaterializer

  def exceptionHandler =
    ExceptionHandler {
      case e: MalformedRequestException => complete(HttpResponse(BadRequest, entity = s"RequestException: ${e.getMessage}"))
      case e: APIException => complete(HttpResponse(InternalServerError, entity = s"ServiceException: ${e.getMessage}"))
    }

  private val sourceHttp = Http()(system)

  val allRoutes = handleExceptions(exceptionHandler) {
    serviceRoutes
  }

  def start(interface: String, port: Int): Unit = {
    sourceHttp
      .bind(interface, port)
      .runForeach(
        connection => {
          connection.handleWith(Route.handlerFlow(allRoutes))
        }
      )
  }
}