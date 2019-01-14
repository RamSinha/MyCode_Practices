package com.careem.streaming.examples.sparkstreaming

import org.apache.spark.sql.SparkSession
import org.apache.spark.sql.expressions.Window
import za.co.absa.abris.avro.AvroSerDe._
import za.co.absa.abris.avro.read.confluent.SchemaManager
import za.co.absa.abris.avro.read.confluent.SchemaManager.SchemaStorageNamingStrategies._
import za.co.absa.abris.avro.schemas.policy.SchemaRetentionPolicies.RETAIN_SELECTED_COLUMN_ONLY

import scala.concurrent.Future
import scala.util.Try

object RTAStreaming {

  def main(args: Array[String]): Unit = {

    import org.apache.log4j.{Level, Logger}

    Logger.getLogger("org").setLevel(Level.ERROR)
    val checkpoint_dir = "file:///Users/ramsinha/Downloads/checkpoint/rta"
    val schemaRegistryURL = "http://schema-registry-blackhole.careem-engineering.com:8081"
    val props = Map("schema.registry.url" -> schemaRegistryURL)
    val topicName = "careemdb_careem_user"

    val spark = SparkSession
      .builder
      .appName("StructuredNetworkWordCount")
      .master("local[1]")
      .getOrCreate()

    val schemaRegistryConf = Map(
      SchemaManager.PARAM_SCHEMA_REGISTRY_URL -> schemaRegistryURL,
      SchemaManager.PARAM_SCHEMA_REGISTRY_TOPIC -> topicName,
      SchemaManager.PARAM_VALUE_SCHEMA_NAMING_STRATEGY -> TOPIC_NAME, //, RECORD_NAME, TOPIC_RECORD_NAME,
      SchemaManager.PARAM_VALUE_SCHEMA_ID -> "latest") // set to "latest" if you want the latest schema version to used


    val rawTopicMessageDF = spark
      .readStream
      .format("kafka")
      .option("kafka.bootstrap.servers", "kafka1-blackhole.careem-engineering.com:9092,kafka2-blackhole.careem-engineering.com:9092,kafka3-blackhole.careem-engineering.com:9092")
      .option("subscribe", topicName)
      .option("maxOffsetsPerTrigger", 20)
      .option("startingOffsets", "earliest")
      .fromConfluentAvro("value", None, Some(schemaRegistryConf))(RETAIN_SELECTED_COLUMN_ONLY)
    import org.apache.spark.sql.functions._
    import org.apache.spark.sql.types._

    val query = rawTopicMessageDF
      .select(unix_timestamp(from_unixtime(col("ts"), "yyyy-MM-dd HH:mm:ss")).cast(TimestampType).as("tts"), col("data.id").as("id"), col("*"))
      .select(window(col("tts"), "1 days"), col("*"))
      .writeStream
      .format("memory")
      .outputMode("append")
      .queryName("test")
      .start()

    Future {
      while (true) {
        Try{
          val df = spark.sql("select * from test").withColumn("rw", row_number().over(Window.partitionBy("data.id").orderBy(desc("tts")))).filter("rw=1")
          df.createOrReplaceGlobalTempView("user")
          df.printSchema()
          println("iteration start")
          spark.sql("select tts, data.id from global_temp.user").foreach(println(_))
          println("iteration done")
          Thread.sleep(2000)
        }.recoverWith({case ex: Exception => {
          ex.printStackTrace()
          Try()
        }})
        }
    }(scala.concurrent.ExecutionContext.global)
    query.awaitTermination()
  }
}
