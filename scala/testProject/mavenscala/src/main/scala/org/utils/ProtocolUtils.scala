package org.utils

/**
  * Created by ramsinha on 20/07/16.
  */

import java.net.URL;

/**
  * Util class providing methods to extract information of various component of URL.
  */
object ProtocolUtils {
  /**
    * Util method to retrieve Protocol name from URL.
    *
    * @param resourceURL Resource URL string format
    * @return Protocol name from URL.
    */
  def getProtocolName(resourceURL: String): String = {
    try {
      val url: URL = new URL(resourceURL)
      return url.getProtocol
    } catch {
      case mex: java.net.MalformedURLException => {
        println(s"Resource URL $resourceURL  is invalid");
        throw mex
      }
      case ex: Exception => {
        throw ex
      }
    }
  }

  /**
    * Util method to retrieve file name from URL.
    *
    * @param resourceURL Resource URL string format
    * @return File name from URL.
    */
  def getFileName(resourceURL: String): String = {
    try {
      val url: URL = new URL(resourceURL)
      return url.getPath
    } catch {
      case mex: java.net.MalformedURLException => {
        println(s"Resource URL $resourceURL  is invalid");
        throw mex
      }
      case ex: Exception => {
        throw ex
      }
    }
  }

  /**
    * Util method to retrieve host server  from URL.
    *
    * @param resourceURL Resource URL string format
    * @return Host server from URL.
    */
  def getHostServer(resourceURL: String): String = {
    try {
      val url: URL = new URL(resourceURL)
      return url.getHost
    } catch {
      case mex: java.net.MalformedURLException => {
        println(s"Resource URL $resourceURL  is invalid");
        throw mex
      }
      case ex: Exception => {
        throw ex
      }
    }
  }

  /**
    * Util method to retrieve port from URL.
    *
    * @param resourceURL Resource URL string format
    * @return Port from URL.
    */
  def getServerPort(resourceURL: String): String = {
    try {
      val url: URL = new URL(resourceURL)
      return if (url.getPort > 0) url.getPort.toString else ""
    } catch {
      case mex: java.net.MalformedURLException => {
        println(s"Resource URL $resourceURL  is invalid");
        throw mex
      }
      case ex: Exception => {
        throw ex
      }
    }
  }

  /**
    * Util method to retrieve  temp file name from resource filename.
    *
    * @param resourceLocation Local resource name.
    * @return Temp File name from resource filename.
    */
  def getTempFileName(resourceLocation: String): String = {
    val tempLocation = resourceLocation + ProcessorConstants.UNDERSCORE + ProcessorConstants.TEMP_SEPERATOR + ProcessorConstants.UNDERSCORE
    +System.currentTimeMillis / 1000

    return tempLocation
  }

  /**
    * Util method to retrieve directory name  from local file location.
    *
    * @param resourceDirectory Local directory name.
    * @return directory name  from local file location.
    */
  def getTargetDirectory(resourceDirectory: String): String = {
    if (resourceDirectory.endsWith("/")) resourceDirectory else resourceDirectory + "/"
  }

  def getServerAddress(resourceURL: String ): String ={
    return new URL(resourceURL).toExternalForm
  }

}

object ProcessorConstants {
  val TEMP_SEPERATOR = "tmp"
  val UNDERSCORE = "_"
}
