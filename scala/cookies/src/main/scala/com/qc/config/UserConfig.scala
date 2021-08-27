package com.qc.config

import com.qc.config.ExecutionEngineType.ExecutionEngineType
import org.rogach.scallop.{ScallopConf, ScallopOption, singleArgConverter}

/**
 * @author ram.sinha on 8/27/21
 */


object ExecutionEngineType extends Enumeration {
  type ExecutionEngineType = Value
  val LOCAL = Value
}

case class UserConfig(userArgs: Array[String]) extends ScallopConf(userArgs){
  implicit val engineConverter = singleArgConverter[ExecutionEngineType](ExecutionEngineType.withName)
  val day: ScallopOption[String] = opt[String]("day", descr = "Value of day to calculate top cookies, ex: \"2018-12-09\"", required = true, short = 'd')
  val file: ScallopOption[String] = opt[String]("file", descr = "Log file path to read cookies information", required = true, short = 'f')
  val top: ScallopOption[Int] = opt[Int]("top", descr = "No of Top K Cookies", required = false, default = Some(1))
  val engine: ScallopOption[ExecutionEngineType] = opt[ExecutionEngineType]("engine", descr = "Execution env to calculate top cookies", required = false, default = Some(ExecutionEngineType.LOCAL), short = 'e')(engineConverter)
  verify()
}
