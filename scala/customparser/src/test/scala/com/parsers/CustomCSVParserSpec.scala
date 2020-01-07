package com.parsers

/**
  * @author ram.sinha on 1/7/20
  */

import java.io.{File, PrintWriter}

import com.parsers.csv.{Parser, ParserOptionConf, SparkService}
import com.typesafe.config.ConfigFactory
import org.scalatest.{FlatSpec, Matchers}

import scala.collection.mutable

/**
  * @author ram.sinha on 12/23/19
  */
class CustomCSVParserSpec extends FlatSpec with Matchers {
  val spark = new SparkService(ConfigFactory.load()).getSession()

  "Parser " should "handle field delimiters inside quoted cells" in {
    val file = TestUtils.createFile("test1")
    TestUtils.writeToTempFile("""a,"b,c,d",e""", file)
    val formatOption = new ParserOptionConf(Array("--files", file.getAbsolutePath, "--format", "custom_csv"))
    val parser = Parser(formatOption, spark)
    val df = parser.read(formatOption.files.toOption.get)
    val record = df.collect().head.get(0).asInstanceOf[mutable.WrappedArray[String]]
    record(0) shouldBe "[a"
    record(1) shouldBe """b,c,d"""
    record(2) shouldBe "e]"
  }


  "if two consecutive field delimiters mean the value is absent/null then Parser " should "emit null for missing field" in {
    val file = TestUtils.createFile("test1")
    TestUtils.writeToTempFile(""""a",,c""", file)
    val formatOption = new ParserOptionConf(Array("--files", file.getAbsolutePath, "--format", "custom_csv"))
    val parser = Parser(formatOption, spark)
    val df = parser.read(formatOption.files.toOption.get)
    val record = df.collect().head.get(0).asInstanceOf[mutable.WrappedArray[String]]
    record.length shouldBe 3
  }

  "If a field delimiter at the end of the line  then Parser " should "emit null for missing field" in {
    val file = TestUtils.createFile("test1")
    TestUtils.writeToTempFile(""""a",b,""", file)
    val formatOption = new ParserOptionConf(Array("--files", file.getAbsolutePath, "--format", "custom_csv"))
    val parser = Parser(formatOption, spark)
    val df = parser.read(formatOption.files.toOption.get)
    val record = df.collect().head.get(0).asInstanceOf[mutable.WrappedArray[String]]
    record.length shouldBe 3
  }

  "Parser " should "treat partially quoted field as the single word" in {
    val file = TestUtils.createFile("test1")
    TestUtils.writeToTempFile(""""abc,"onetwo,three,doremi""", file)
    val formatOption = new ParserOptionConf(Array("--files", file.getAbsolutePath, "--format", "custom_csv"))
    val parser = Parser(formatOption, spark)
    val df = parser.read(formatOption.files.toOption.get)
    val record = df.collect().head.get(0).asInstanceOf[mutable.WrappedArray[String]]
    record(0) shouldBe "[abc,onetwo"
    record(1) shouldBe """three"""
    record(2) shouldBe "doremi]"
  }
}

object TestUtils {

  def createFile(fileName: String, ext: String = "csv") = {
    val tempFile = File.createTempFile(fileName, ext)
    tempFile.deleteOnExit()
    tempFile
  }

  def writeToTempFile(contents: String, tempFile: File): File = {
    new PrintWriter(tempFile) {
      try {
        write(contents)
      } finally {
        close()
      }
    }
    tempFile
  }
}