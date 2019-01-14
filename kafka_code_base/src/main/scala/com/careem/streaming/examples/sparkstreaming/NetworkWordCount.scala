package com.careem.streaming.examples.sparkstreaming


import org.apache.spark._
import org.apache.spark.streaming._
import org.apache.spark.rdd.RDD
import org.apache.spark.sql.types.{IntegerType, StringType, StructField, StructType}
import org.apache.spark.sql.{Row, SQLContext, SparkSession}
import org.apache.spark.streaming.dstream.DStream

import scala.collection.mutable.Queue


object NetworkWordCount extends App {
  val conf = new SparkConf().setMaster("local[2]").setAppName("NetworkWordCount")
  val ssc = new StreamingContext(conf, Seconds(10))
  val lines = ssc.socketTextStream("localhost", 9999)
  val words = lines.flatMap(_.split(" "))
  val pairs = words.map(word => (word, 1))
  val wordCounts = pairs.reduceByKey(_ + _)

  // Print the first ten elements of each RDD generated in this DStream to the console
  wordCounts.print()
  pairs.print()

  ssc.start()
  ssc.awaitTermination()
}

object QueuedDStreamExample extends App {

  import org.apache.spark._
  import org.apache.spark.streaming._
  import org.apache.spark.rdd.RDD
  import org.apache.spark.sql.types.{IntegerType, StringType, StructField, StructType}
  import org.apache.spark.sql.{Row, SQLContext, SparkSession}
  import org.apache.spark.streaming.dstream.DStream

  import scala.collection.mutable.Queue

  import org.apache.spark._
  import org.apache.spark.streaming._
  import org.apache.spark.rdd.RDD
  import scala.collection.mutable.Queue
  import org.apache.spark.sql.SparkSession
  import org.apache.log4j.Logger
  import org.apache.log4j.Level

  Logger.getLogger("org").setLevel(Level.ERROR)
  Logger.getLogger("akka").setLevel(Level.ERROR)

  val conf = new SparkConf().setMaster("local[2]").setAppName("NetworkWordCount")
  val ssc = new StreamingContext(conf, Seconds(10))

  val rdd1 = ssc.sparkContext.parallelize(Array((1,4), (1,5), (1,6), (1,5), (1,6) , (1,5), (1,6) , (1,5), (1,6)))
  val rdd2 = ssc.sparkContext.parallelize(Array((1,"FortyFour"), (1,"FiftyFive"), (1,"SixtySix"), (1,"FiftyFive"), (1,"SixtySix"), (1,"FiftyFive"), (1,"SixtySix")))
  val rdd3 = ssc.sparkContext.parallelize(Array(1,2,3,4,5))
  val rdd4 = ssc.sparkContext.parallelize(Array(6,7,8,9,10))

  val first  = ssc.queueStream(Queue(rdd1), false)
  val second = ssc.queueStream(Queue(rdd2), false)
  val third  = ssc.queueStream(Queue(rdd3), false)
  val fourth = ssc.queueStream(Queue(rdd3,rdd4), true)


  val coGrouped = first.cogroup(second)
  val sparkSession = SparkSession.builder.config(ssc.sparkContext.getConf).getOrCreate()
  import sparkSession.implicits._
  val sqlContext = sparkSession.sqlContext

  def dfSchema(columnNames: Seq[String]): StructType =
    StructType(
      Seq(
        StructField(name = "age", dataType = IntegerType, nullable = false)
      )
    )

  val schema = dfSchema(Seq("age"))

  def row(age: Int): Row = Row(age)

  fourth.foreachRDD(rdd => {
    val df = sparkSession.createDataFrame(rdd.map(row), schema)
    df.createTempView("test")
    val df_1 = sqlContext.sql("select sum(age) from test")
    println(df_1.schema)
    df_1.collect().foreach(println)
    sqlContext.dropTempTable("test")
    println(s"count of RDD is ${rdd.count()}")
    rdd.collect().foreach(println(_))
    rdd.saveAsTextFile("/Users/ramsinha/Downloads/testrdd")
  })
  ssc.start()

//  val rddQueue = new Queue[RDD[(Int,Int)]]
//  rddQueue.enqueue(rdd1)
//  rddQueue.enqueue(rdd2)
//  val numsDStream = ssc.queueStream(rddQueue, false)
//  val plusOneDStream = numsDStream.map(x => x + 1)
//   numsDStream.print
  ssc.start()
  ssc.stop(false)
}