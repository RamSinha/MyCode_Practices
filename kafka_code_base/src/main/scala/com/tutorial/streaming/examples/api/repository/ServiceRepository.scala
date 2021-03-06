package com.tutorial.streaming.examples.api.repository

import java.sql.Timestamp
import java.util.concurrent.Executors

import com.tutorial.streaming.examples.api.dao.ServiceDAO.{DriverPingInfo, LeadInfo, TripRequestData}
import com.tutorial.streaming.examples.api.repository.impl.{DriverPingInfoRepository, PFLeadDataRepository, TripDataRepository}

import scala.concurrent.duration.Duration
import scala.concurrent.{Await, ExecutionContext, Future}

import scala.concurrent.ExecutionContext.Implicits.global


trait IRepository[T, V] {
  type Entity = T
  type SqlDataType = V

  def addEntity(e: Entity): Future[Boolean]

  def addEntities(e: List[Entity])

  def deleteEntity(e: Entity, predicate: (Entity) => Boolean): Future[Boolean]

  def updateEntity(e: Entity, predicate: (Entity) => Boolean): Future[Boolean]

  def getAllEntities(predicate: (Entity) => Boolean): Future[Seq[Entity]]

  def getCount(from: Timestamp, to: Timestamp): Future[Int]

  def getLatestEntityById(id: SqlDataType): Future[Option[Entity]]

  def getEntityById(id: SqlDataType): Future[Seq[Entity]]

  def getCreateSchema: String

  def init(): Future[Unit]

  def drop(): Future[Unit]
}

object RepositoryFactory {
  implicit val hikariThreadPool = ExecutionContext.fromExecutorService(Executors.newFixedThreadPool(1))
  val tripRequestRepository: IRepository[TripRequestData, String] = {
    val config = new DbConfiguration {}.config
    new TripDataRepository(config)
  }

  val driverPingRepository: IRepository[DriverPingInfo, String] = {
    val config = new DbConfiguration {}.config
    new DriverPingInfoRepository(config)
  }

  val pfLeadRepository: IRepository[LeadInfo, String] = {
    val config = new DbConfiguration {}.config
    new PFLeadDataRepository(config)
  }

  def shutdown(): Unit = {
    hikariThreadPool.shutdown()
  }
}

object CreateTableScript {
  def main(args: Array[String]): Unit = {
    val tripDataRepo = RepositoryFactory.tripRequestRepository
    val tripInitFuture = tripDataRepo.init()
    tripInitFuture.onFailure { case ex => ex.printStackTrace() }
    Await.result(tripInitFuture, Duration.Inf)
    val driverPingRepo = RepositoryFactory.driverPingRepository
    val driverPingInitFuture = driverPingRepo.init()
    driverPingInitFuture.onFailure { case ex => ex.printStackTrace() }
    Await.result(driverPingInitFuture, Duration.Inf)

    val pfLeadRepo = RepositoryFactory.pfLeadRepository
    val pfLeadInitFuture = pfLeadRepo.init()
    pfLeadInitFuture.onFailure { case ex => ex.printStackTrace() }
    Await.result(pfLeadInitFuture, Duration.Inf)
  }
}

object DropTableScript {
  def main(args: Array[String]): Unit = {
    val tripDataRepo = RepositoryFactory.tripRequestRepository
    val f = tripDataRepo.drop()
    f.onFailure { case ex => ex.printStackTrace() }
    Await.result(f, Duration.Inf)

    val driverPingRepo = RepositoryFactory.driverPingRepository
    val driverPingDropFuture = driverPingRepo.drop()
    driverPingDropFuture.onFailure { case ex => ex.printStackTrace() }
    Await.result(driverPingDropFuture, Duration.Inf)
  }
}