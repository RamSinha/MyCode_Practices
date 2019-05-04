package com.tutorial.streaming.examples.api.repository

import com.typesafe.config.ConfigFactory
import slick.basic.DatabaseConfig
import slick.jdbc.JdbcProfile

trait DbConfiguration {
  lazy val config = DatabaseConfig.forConfig[JdbcProfile]("db", ConfigFactory.load("datasource.conf"))
}

trait Db {
  val config: DatabaseConfig[JdbcProfile]
  val db: JdbcProfile#Backend#Database = config.db
}
