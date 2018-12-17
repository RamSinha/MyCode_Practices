package com.careem.streaming.examples.kafka

import java.sql.Timestamp
import java.util.Properties

import com.careem.streaming.examples.api.dao.ServiceDAO.{DriverPingInfo, TripRequestData}
import com.careem.streaming.examples.api.repository.RepositoryFactory
import org.apache.kafka.clients.consumer.{ConsumerRecords, KafkaConsumer}
import org.apache.kafka.common.serialization.StringDeserializer

import scala.collection.JavaConversions._

object MDConsumer extends App {
  val props = new Properties()

  import org.apache.kafka.clients.consumer.ConsumerConfig

  props.put(ConsumerConfig.BOOTSTRAP_SERVERS_CONFIG, KafkaConstants.KAFKA_BROKERS)
  props.put(ConsumerConfig.GROUP_ID_CONFIG, KafkaConstants.GROUP_ID_CONFIG_D)
  props.put(ConsumerConfig.KEY_DESERIALIZER_CLASS_CONFIG, classOf[StringDeserializer].getName)
  props.put(ConsumerConfig.VALUE_DESERIALIZER_CLASS_CONFIG, classOf[StringDeserializer].getName)
  props.put(ConsumerConfig.MAX_POLL_RECORDS_CONFIG, KafkaConstants.MAX_POLL_RECORDS)
  props.put(ConsumerConfig.ENABLE_AUTO_COMMIT_CONFIG, "false")
  props.put(ConsumerConfig.AUTO_OFFSET_RESET_CONFIG, KafkaConstants.OFFSET_RESET_EARLIER)


  val consumer = new KafkaConsumer[String, String](props)
  consumer.subscribe(List(KafkaConstants.TOPIC_NAME_DRIVER))
  while (true) {
    println("Reading messages from kafka")
    pollKafkaConsumer(consumer)
    println("taking rest")
    Thread.sleep(5000)
  }

  private def pollKafkaConsumer(kafkaConsumer: KafkaConsumer[String, String]): Unit = {
    val records = kafkaConsumer.poll(1000)
    processRecords(records)
    syncCommitOffset(kafkaConsumer)
  }

  private def processRecords(records: ConsumerRecords[String, String]): Unit = {
    for (record <- records) {
      record.topic() match {
        case KafkaConstants.TOPIC_NAME_TRIP => {

          println(s"Trip Message found $record")
          val parts = record.value.split("#")
          RepositoryFactory.tripRequestRepository.addEntity(
            TripRequestData(None, parts(0), s"${parts(1)}*${parts(2)}", s"${parts(3)}*${parts(4)}",new Timestamp((parts(5).toLong - 14400)*1000)  )
          )
        }
        case KafkaConstants.TOPIC_NAME_DRIVER =>
          {
            println(s"Driver ping Message found $record")
            val parts = record.value.split("#")
            RepositoryFactory.driverPingRepository.addEntity(
              DriverPingInfo(None, parts(0), "DUMMY", s"${parts(1)}*${parts(2)}",new Timestamp((parts(3).toLong - 14400)*1000))
            )
          }
        case _ => println("Unknown topic")
      }

      println(s"Message found $record")
    }
  }

  private def syncCommitOffset(kafkaConsumer: KafkaConsumer[String, String]): Unit = {
    kafkaConsumer.commitAsync()
  }
}
