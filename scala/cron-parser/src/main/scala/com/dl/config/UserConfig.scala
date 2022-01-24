package com.qc.config

import org.rogach.scallop.{ScallopConf, ScallopOption, singleArgConverter}

/**
 * @author ram.sinha on 1/23/22
 */


case class UserConfig(userArgs: Array[String]) extends ScallopConf(userArgs){
  val expr: ScallopOption[String] = opt[String]("expr", descr = "cron expression with command to execute, ex: \"*/15 0 1,15 * 1-5 /usr/bin/find\"", required = true, short = 'i')
  verify()
}
