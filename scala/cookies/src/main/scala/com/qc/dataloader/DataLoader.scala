package com.qc.dataloader

import com.qc.dao.CookieRecord

/**
 * @author ram.sinha on 8/27/21
 */
trait DataLoader {
  def loadData(): Iterator[CookieRecord]
}
