package com.careem.streaming.examples.api.repository.impl


import java.sql.Timestamp

import com.careem.streaming.examples.api.dao.ServiceDAO.{DriverPingInfo, TripRequestData, TripRequestDataTable}
import com.careem.streaming.examples.api.repository.{Db, IRepository}
import slick.basic.DatabaseConfig
import slick.jdbc.JdbcProfile

import scala.concurrent.{ExecutionContext, Future}


class TripDataRepository(val config: DatabaseConfig[JdbcProfile])(implicit ex: ExecutionContext)
  extends Db with TripRequestDataTable with IRepository[TripRequestData, String] {

  import config.profile.api._

  override def addEntity(e: TripRequestData) = db.run((tripRequestDataEntries += e).map {
    _ > 0
  })

  override  def addEntities(e: List[TripRequestData]) = db.run((tripRequestDataEntries ++= e))

  override def getCreateSchema = tripRequestDataEntries.schema.createStatements.mkString(",")

  override def init() = db.run(DBIO.seq(tripRequestDataEntries.schema.create))

  override def drop() = db.run(DBIO.seq(tripRequestDataEntries.schema.drop))

  override def deleteEntity(e: Entity, predicate: Entity => Boolean): Future[Boolean] = ???

  override def updateEntity(e: Entity, predicate: Entity => Boolean): Future[Boolean] = ???

  override def getAllEntities(predicate: Entity => Boolean): Future[Seq[Entity]] = ???

  override def getLatestEntityById(id: SqlDataType): Future[Option[Entity]] = ???

  override def getEntityById(id: SqlDataType): Future[Seq[Entity]] = ???

  override def getCount (from: Timestamp, to: Timestamp) : Future [Int] = {
    db.run(tripRequestDataEntries.filter(_.requestTimeStamp.between(from, to)).length.result)
  }
}