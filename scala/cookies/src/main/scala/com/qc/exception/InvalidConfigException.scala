package com.qc.exception

/**
 * @author ram.sinha on 8/27/21
 */
case class InvalidConfigException(private val message: String,
                       private val cause: Throwable = None.orNull)
  extends Exception( message, cause )