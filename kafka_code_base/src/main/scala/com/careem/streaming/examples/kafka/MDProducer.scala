package com.careem.streaming.examples.kafka

import java.util.Properties

import org.apache.kafka.clients.producer.{KafkaProducer, ProducerConfig, ProducerRecord}
import org.apache.kafka.common.serialization.StringSerializer


object MDProducer extends App {
  val props = new Properties
  props.put(ProducerConfig.BOOTSTRAP_SERVERS_CONFIG, KafkaConstants.KAFKA_BROKERS)
  props.put(ProducerConfig.CLIENT_ID_CONFIG, KafkaConstants.CLIENT_ID)
  props.put(ProducerConfig.KEY_SERIALIZER_CLASS_CONFIG, classOf[StringSerializer])
  props.put(ProducerConfig.VALUE_SERIALIZER_CLASS_CONFIG, classOf[StringSerializer])
  props.put("request.required.acks", KafkaConstants.REQUIRED_ACKS)
  val producer = new KafkaProducer[String, String](props)
  for (m <- DataSetGenerator.getDriverDataStream) {
    println(s"Sending message $m to topic ${KafkaConstants.TOPIC_NAME_DRIVER}")
    val data = new ProducerRecord[String, String](KafkaConstants.TOPIC_NAME_DRIVER, m)
    producer.send(data)
  }
  producer.close
}
