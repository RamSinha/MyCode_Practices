package com.qc.dataloader.impl

import com.qc.config.UserConfig
import com.qc.dao.CookieRecord
import com.qc.dataloader.DataLoader
import org.joda.time.format.DateTimeFormat
import org.joda.time.{DateTime, DateTimeZone}

import scala.io.Source

/**
 * @author ram.sinha on 8/27/21
 */
case class FileBasedDataLoaderWithDataFilter(userConfig: UserConfig) extends DataLoader {
  val dateTimeFormatter = DateTimeFormat.forPattern( "yyyy-MM-dd" ).withZone( DateTimeZone.UTC )

  override def loadData(): Iterator[CookieRecord] = {
    val specificDate = DateTime.parse( userConfig.day(), dateTimeFormatter )
    Source
      .fromFile( userConfig.file() )
      .getLines
      .flatMap( CookieRecord.apply( _ ) )
      .filter( x => x.timeStamp.minusMillis( x.timeStamp.getMillisOfDay ).equals( specificDate ) ) // This can be further improved by stopping parsing after we find first record that is less than specific date.
  }
}
