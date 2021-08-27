package com.execution

import com.qc.config.UserConfig
import com.qc.execution.ExecutionEngineFactory
import com.typesafe.config.ConfigFactory
import com.util.DataGeneratorUtil
import org.scalatest.{FlatSpec, Matchers}

/**
 * @author ram.sinha on 8/28/21
 */
class LocalEngineSpec extends FlatSpec with Matchers {
  val rawRecords = List(
    "AtY0laUfhglK3lC7,2018-12-09T14:19:00+00:00",
    "SAZuXPGUrfbcn5UA,2018-12-09T10:13:00+00:00",
    "5UAVanZf6UtGyKVS,2018-12-09T07:25:00+00:00",
    "AtY0laUfhglK3lC7,2018-12-09T06:19:00+00:00",
    "SAZuXPGUrfbcn5UA,2018-12-08T22:03:00+00:00",
    "4sMM2LxV07bPJzwf,2018-12-08T21:30:00+00:00",
    "fbcn5UAVanZf6UtG,2018-12-08T09:30:00+00:00",
    "4sMM2LxV07bPJzwf,2018-12-07T23:30:00+00:00")

  "LocalEngine " should "correctly calculate the top hit cookies" in {
    val userConfig = UserConfig(Array("-f", "", "-d", "2018-12-09"))
    val executionEngine = ExecutionEngineFactory.createExecutionEngine(userConfig, ConfigFactory.load()) // computation engine
    DataGeneratorUtil.getDataSet(rawRecords).map(executionEngine.accept)
    executionEngine.topResult.map(_.cookieName) should be eq  List("AtY0laUfhglK3lC7")
  }


  "LocalEngine " should "correctly calculate the top hit cookies correctly if multiple cookies qualifies" in {
    val userConfig = UserConfig(Array("-f", "", "-d", "2018-12-08"))
    val executionEngine = ExecutionEngineFactory.createExecutionEngine(userConfig, ConfigFactory.load()) // computation engine
    DataGeneratorUtil.getDataSet(rawRecords).map(executionEngine.accept)
    executionEngine.topResult.map(_.cookieName) should be eq  List("4sMM2LxV07bPJzwf", "SAZuXPGUrfbcn5UA", "fbcn5UAVanZf6UtG") // sorted order
  }
}
