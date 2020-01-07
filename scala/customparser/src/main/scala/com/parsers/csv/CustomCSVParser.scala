package com.parsers.csv

import java.io.IOException

import org.apache.spark.sql.{DataFrame, SparkSession}

object CustomCSVParser {
  val NULL_CHARACTER = '\0'

  @throws[IOException]
  def parseLine(nextLine: String, quote: Char, delimiter: Char, lineSep: Char): List[String] = {
    var inCell = false // Flag to hold info if we are in csv cell
    val sb = new StringBuilder()
    val outputBuffer = new scala.collection.mutable.ArrayBuffer[String]()
    var inQuotes = false // Flag to denote if we are in quoted field
    var i = 0
    while (i < nextLine.length) {
      val c = nextLine.charAt(i)
      if (c == quote) {
        inQuotes = !inQuotes //
      }
      else if (c == delimiter && !inQuotes) {
        outputBuffer += sb.toString()
        sb.setLength(0)
        inCell = false
      }
      else {
        sb.append(c)
        inCell = true
      }
      i += 1
    }
    if (sb.nonEmpty){
      outputBuffer += sb.toString()
    }

    if (!inCell){
      outputBuffer += "NA"
    }
    outputBuffer.toList
//    val row = new GenericInternalRow(outputBuffer.length)
//    for (i <- Range(0, outputBuffer.length)){
//      row(i) = outputBuffer(i)
//    }
//    row
  }
}

class CustomCSVParser(spark: SparkSession, options: ParserOptionConf) extends Parser with Serializable {

  import CustomCSVParser._

  val userOptions = options
  val quote = userOptions.quote.toOption.get
  val delimiter = userOptions.delimiter.toOption.get
  val linesep = userOptions.linesep.toOption.get

  isEqual(quote, delimiter) match {
    case true  => throw new Exception("quote and delim can't be same")
    case _ => // Fine
  }
  assert(userOptions.linesep.toOption.get != NULL_CHARACTER, "Null character can't be line separator")

  private def isEqual(c1: Char, c2: Char) = c1 != NULL_CHARACTER && c1 == c2
  override def read(file: List[String]): DataFrame = {
    val quote = this.quote
    val delimiter = this.delimiter
    val linesep = this.linesep
    import spark.implicits._
    spark.
      read.
      format("text").
      load(file: _*).
      map(x => CustomCSVParser.parseLine(x.toString(), quote, delimiter, linesep)).
      toDF()
  }
}