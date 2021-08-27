package com.qc.execution

import com.qc.dao.CookieRecord

/**
 * @author ram.sinha on 8/27/21
 */
trait ExecutionEngine {
  def accept(input: CookieRecord): Unit
  def topResult(): List[CookieRecord]
}
