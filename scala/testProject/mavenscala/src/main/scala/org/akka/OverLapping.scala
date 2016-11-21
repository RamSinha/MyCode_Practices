package org.akka

/**
  * Created by ramsinha on 15/11/16.
  */
object OverLapping {
  def main(args: Array[String]) {
    import java.io.{BufferedReader, InputStreamReader}
    val reader: BufferedReader = new BufferedReader(new InputStreamReader(System.in))
    val records = scala.collection.mutable.Map[Int, Int]()
    val numberOfEntry = reader.readLine().toInt
    for (i <- 0 until numberOfEntry ){
        val pair = reader.readLine().split(" ")
        records += pair(0).toInt -> pair(1).toInt
    }

    val sortedRecord = scala.collection.mutable.ArrayBuffer(records.toSeq.sortBy(_._1):_*)




    var pointer = 1


    for (i <- 1 until sortedRecord.length ){
      val cur = sortedRecord(pointer)
      val prev = sortedRecord(pointer - 1)

      if(i < sortedRecord.length && cur._1 <= prev._2){
        sortedRecord(i-1) = (prev._1, cur._2)
        sortedRecord.remove(i)
      }else{
        pointer += 1
      }
    }

    println(sortedRecord.length)
    for (i <- 0 until sortedRecord.length ){
      val record = sortedRecord(i)
      println(record._1 + " " + record._2)
    }

  }
}
