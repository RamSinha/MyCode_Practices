package com.util

import java.io.{BufferedWriter, FileWriter}
import java.nio.file.Files

import com.qc.dao.CookieRecord

/**
 * @author ram.sinha on 8/27/21
 */
object DataGeneratorUtil {
  def getDataFile(rawRecords: List[String]) = {
    val file = Files.createTempFile( "cookie-test", ".csv" ).toFile
    file.setWritable( true )
    file.setReadable( true )
    file.setExecutable( true )
    file.deleteOnExit()
    val bw = new BufferedWriter( new FileWriter( file ) )
    rawRecords.foreach { x => bw.write( x ); bw.newLine() }
    bw.close()
    file.getAbsolutePath
  }

  def getDataSet(rawRecords: List[String]) = {
    rawRecords.flatMap(CookieRecord.apply(_)).toIterator
  }
}
