package com.careem.streaming.examples.sparkstreaming

import com.careem.streaming.examples.kafka.KafkaConstants
import org.apache.spark.sql.SparkSession
import org.apache.spark.sql.types.{StringType, StructField, StructType, TimestampType}
import org.apache.spark.sql.functions._

object RTAPFLeadStreaming {

  val schema = StructType(Seq(
    StructField("Name", StringType, true),
    StructField("Email", StringType, true),
    StructField("Datetime", StringType, true),
    StructField("Location", StringType, true)
  ))


  def main(args: Array[String]): Unit = {

    import org.apache.log4j.{Level, Logger}

    Logger.getLogger("org").setLevel(Level.ERROR)

    val topicName = KafkaConstants.TOPIC_PF_LEAD

    val spark = SparkSession
      .builder
      .appName("RTAPFLeadStreaming")
      .master("local[2]")
      .getOrCreate()

    val rawTopicMessageDF = spark
      .readStream
      .format("kafka")
      .option("kafka.bootstrap.servers", KafkaConstants.KAFKA_BROKERS)
      .option("subscribe", topicName)
      .option("maxOffsetsPerTrigger", 20)
      .option("startingOffsets", "latest")
      .option("key.serializer", "org.apache.kafka.common.serialization.StringSerializer")
      .option("value.serializer", "org.apache.kafka.common.serialization.ByteArraySerializer")
      .load()

    val query = rawTopicMessageDF
      .selectExpr("CAST(value AS STRING) as json_data")
      .select(from_json(col("json_data"), schema = schema).as("leads"))
      .select("leads.*")
      .writeStream
      .format("console")
      .outputMode("append")
      .start()

    query.awaitTermination()
  }
}
