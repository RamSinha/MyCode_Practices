package com.qc.execution.impl

import com.qc.config.UserConfig
import com.qc.dao.CookieRecord
import com.qc.execution.ExecutionEngine
import com.typesafe.config.Config

import scala.collection.mutable

/**
 * @author ram.sinha on 8/27/21
 */
class LocalEngine(userConfig: UserConfig, appConfig: Config) extends ExecutionEngine{
  val inMemoryMap = new mutable.HashMap[CookieRecord, Int]()
  val maxHeap = new mutable.PriorityQueue[CookieRecord]()(Ordering.by[CookieRecord, Int](inMemoryMap))
  override def accept(input: CookieRecord): Unit = {
    val currentFreq = inMemoryMap.getOrElse(input, 0)
    inMemoryMap.update(input, currentFreq + 1 )
  }
  override def topResult(): List[CookieRecord] = {
    inMemoryMap.collect({
      case (k,_) => {
        if (maxHeap.isEmpty) {
          maxHeap.enqueue(k)
        }else {
          val head = maxHeap.head
          if (inMemoryMap(head) == inMemoryMap(k)){
            maxHeap.enqueue(k)
          }else if (inMemoryMap(head) > inMemoryMap(k)){
            // ignore this record
          }else {
            maxHeap.dequeue()
            maxHeap.enqueue(k)
          }
        }
      }
    })
    maxHeap.toList
  }
}
