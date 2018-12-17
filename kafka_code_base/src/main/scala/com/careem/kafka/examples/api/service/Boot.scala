package com.careem.kafka.examples.api.service

import akka.actor.ActorSystem
import akka.stream.ActorMaterializer
import com.careem.kafka.examples.api.service.http.HttpService

import scala.concurrent.ExecutionContext

object Boot extends App {

  implicit val actorSystem = ActorSystem("metrics-system")
  implicit val actorMaterializer = ActorMaterializer()
  implicit val executionContext = actorSystem.dispatcher
  implicit val scheduler = actorSystem.scheduler

  val httpService = new HttpService {
    override implicit def system: ActorSystem = actorSystem
    override implicit def materializer: ActorMaterializer = actorMaterializer
    override def ec: ExecutionContext = executionContext
  }

  httpService.start("0.0.0.0", 8899)
}
