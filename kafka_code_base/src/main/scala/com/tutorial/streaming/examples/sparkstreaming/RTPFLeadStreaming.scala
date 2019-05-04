package com.tutorial.streaming.examples.sparkstreaming

import java.sql.Timestamp

import com.careem.streaming.examples.api.dao.ServiceDAO.LeadInfo
import com.careem.streaming.examples.api.repository.RepositoryFactory
import com.careem.streaming.examples.kafka.KafkaConstants
import org.apache.spark.sql.SparkSession
import org.apache.spark.sql.functions._
import org.apache.spark.sql.streaming.Trigger
import org.apache.spark.sql.types.{StringType, StructField, StructType}
import org.joda.time.format.DateTimeFormat

object RTAPFLeadStreaming {

  val schema = StructType(Seq(
    StructField("Name", StringType, true),
    StructField("Email", StringType, true),
    StructField("Datetime", StringType, true),
    StructField("Location", StringType, true)
  ))



  class SlickPostgresSink extends org.apache.spark.sql.ForeachWriter[org.apache.spark.sql.Row]{

    def open(partitionId: Long, version: Long):Boolean = {
      true
    }

    def process(value: org.apache.spark.sql.Row): Unit = {
      val dtf = DateTimeFormat.forPattern("MM-dd-yyyy HH:mm:ss")
      RepositoryFactory.pfLeadRepository.addEntity(
        LeadInfo(
          None,
          value(0).toString,
          value(1).toString,
          new Timestamp(dtf.parseDateTime(value(2).toString).getMillis),
          value(3).toString
        )
      )
    }

    def close(errorOrNull:Throwable):Unit = {
    }
  }

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
      .foreach(new SlickPostgresSink)
      .trigger(Trigger.ProcessingTime("5 seconds"))
      .outputMode("append")
      .start()

    query.awaitTermination()
  }
}
