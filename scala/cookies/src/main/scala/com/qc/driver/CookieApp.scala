package com.qc.driver

import com.qc.config.UserConfig
import com.qc.dao.CookieRecord
import com.qc.dataloader.DataLoaderFactory
import com.qc.execution.ExecutionEngineFactory
import com.typesafe.config.ConfigFactory

/**
 * @author ram.sinha on 8/27/21
 */
object CookieApp extends App {
  val userOptions = UserConfig( args ) // parse user option
  val dataLoader = DataLoaderFactory.getDataLoader(userOptions, ConfigFactory.load()) // get data-loader
  val executionEngine = ExecutionEngineFactory.createExecutionEngine(userOptions, ConfigFactory.empty()) // computation engine
  dataLoader.loadData().foreach(executionEngine.accept) // pass records to computation engine
  val topCookiesAtDay = executionEngine.topResult.sorted(Ordering.by[CookieRecord, String](_.cookieName)) // get TopK sorted by Cookie Name
  println("*********************************************")
  println(s"List of top cookies at ${userOptions.day()}")
  println("********************************************* \n ")
  println(topCookiesAtDay.map(_.cookieName).mkString("\n")) // print all the cookies
  println("\n********************************************* \n ")
}
