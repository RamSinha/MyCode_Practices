package com.careem.kafka.examples.api.dao

import java.sql.Timestamp
import java.time.Instant

import com.careem.kafka.examples.api.repository.Db

object ServiceDAO {

  case class TripRequestData(id: Option[Long],
                      userId: String,
                      pickUpLocation: String,
                      dropOffLocation: String,
                      requestTimeStamp: Timestamp = new Timestamp(Instant.now.toEpochMilli)
                      )

  trait TripRequestDataTable {
    this: Db =>

    import config.profile.api._

    class TripRequestDataEntries(tag: Tag) extends Table[TripRequestData](tag, "trip_request_data_entries") {
      def id = column[Long]("etl_id", O.PrimaryKey, O.AutoInc)

      def userId = column[String]("user_id", O.Length(512))

      def pickUpLocation = column[String]("pu_location", O.Length(64), O.Default("NA"))

      def dropOffLocation = column[String]("do_location", O.Length(64))

      def requestTimeStamp = column[Timestamp]("request_time_stamp", O.SqlType("timestamp default now()"))

      def * = (id.?, userId, pickUpLocation, dropOffLocation, requestTimeStamp) <> (TripRequestData.tupled, TripRequestData.unapply)
    }

    val tripRequestDataEntries = TableQuery[TripRequestDataEntries]
  }


  case class DriverPingInfo(id: Option[Long],
                            driverId: String,
                            driverName: String,
                            driverLocation: String,
                            updateTime: Timestamp = new Timestamp(Instant.now.toEpochMilli))

  trait DriverPingInfoTable {
    this: Db =>

    import config.profile.api._

    class DriverPingInfos(tag: Tag) extends Table[DriverPingInfo](tag, "driver_ping_info") {
      def id = column[Long]("id", O.PrimaryKey, O.AutoInc)

      def driverId = column[String]("driver_id", O.Length(64))
      def driverName = column[String]("driver_name", O.Length(64))
      def driverLocation = column[String]("driver_location", O.Length(64))
      def updateTime = column[Timestamp]("update_time", O.SqlType("timestamp default now()"))

      def * = (id.?, driverId, driverName, driverLocation, updateTime) <> (DriverPingInfo.tupled, DriverPingInfo.unapply)
    }

    val driverPingEntries = TableQuery[DriverPingInfos]
  }

}
