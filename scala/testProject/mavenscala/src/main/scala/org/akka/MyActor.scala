package org.akka

/**
  * Created by ramsinha on 29/08/16.
  */


import akka.actor.Actor
import akka.actor.ActorRef
import akka.actor.Props
import akka.event.Logging


class MyActor extends Actor {
  def receive = {
    case value: String => doSomething(value)
    case _ => println("received unknown message")
  }
  def doSomething(value: Any) {
    return "Did something"
  }
}


case class ProcessStringMsg(messg: String)

case class StringProcessedMsg(words: Int)

class StringCounterActor extends Actor {
  def receive = {
    case ProcessStringMsg(string) => {
      val wordsInLine = string.split(" ").length
      sender ! StringProcessedMsg(wordsInLine)
    }
    case _ => println("Error: message not recognized")
  }
}


case class StartProcessFileMsg()


class WordCounterActor(fileName: String) extends Actor {
  private var running = false
  private var totalLines = 0
  private var linesProcessed = 0
  private var result = 0
  private var fileSender: Option[ActorRef] = None

  def receive = {
    case StartProcessFileMsg() => {
      if (running) {
        println("Duplicate start message recieved")
      } else {
        running = true
        fileSender = Some(sender)
        import scala.io.Source._
        fromFile(fileName).getLines.foreach {
          line => context.actorOf(Props[StringCounterActor]) ! ProcessStringMsg(line)
            totalLines += 1
        }
      }
    }
    case StringProcessedMsg(words) => {
      result += words
      linesProcessed += 1
      if (linesProcessed == totalLines) {
        fileSender.map(_ ! result)
      }
    }
    case _ => println("Message not recognised")
  }
}

object Sample  {

  import akka.util.Timeout
  import scala.concurrent.duration._
  import akka.actor.ActorSystem
  import akka.pattern.ask
  import akka.dispatch.ExecutionContexts._

  implicit val ec = global


  import akka.actor.OneForOneStrategy
  import akka.actor.SupervisorStrategy._
  import scala.concurrent.duration._
  import akka.remote.RemoteActorRefProvider
  //import akka.remote.netty.NettyRemoteTransport
  import scala.concurrent.Future
  import scala.concurrent.Await
  import scala.concurrent.duration

   val supervisorStrategy =
    OneForOneStrategy() {
      case _: ArithmeticException      => Resume
      case _: NullPointerException     => Restart
      case _: IllegalArgumentException => Stop
      case _: Exception                => Escalate
    }

  def main(args: Array[String]) {
    val system = ActorSystem("System")
    val actor = system.actorOf(Props(new WordCounterActor("/Users/ramsinha/testCommon.yml")))
    implicit val timeout = Timeout(25 seconds)
    val future = actor ? StartProcessFileMsg()
    future.map { result =>
      println("Total number of words " + result)
      system.shutdown
    }
  }
}


