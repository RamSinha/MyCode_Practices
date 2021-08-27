package com.dataloader

import com.qc.config.UserConfig
import com.qc.dataloader.DataLoaderFactory
import com.qc.dataloader.impl.FileBasedDataLoaderWithDataFilter
import com.typesafe.config.ConfigFactory
import com.util.DataGeneratorUtil
import org.scalatest.{FlatSpec, Matchers}

import scala.collection.mutable

/**
 * @author ram.sinha on 8/27/21
 */
class FileBasedDataLoaderWithDataFilterSpec extends FlatSpec with Matchers{
    val rawRecords = List(
      "AtY0laUfhglK3lC7,2018-12-09T14:19:00+00:00",
      "SAZuXPGUrfbcn5UA,2018-12-09T10:13:00+00:00",
      "5UAVanZf6UtGyKVS,2018-12-09T07:25:00+00:00",
      "AtY0laUfhglK3lC7,2018-12-09T06:19:00+00:00",
      "SAZuXPGUrfbcn5UA,2018-12-08T22:03:00+00:00",
      "4sMM2LxV07bPJzwf,2018-12-08T21:30:00+00:00",
      "fbcn5UAVanZf6UtG,2018-12-08T09:30:00+00:00",
      "4sMM2LxV07bPJzwf,2018-12-07T23:30:00+00:00")

  "FileLoaded " should "correctly parse the input file" in {
    val file = DataGeneratorUtil.getDataFile(rawRecords)
    val userConfig = UserConfig(Array("-f", file, "-d", "2018-12-09"))
    val dataLoader = DataLoaderFactory.getDataLoader(userConfig, ConfigFactory.load())
    val parsedRecord = dataLoader.loadData()
    parsedRecord.length shouldBe 4
  }

}
