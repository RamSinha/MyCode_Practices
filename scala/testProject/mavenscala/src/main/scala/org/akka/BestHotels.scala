package org.akka

/**
  * Created by ramsinha on 15/11/16.
  */
object BestHotels {

  def main(args: Array[String]) {

    import java.io.{BufferedReader, InputStreamReader}
    val reader: BufferedReader = new BufferedReader(new InputStreamReader(System.in))
    val numberOfInput = reader.readLine().toInt
    val hotels_score = scala.collection.mutable.Map[Int, Int]()
    val hotels_freq = scala.collection.mutable.Map[Int, Int]()

    for (i <- 0 until numberOfInput) {
      val record = reader.readLine().split(" ")
      val hotel_id = record(0).toInt
      val hotel_score = record(1).toInt
      if (hotels_score.contains(hotel_id)) {

        hotels_score += hotel_id -> ((hotels_score.get(hotel_id).get.toInt + hotel_score)/hotels_freq.getOrElse(hotel_id, 1))
      } else {
        hotels_score += hotel_id -> hotel_score
      }
    }
    val result = hotels_score.toSeq.sortBy(_._2)
    var last = -1
    for (i <- (result.length - 1) to 0 by -1) {
      println(result(i)._1)
    }
  }

  def best_hotels() = {
    import java.io.{BufferedReader, InputStreamReader}
    val reader: BufferedReader = new BufferedReader(new InputStreamReader(System.in))
    val numberOfInput = reader.readLine().toInt
    val hotels_score = scala.collection.mutable.Map[Int, Int]()
    val hotels_freq = scala.collection.mutable.Map[Int, Int]()

    for (i <- 0 until numberOfInput) {
      val record = reader.readLine().split(" ")
      val hotel_id = record(0).toInt
      val hotel_score = record(1).toInt
      hotels_freq += hotel_id -> (hotels_freq.getOrElse(hotel_id, 0) + 1 )
      if (hotels_score.contains(hotel_id)) {
        hotels_score += hotel_id -> ((hotels_score.get(hotel_id).get.toInt + hotel_score)/hotels_freq.getOrElse(hotel_id, 1))
      } else {
        hotels_score += hotel_id -> hotel_score
      }
    }
    val result_1 = hotels_score.toSeq.sortBy(_._2).toList
    val result = scala.collection.mutable.ArrayBuffer(result_1:_*)



    for (i <- (result.length - 1) to 0 by -1) {
      if (i < result.length - 1 ){
        val cur = result(i)
        val next = result(i + 1)
        if (cur._2 == next._2 && cur._1 < next._1){
          println(result(i)._1)
        }else{
          println(result(i+1)._1)
          result(i+1) = cur
        }
      }else{
        println(result(i)._1)
      }

    }
  }
}
