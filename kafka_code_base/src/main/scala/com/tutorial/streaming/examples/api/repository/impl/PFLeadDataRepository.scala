package com.tutorial.streaming.examples.api.repository.impl

import java.sql.Timestamp

import com.tutorial.streaming.examples.api.dao.ServiceDAO.{LeadInfo, LeadInfoTable}
import com.tutorial.streaming.examples.api.repository.{Db, IRepository}
import slick.basic.DatabaseConfig
import slick.jdbc.JdbcProfile

import scala.concurrent.{ExecutionContext, Future}


class PFLeadDataRepository(val config: DatabaseConfig[JdbcProfile])(implicit ex: ExecutionContext)
  extends Db with LeadInfoTable with IRepository[LeadInfo, String] {

  import config.profile.api._

  override def addEntity(e: LeadInfo) = db.run((leadInfoEntries += e).map {
    _ > 0
  })

  override  def addEntities(e: List[LeadInfo]) = db.run((leadInfoEntries ++= e))

  override def getCreateSchema = leadInfoEntries.schema.createStatements.mkString(",")

  override def init() = db.run(DBIO.seq(leadInfoEntries.schema.create))

  override def drop() = db.run(DBIO.seq(leadInfoEntries.schema.drop))

  override def deleteEntity(e: Entity, predicate: Entity => Boolean): Future[Boolean] = ???

  override def updateEntity(e: Entity, predicate: Entity => Boolean): Future[Boolean] = ???

  override def getAllEntities(predicate: Entity => Boolean): Future[Seq[Entity]] = ???

  override def getLatestEntityById(id: SqlDataType): Future[Option[Entity]] = ???

  override def getEntityById(id: SqlDataType): Future[Seq[Entity]] = ???

  override def getCount (from: Timestamp, to: Timestamp) : Future [Int] = {
    db.run(leadInfoEntries.filter(_.updateTime.between(from, to)).length.result)
  }
}