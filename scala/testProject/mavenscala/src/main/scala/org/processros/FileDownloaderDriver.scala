package org.processors

import org.processors._
import org.utils._
import java.util.concurrent._

/**
  * Created by ramsinha on 20/07/16.
  */
object FileDownloaderDriver {
  def main(args: Array[String]) {

    if (args.length < 2) {
      println("Usage:\n FileDownloaderDriver <localDirectoryPath> file_1 file_2 file_3 ")
      System.exit(1)
    }

    val downloadDirectory: String = args(0)

    val listOfFiles = args slice(1, args.length)
    val executorService: ExecutorService = Executors.newFixedThreadPool(10);
    println(s"download directory is $downloadDirectory")
    for (resource <- listOfFiles) {
      executorService.execute(new Runnable {
        override def run(): Unit = {
          try {
            println(s" resource is $resource")
            var processor = ProcessorFactory.getProcessor(ProtocolUtils.getProtocolName(resource))
            processor.processFile(resource, downloadDirectory)
          } catch {
            case ex: Exception => println(ex.getMessage); println(s"Failed to download $resource")
          }
        }
      })
    }
    executorService.shutdown();
  }
}
