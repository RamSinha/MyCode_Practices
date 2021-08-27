package com.qc.execution

import com.qc.config.{ExecutionEngineType, UserConfig}
import com.qc.exception.InvalidConfigException
import com.qc.execution.impl.LocalEngine
import com.typesafe.config.Config

/**
 * @author ram.sinha on 8/27/21
 */
object ExecutionEngineFactory {
  def createExecutionEngine(useConfig : UserConfig, appConfig: Config): ExecutionEngine = {
    useConfig.engine() match {
      case ExecutionEngineType.LOCAL => new LocalEngine(useConfig, appConfig)
      case _ => throw InvalidConfigException(s"Invalid engine config allowed values: ${ExecutionEngineType.values.mkString(" | ")}")
    }
  }
}
