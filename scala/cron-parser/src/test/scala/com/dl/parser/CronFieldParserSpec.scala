package com.dl.parser

import com.dl.exception.{InvalidInputException, OutOfRangeException}
import com.dl.model.{Field, FieldDefinition}
import org.scalatest.{FlatSpec, Matchers}


/**
 * @author ram.sinha on 1/24/22
 */
class CronFieldParserSpec extends FlatSpec with Matchers {
  "CronFieldParser" should "correctly calculate scheduled sets from the hour field" in {
    CronFieldParser.getSchedulePoints("1-7", Field.HOUR)  shouldBe (1 to 7).toList
  }

  "CronFieldParser" should "correctly calculate scheduled sets from the minute field" in {
    CronFieldParser.getSchedulePoints("1-25", Field.MINUTE)  shouldBe (1 to 25).toList
  }

  "CronFieldParser" should "correctly calculate scheduled sets from the day_of_month field" in {
    CronFieldParser.getSchedulePoints("*", Field.DAY_OF_MONTH)  shouldBe (1 to 31).toList
  }

  "CronFieldParser" should "correctly calculate scheduled sets from the month field" in {
    println(CronFieldParser.getSchedulePoints("*", Field.MONTH))
    CronFieldParser.getSchedulePoints("*", Field.MONTH)  shouldBe  (1 to 12).toList
  }

  "CronFieldParser" should "correctly calculate scheduled sets from the day_of_week field" in {
    CronFieldParser.getSchedulePoints("1-7", Field.DAY_OF_WEEK)  shouldBe (1 to 7).toList
  }
  "CronFieldParser" should "correctly calculate scheduled sets from the hour field with period" in {
    CronFieldParser.getSchedulePoints("0-23/2", Field.HOUR)  shouldBe Range(0, 23 + 1 , 2 ).toList
  }

  "CronFieldParser" should "correctly calculate scheduled sets from the minute field with period" in {
    CronFieldParser.getSchedulePoints("*/5", Field.MINUTE)  shouldBe Range(0, 59 + 1 , 5).toList
  }

  "CronFieldParser" should "correctly calculate scheduled sets from the day_of_month field with period" in {
    CronFieldParser.getSchedulePoints("*/5", Field.DAY_OF_MONTH)  shouldBe Range(1, 31 + 1 , 5).toList
  }

  "CronFieldParser" should "correctly parse the day_of_month field with period" in {
    CronFieldParser.parserField("*/5", Field.DAY_OF_MONTH)  shouldBe FieldDefinition(Field.DAY_OF_MONTH, Range(1, 32 , 5).mkString(" "))
  }

  "CronFieldParser" should "throw exception for invalid field for the day_of_month field with period" in {
    val caught =
      intercept[InvalidInputException] {
        CronFieldParser.parserField("*/", Field.DAY_OF_MONTH)
      }
    caught.getMessage.contains("Invalid inout for schedule DAY_OF_MONTH, period missing") shouldBe true
  }

  "CronFieldParser" should "throw exception for invalid range for the day_of_week field with period" in {
    val caught =
      intercept[OutOfRangeException] {
        CronFieldParser.parserField("1-25", Field.DAY_OF_WEEK)
      }
    caught.getMessage.contains("Invalid range for schedule DAY_OF_WEEK") shouldBe true
  }
}
