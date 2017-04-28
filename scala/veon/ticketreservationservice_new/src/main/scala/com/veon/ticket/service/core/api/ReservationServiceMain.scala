package com.veon.ticket.service.core.api

import akka.actor.{ActorSystem, Props}
import akka.io.IO
import com.veon.ticket.service.core.api.dao.{ActorSystemFactory, Mediator}
import com.veon.ticket.service.core.api.dao.Mediator.{BookTicketRequest, ReservationTicketBookingActor}
import com.veon.ticket.service.core.api.logging.LoggerFactory
import spray.can.Http

object ReservationServiceMain {
  def main(args: Array[String]) {

    LoggerFactory.initialize()
    implicit val system = ActorSystemFactory.system
    val service = system.actorOf(Props[ReservationAPIServiceActor], "reservation-api-service")
    IO(Http) ! Http.Bind(service, interface = "0.0.0.0", port = 8080)
  }
}
