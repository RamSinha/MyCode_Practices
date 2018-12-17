package com.careem.kafka.examples.api.exceptions

final case class APIException(private val message: String,
                              private val cause: Throwable = None.orNull)
  extends Exception(message, cause)
