package com.dl.model

/**
 * @author ram.sinha on 1/23/22
 */

object Field extends Enumeration {
  class CronField (val order: Int, val name: String, val startRange: Int, val endRange: Int)  extends super.Val {
    def validate(values: List[Int]): Boolean = ! values.exists(x => x < this.startRange || x > this.endRange)
  }
  implicit def FieldToCronField(x: Value): CronField = x.asInstanceOf[CronField]
  val MINUTE = new CronField(0, "MINUTE", 0, 59)
  val HOUR = new CronField(1, "HOUR", 0, 23)
  val DAY_OF_MONTH = new CronField(2, "DAY_OF_MONTH", 1, 31)
  val MONTH = new CronField(3, "MONTH", 1, 12)
  val DAY_OF_WEEK = new CronField(4, "DAY_OF_WEEK", 0, 7)
  val COMMAND = new CronField(5, "COMMAND", -1 , -1)
}


