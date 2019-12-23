package com.parsers.csv

import com.typesafe.config.Config
import org.apache.spark.sql.SparkSession

import scala.util.Try

/**
  * @author ram.sinha on 12/23/19
  */
case class SparkService(config: Config) {

  val masterUrl = Try {
    config.getString("spark.master")
  }.toOption.getOrElse("local[*]")

  val appName = Try {
    config.getString("spark.appName")
  }.toOption.getOrElse("customParser")

  val _session = SparkSession.builder().
    appName(appName).
    master(masterUrl).
    getOrCreate()

  _session.sparkContext.setLogLevel("FATAL")
  def getSession() = _session
}
