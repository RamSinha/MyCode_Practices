package com.qc.dataloader

import com.qc.config.UserConfig
import com.qc.dataloader.impl.FileBasedDataLoaderWithDataFilter
import com.qc.exception.InvalidConfigException
import com.typesafe.config.Config

/**
 * @author ram.sinha on 8/27/21
 */
object DataLoaderFactory {
  def getDataLoader(userConfig: UserConfig, appConfig: Config): DataLoader = {
    userConfig.file.toOption match {
      case Some(_) => FileBasedDataLoaderWithDataFilter(userConfig)
      case None => throw InvalidConfigException("Undefined Data Loader")
    }
  }
}
