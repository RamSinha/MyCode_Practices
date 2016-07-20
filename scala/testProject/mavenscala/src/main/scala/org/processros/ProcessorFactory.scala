package org.processors


import java.io.File
import java.net.URL
import java.io.FileOutputStream
import java.io.IOException

import java.nio.channels.Channels
import java.nio.channels.ReadableByteChannel

import org.apache.commons.io.FileUtils
import org.apache.commons.net.ftp.FTP
import org.apache.commons.net.ftp.FTPClient
import org.apache.commons.net.ftp.FTPReply

import org.utils.{ProcessorConstants, ProtocolUtils, _};

/**
  * Created by ramsinha on 20/07/16.
  */


/**
  * This is an ENUM representing supported protocols
  */

object PROTOCOLS extends Enumeration {
  val FTP = MyValue("ftp")
  val SFTP = MyValue("sftp")
  val HTTP = MyValue("http")

  def MyValue(name: String): Value with Matching =
    new Val(nextId, name) with Matching

  /**
    * Extractor Pattern
    *
    * @param s
    * @return
    */
  def unapply(s: String): Option[Value] =
    values.find(s == _.toString)

  trait Matching {
    /**
      * Extractor Pattern
      *
      * @param s
      * @return
      */
    def unapply(s: String): Boolean =
      (s == toString)
  }

}


/**
  * Factory class, which provides a handle to create instance of  [[org.processors.Processor]]
  */
object ProcessorFactory {

  /**
    *
    * @param protocol Name of the protocol for which processor is required
    * @return Returns an instance of [[org.processors.Processor]]
    */
  def getProcessor(protocol: String): Processor = {
    protocol match {
      case PROTOCOLS.FTP() => FTPProcessor
      case PROTOCOLS.SFTP() => SFTPProcessor
      case PROTOCOLS.HTTP() => HTTPProcessor
    }
  }
}

/**
  * Generic processor trait, To support more protocol please extend this trait and implement process file method
  */
trait Processor {
  def processFile(resourceLocation: String, targetLocation: String)
}

object FTPProcessor extends Processor {
  override
  def processFile(resourceLocation: String, targetDirectory: String) = {
    /*
    code to process FTP files
     */
    try {
      var ftp: FTPClient = new FTPClient();
      val serverAddress = ProtocolUtils.getServerAddress(resourceLocation)
      ftp.connect(serverAddress)
      val reply: Int = ftp.getReply
      if (FTPReply.isPositiveCompletion(reply)) {
        println(s"Successfully connected to $serverAddress")
      } else {
        throw new IOException(s"Failed to connect to $serverAddress")
      }


      var result: Boolean = true
      val targetLocation = ProtocolUtils.getTargetDirectory(targetDirectory) + ProtocolUtils.getFileName(resourceLocation)
      val tempFileLocation = ProtocolUtils.getTempFileName(targetLocation)

      try {
        val targetFile: File = new File(targetLocation);
        if (targetFile.exists()) {
          println(s"Target file $targetLocation already exists, please remove it.")
          throw new Exception(s"Target file $targetLocation already exists, please remove it.")
        }
        var downloadfileStream = new FileOutputStream(tempFileLocation);
        ftp.retrieveFile(ProtocolUtils.getFileName(resourceLocation), downloadfileStream);
      } catch {
        case ex: Exception => {
          /**
            * If there is any exception no need to move partial file to actual target location.
            */
          println(s"Failed to download resource $resourceLocation")
          result = false
        }
      } finally {
        if (result) {
          var file: File = new File(targetLocation)
          if (file.exists()) {
            println(s"File with name $targetLocation  already exist at target location. Please remove older file.")
          } else {
            FileUtils.moveFile(new File(tempFileLocation), new File(targetLocation))
          }
        }
        val tempFileDescriptor: File = new File(tempFileLocation);
        if (tempFileDescriptor.exists()) {
          FileUtils.forceDelete(tempFileDescriptor)
        }
      }
    } catch {
      case ex: IOException => println(ex.getMessage); throw ex
      case ex: Exception => println(s"Failed to download $resourceLocation"); throw ex
    }


  }
}

object HTTPProcessor extends Processor {
  override
  def processFile(resourceLocation: String, targetDirectory: String) = {
    /*
    code to process HTTP files
    */
    var result: Boolean = true
    val targetLocation = ProtocolUtils.getTargetDirectory(targetDirectory) + ProtocolUtils.getFileName(resourceLocation)
    val tempFileLocation = ProtocolUtils.getTempFileName(targetLocation)
    try {
      val remote_resource: URL = new URL(resourceLocation);
      val readableByteChannel: ReadableByteChannel = Channels.newChannel(remote_resource.openStream());
      val fileOutputStream: FileOutputStream = new FileOutputStream(tempFileLocation);
      fileOutputStream.getChannel().transferFrom(readableByteChannel, 0, Long.MaxValue);
    } catch {
      case ex: Exception => {
        /**
          * If there is any exception no need to move partial file to actual target location.
          */
        println(s"Failed to download resource $resourceLocation")
        result = false
      }
    } finally {
      if (result) {
        var file: File = new File(targetLocation)
        if (file.exists()) {
          println(s"File with name $targetLocation  already exist at target location. Please remove older file.")
        } else {
          FileUtils.moveFile(new File(tempFileLocation), new File(targetLocation))
        }
      }
      val tempFileDescriptor: File = new File(tempFileLocation);
      if (tempFileDescriptor.exists()) {
        FileUtils.forceDelete(tempFileDescriptor)
      }
    }
  }
}

object SFTPProcessor extends Processor {
  override
  def processFile(resourceLocation: String, targetLocation: String) = {
    /*
    code to process SFTP files
     */
    throw new Exception("SFTP: Protocol not supported")
  }
}

object processorTester {
  def main(args: Array[String]) {
    //    HTTPProcessor.processFile("https://www.google.co.in", "/Users/ramsinha/Downloads/processedFiles/test.html")
    //    HTTPProcessor.processFile("https://www.google.co.in", "/Users/ramsinha/Downloads/processedFiles/test_1.html")
    //    HTTPProcessor.processFile("https://www.google.co.in", "/Users/ramsinha/Downloads/processedFiles/test_2.html")
    FileUtils.forceDelete(new File("/Users/ramsinha/Downloads/fileDontExist"))
  }
}

