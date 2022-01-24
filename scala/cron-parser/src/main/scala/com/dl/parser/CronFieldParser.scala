package com.dl.parser

import com.dl.exception.{InvalidInputException, OutOfRangeException}
import com.dl.model.{Field, FieldDefinition}

/**
 * @author ram.sinha on 1/23/22
 */
object CronFieldParser {
  val SLASH  = '/'
  val ASTERISK  = '*'
  val DASH  = '-'
  val SPECIAL_CHARS_MINUS_ASTERISK = List ( '/', '-', ',')

  /**
   * Core business logic
   * Method parses the field expression for every schedule type recursively
   * @param expr
   * @param fieldType
   * @return
   */
  def parserField(expr : String, fieldType: Field.Value) : FieldDefinition = {
    fieldType match {
      case Field.COMMAND => FieldDefinition(fieldType, expr)
      case x => {
        val schedulePoints = getSchedulePoints(expr, x)
        if (!fieldType.validate(schedulePoints)) {
          throw OutOfRangeException(s"Invalid range for schedule ${fieldType.name} ")
        }
        FieldDefinition(fieldType, schedulePoints.mkString(" "))
      }
    }
  }

  def getSchedulePoints(expr: String, fieldType: Field.Value): List[Int] = {
    if (!expr.exists(SPECIAL_CHARS_MINUS_ASTERISK.contains)){
      if (expr.equalsIgnoreCase(ASTERISK.toString)) {
        (fieldType.startRange to fieldType.endRange).toList
      }else {
        List(expr.toInt)
      }
    }else {
      val parts = expr.split( "," )
      if (parts.length > 1 ){
        parts.foldLeft(List.empty[Int])((x: List[Int], y:String) => x ++ getSchedulePoints(y, fieldType))
      }else {
       val parts = expr.split(DASH)
       if (expr.contains(DASH) && parts.length != 2){
         throw InvalidInputException(s"Invalid inout for schedule ${fieldType.name}, range missing")
       }
       if (parts.length > 1 ){
         // expr contains dash with range
         val start = parts(0)
         val end = parts(1)
         if (end.contains(SLASH)) {
           val schedulePoints = Range(start.toInt , end.split(SLASH)(0).toInt + 1 ,  end.split(SLASH)(1).toInt)
           if (schedulePoints.isEmpty) throw InvalidInputException(s"Invalid inout for schedule ${fieldType.name}, range missing")
           schedulePoints.toList
         }else {
           val schedulePoints = start.toInt to end.toInt
           if (schedulePoints.isEmpty) throw InvalidInputException(s"Invalid inout for schedule ${fieldType.name}, range missing")
           schedulePoints.toList
         }
       } else {
         if (expr.split(SLASH).length == 1) throw InvalidInputException(s"Invalid inout for schedule ${fieldType.name}, period missing")
          Range(fieldType.startRange, fieldType.endRange + 1, expr.split(SLASH)(1).toInt).toList
       }
      }
    }
  }
}
