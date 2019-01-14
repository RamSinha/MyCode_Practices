package com.careem.streaming.examples.kafka

import java.io.File
import java.time.Instant

import com.github.tototoshi.csv._

import scala.Stream._
import scala.util.Random

object DataSetGenerator {
  val rand = new Random

  def getDataStream(dataSetLocation: String): Stream[List[String]] = {
    val reader = CSVReader.open(new File(dataSetLocation))
    reader.toStream.drop(2).map(record => List(1, 2, 5, 6, 8).map(record.apply(_)))
  }

  def getTripDataStream(): Stream[String] = {
    from(10) take 10000000 map { x =>
      if (x % 10 == 0) {
        Thread.sleep(2000)
      }
      List(rand.nextInt(x).toString,
        rand.nextInt(1000),
        rand.nextInt(1000),
        rand.nextInt(1000),
        rand.nextInt(1000),
        Instant.now.getEpochSecond
      ).mkString("#")
    }
  }

  def getDriverDataStream(): Stream[String] = {
    from(10) take 10000000 map { x =>
      if (x % 10 == 0) {
        Thread.sleep(2000)
      }
      List(rand.nextInt(x),
        rand.nextInt(1000),
        rand.nextInt(1000),
        Instant.now.getEpochSecond
      ).mkString("#")
    }
  }
}


/*
  case class DriverPingInfo(id: Option[Long],
                            driverId: String,
                            driverName: String,
                            driverLocation: String,
                            updateTime: Timestamp = new Timestamp(Instant.now.toEpochMilli))

  case class TripRequestData(id: Option[Long],
                      userId: String,
                      pickUpLocation: String,
                      dropOffLocation: String,
                      requestTimeStamp: Timestamp = new Timestamp(Instant.now.toEpochMilli)
                      )
 */