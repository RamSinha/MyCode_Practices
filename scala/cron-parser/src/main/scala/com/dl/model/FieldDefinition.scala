package com.dl.model

/**
 * @author ram.sinha on 1/23/22
 */

/**
 * Model object encapsulating ScheduleType and DataPoints of execution
 * @param scheduleType
 * @param scheduleDescription
 */
case class FieldDefinition(scheduleType: Field.Value, scheduleDescription: String) {
  override def toString: String = {
    s"${scheduleType.name.toLowerCase().padTo(14 , " ").mkString("", "", ":")} ${scheduleDescription}"
  }
}
