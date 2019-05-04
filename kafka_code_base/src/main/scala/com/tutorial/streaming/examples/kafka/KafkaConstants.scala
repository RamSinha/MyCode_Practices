package com.tutorial.streaming.examples.kafka

object KafkaConstants {
  val KAFKA_BROKERS = "localhost:9092"
  val MESSAGE_COUNT = 1000
  val CLIENT_ID = "client1"
  val TOPIC_NAME_TRIP = "trip"
  val TOPIC_NAME_DRIVER = "driver"
  val TOPIC_PF_LEAD = "pf_lead"
  val GROUP_ID_CONFIG_T = "CG_T"
  val GROUP_ID_CONFIG_D = "CG_D"
  val MAX_NO_MESSAGE_FOUND_COUNT = 100
  val OFFSET_RESET_LATEST = "latest"
  val OFFSET_RESET_EARLIER = "earliest"
  val MAX_POLL_RECORDS = "1"
  val REQUIRED_ACKS = "1"
}
