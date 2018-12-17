package com.careem.streaming.examples.api.exceptions

final case class MalformedRequestException(val message: String,
                                           val cause: Throwable = None.orNull)
  extends Exception(message, cause)