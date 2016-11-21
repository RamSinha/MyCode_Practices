package org.akka

/**
  * Created by ramsinha on 27/09/16.
  */
object Solution_3 {
  def main(args: Array[String]) {
    import java.io.{BufferedReader, InputStreamReader}

    val reader: BufferedReader = new BufferedReader(new InputStreamReader(System.in))

    val target = reader.readLine().toInt
    val numberOfValues = reader.readLine().toInt

    val numbers = scala.collection.mutable.Map[Int, Int]()
    val numList = scala.collection.mutable.ArrayBuffer[Int]()
    for (i <- 0 until numberOfValues) {
      val value = reader.readLine().toInt

      if (numbers.contains(value)) {
        numbers(value) = 2
      } else {
        numbers += value -> 1
      }

      numList += value
    }
    var notification = true
    for (i <- numList) {
      if (notification) {
        val find = target - i
        if (numbers.contains(find)) {
          if (find == i) {
            if (numbers.get(find).get > 1) {
              println(1)
              notification = false
            }
          } else {
            if (numbers.contains(find)) {
              println(1)
              notification = false
            }
          }
        }
      }
    }
  }
}
