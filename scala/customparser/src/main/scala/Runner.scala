package com.parsers
import com.parsers.csv.{Parser, ParserOptionConf, SparkService}
import com.typesafe.config.ConfigFactory

/**
  * @author ram.sinha on 12/22/19
  */
object Runner extends App {
  val formatOption = new ParserOptionConf(args)
  val spark = new SparkService(ConfigFactory.load()).getSession()
  val parser = Parser(formatOption, spark)
  val df = parser.read(formatOption.files.toOption.get)
  df.show(formatOption.top.toOption.get)
}