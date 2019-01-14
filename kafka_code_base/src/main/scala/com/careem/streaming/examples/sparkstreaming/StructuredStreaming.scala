package com.careem.streaming.examples.sparkstreaming

import org.apache.spark.sql.{DataFrame, Dataset, RelationalGroupedDataset}
import org.apache.spark.sql.streaming.StreamingQuery
import org.apache.spark.sql.types.StructType

object StructuredStreaming {
  def main(args: Array[String]): Unit = {
    import org.apache.spark.sql.SparkSession

    val spark = SparkSession
      .builder
      .appName("StructuredNetworkWordCount")
      .master("local[2]")
      .getOrCreate()



    val lines = spark.readStream
      .format("socket")
      .option("host", "localhost")
      .option("port", 9999)
      .load()

    // Split the lines into words

    //import org.apache.spark.sql.Encoders

    case class DummyClass (first: String , second : String, third: String)
    val k = new StructType().add("x", "string").add("y", "string").add("z", "string")
    import spark.implicits._

    val words = lines.as[String].flatMap(_.split(" ").map(x => {
      val parts: Array[String] = x.split("#")
      (parts(0), parts(1), parts(2))
    })).toDF("x", "y", "z")

    println(words.columns.toSeq)

    // Generate running word count
    //    val wordCounts = words.groupBy("value").count()

    val wordCounts = words.groupBy("x", "y", "z").count()
    val query: StreamingQuery = wordCounts.writeStream
      .outputMode("complete")
      .format("console")
      .start()

    query.awaitTermination()
  }
}
