package com.careem.streaming.examples.api.repository.impl


import java.sql.Timestamp

import com.careem.streaming.examples.api.dao.ServiceDAO.{DriverPingInfo, DriverPingInfoTable}
import com.careem.streaming.examples.api.repository.{Db, IRepository}
import slick.basic.DatabaseConfig
import slick.jdbc.JdbcProfile

import scala.concurrent.{ExecutionContext, Future}


class DriverPingInfoRepository(val config: DatabaseConfig[JdbcProfile])(implicit ex: ExecutionContext)
  extends Db with DriverPingInfoTable with IRepository[DriverPingInfo, String] {

  import config.profile.api._

  override def addEntity(e: DriverPingInfo) = db.run((driverPingEntries += e).map {
    _ > 0
  })

  override  def addEntities(e: List[DriverPingInfo]) = db.run((driverPingEntries ++= e))

  override def getCreateSchema = driverPingEntries.schema.createStatements.mkString(",")

  override def init() = db.run(DBIO.seq(driverPingEntries.schema.create))

  override def drop() = db.run(DBIO.seq(driverPingEntries.schema.drop))

  override def deleteEntity(e: Entity, predicate: Entity => Boolean): Future[Boolean] = ???

  override def updateEntity(e: Entity, predicate: Entity => Boolean): Future[Boolean] = ???

  override def getAllEntities(predicate: Entity => Boolean): Future[Seq[Entity]] = ???

  override def getLatestEntityById(id: SqlDataType): Future[Option[Entity]] = ???

  override def getEntityById(id: SqlDataType): Future[Seq[Entity]] = ???
  override def getCount (from: Timestamp, to: Timestamp) : Future [Int] = {
    db.run(driverPingEntries.filter(_.updateTime.between(from, to)).length.result)
  }
}