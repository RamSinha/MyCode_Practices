package com.dl.driver

import com.dl.parser.CronExpressionBuilder
import com.dl.config.UserConfig

/**
 * @author ram.sinha on 1/23/22
 */
object CronParserApp extends App {
  val expression = UserConfig(args).expr()
  val builder = CronExpressionBuilder.create()
  val fds = builder.createFieldDefinition(expression)
  builder.printFormatted(fds)
}
