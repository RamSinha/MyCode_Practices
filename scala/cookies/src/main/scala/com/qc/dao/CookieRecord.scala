package com.qc.dao

import org.joda.time.{DateTime, DateTimeZone}
import org.joda.time.format.DateTimeFormat

import scala.util.Try

/**
 * @author ram.sinha on 8/27/21
 */
case class CookieRecord(cookieName: String, timeStamp: DateTime){
  override def hashCode(): Int = cookieName.hashCode
  override def equals(obj: Any): Boolean = obj.asInstanceOf[CookieRecord].cookieName.equalsIgnoreCase(this.cookieName)
}
object CookieRecord {
  val timeFormatter = DateTimeFormat.forPattern("yyyy-MM-dd'T'HH:mm:ssZZ").withZone(DateTimeZone.UTC)
  def apply(rawString: String): Option[CookieRecord] = {
    Try{
      val components = rawString.split(",")
      val cookieName =  components(0)
      val timeStamp =  DateTime.parse(components(1), timeFormatter)
      new CookieRecord( cookieName, timeStamp )
    }.toOption
  }
}
