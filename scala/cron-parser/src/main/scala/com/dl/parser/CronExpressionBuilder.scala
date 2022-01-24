package com.dl.parser

import com.dl.model.{Field, FieldDefinition}

/**
 * @author ram.sinha on 1/23/22
 */
class CronExpressionBuilder private {
  val SPACE: String = " "

  /**
   * Method takes the raw string input and creates a cron expression
   * @param expression Input expression
   * @return List of field definition object
   */
  def createFieldDefinition(expression: String): List[FieldDefinition] = {
    val parts = expression.split(SPACE).zipWithIndex.map(t => (t._2 -> t._1)).toMap
    val v = Field.values.map(x => x.order -> x).toMap
    parts.map(p => CronFieldParser.parserField(p._2, v(p._1))).toList
  }

  /**
   * This method print the final outout with padded columns, the list is also sorted based on the cron expression order
   * @param fds FieldDefinition object per input field
   */
  def printFormatted(fds: List[FieldDefinition]): Unit ={
    println(fds.sortBy(_.scheduleType.order).mkString("\n"))
  }
}

/**
 * Factory method to create CronExpressionBuilder
 */
object CronExpressionBuilder {
  def create(): CronExpressionBuilder = {
    new CronExpressionBuilder()
  }
}
