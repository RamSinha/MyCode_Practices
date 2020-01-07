package com.parsers.csv

import org.apache.spark.sql.{DataFrame, SparkSession}
import org.rogach.scallop._

/**
  * @author ram.sinha on 12/23/19
  */

trait Parser {
  def read(file: List[String]): DataFrame
}


object Parser {
  def apply(options: ParserOptionConf, spark: SparkSession): Parser = {
    options.format.toOption match {
      case Some("csv") => new SparkCSVParser(spark, options)
      case Some("custom_csv") => new CustomCSVParser(spark, options)
      case Some(_) => throw new Exception("Format not supported")
    }
  }
}

class SparkCSVParser(spark: SparkSession, options: ParserOptionConf) extends Parser {
  override def read(files: List[String]): DataFrame = {
    spark.read.
      option("quote", options.quote.toOption.get.toString).
      option("delimiter", options.delimiter.toOption.get.toString).
      option("encoding", options.encoding.toOption.get.toString).
      option("header", options.header.toOption.get).
      option("multiline", options.multiline.toOption.get.toString).
      csv(files: _*)
  }
}

class ParserOptionConf(args: Array[String]) extends ScallopConf(args) with Serializable{
  val quote: ScallopOption[Char] = opt[Char]("quote", descr = "Quoting character", required = false, default = Some('"'))
  val linesep: ScallopOption[Char] = opt[Char]("linesep", descr = "Line separator", required = false, default = Some('\n'))
  val delimiter: ScallopOption[Char] = opt[Char]("delimiter", descr = "Field delimiter", required = false, default = Some(','))
  val escape: ScallopOption[Char] = opt[Char]("escape", descr = "Field escape character", required = false, default = Some('\\'))
  val ignoreWordOutSideQuote: ScallopOption[Boolean] = opt[Boolean]("ignoreWordOutSideQuote", descr = "set to ignore partially quoted word outside quote boundary", required = false, default = Some(false))
  val ignoreWhiteSpaces: ScallopOption[Boolean] = opt[Boolean]("ignoreWhiteSpaces", descr = "Ignore whitespace in front of quote word", required = false, default = Some(true))
  val encoding: ScallopOption[String] = opt[String]("encoding", descr = "Encoding format", required = false, default = Some("UTF-8"))
  val header: ScallopOption[Boolean] = opt[Boolean]("header", descr = "File contains header", required = false, default = Some(false))
  val multiline: ScallopOption[Boolean] = opt[Boolean]("multiLine", descr = "Handle newline character embedded in the column ", required = false, default = Some(true))
  val format: ScallopOption[String] = opt[String]("format", descr = "File format", required = false, default = Some("csv"))
  val files: ScallopOption[List[String]] = opt[List[String]]("files", descr = "List of files to read", required = false)
  val top: ScallopOption[Int] = opt[Int]("top", descr = "No of line to display", required = false, default = Some(100))
  verify()
}