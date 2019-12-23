package com.parsers

import java.io.{File, PrintWriter}

import com.parsers.csv.{Parser, ParserOptionConf, SparkService}
import com.typesafe.config.ConfigFactory
import org.scalatest.{FlatSpec, Matchers}

/**
  * @author ram.sinha on 12/23/19
  */
class CSVParserSpec extends FlatSpec with Matchers {
  val spark = new SparkService(ConfigFactory.load()).getSession()


  "Parser " should "read all csv file content correctly if there is multi line in the field" in {
    val file = TestUtils.createFile("test1")
    TestUtils.writeToTempFile(
      """a,"a split
                             cell"
                                |b,"something else"
                                |""".stripMargin, file)
    val formatOption = new ParserOptionConf(Array("--files", file.getAbsolutePath))
    val parser = Parser(formatOption, spark)
    val df = parser.read(formatOption.files.toOption.get)
    df.collect().length shouldBe 2
  }

  "Parser " should "handle field delimiters inside quoted cells" in {
    val file = TestUtils.createFile("test1")
    TestUtils.writeToTempFile("""a,"b,c,d",e""", file)
    val formatOption = new ParserOptionConf(Array("--files", file.getAbsolutePath))
    val parser = Parser(formatOption, spark)
    val df = parser.read(formatOption.files.toOption.get)
    val record = df.collect().head
    record.get(0) shouldBe "a"
    record.get(1) shouldBe """b,c,d"""
    record.get(2) shouldBe "e"
  }


  "if two consecutive field delimiters mean the value is absent/null then Parser " should "emit null for missing field" in {
    val file = TestUtils.createFile("test1")
    TestUtils.writeToTempFile(""""a",,c""", file)
    val formatOption = new ParserOptionConf(Array("--files", file.getAbsolutePath))
    val parser = Parser(formatOption, spark)
    val df = parser.read(formatOption.files.toOption.get)
    val record = df.collect().head
    record.length shouldBe 3
  }

  "If a field delimiter at the end of the line  then Parser " should "emit null for missing field" in {
    val file = TestUtils.createFile("test1")
    TestUtils.writeToTempFile(""""a",b,""", file)
    val formatOption = new ParserOptionConf(Array("--files", file.getAbsolutePath))
    val parser = Parser(formatOption, spark)
    val df = parser.read(formatOption.files.toOption.get)
    val record = df.collect().head
    record.length shouldBe 3
  }

  "Parser " should "treat partially quoted field as the single word" in {
    val file = TestUtils.createFile("test1")
    TestUtils.writeToTempFile(""""abc,"onetwo,three,doremi""", file)
    val formatOption = new ParserOptionConf(Array("--files", file.getAbsolutePath))
    val parser = Parser(formatOption, spark)
    val df = parser.read(formatOption.files.toOption.get)
    val record = df.collect().head
    record.get(0) shouldBe """"abc,"onetwo"""
    record.get(1) shouldBe """three"""
    record.get(2) shouldBe "doremi"
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