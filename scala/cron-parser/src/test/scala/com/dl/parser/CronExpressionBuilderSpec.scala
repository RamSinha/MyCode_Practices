package com.dl.parser

import com.dl.exception.InvalidInputException
import com.dl.model.{Field, FieldDefinition}
import org.scalatest.{FlatSpec, Matchers}

/**
 * @author ram.sinha on 1/24/22
 */
class CronExpressionBuilderSpec extends FlatSpec with Matchers{
"CronExpressionBuilder" should "successfully parser input cron with command" in {
  val fds = CronExpressionBuilder.create().createFieldDefinition("*/15 0 1,15 * 1-7 /usr/bin/find")
  fds.sortBy(_.scheduleType.order).head.toString shouldBe "minute        : 0 15 30 45"
}
}
