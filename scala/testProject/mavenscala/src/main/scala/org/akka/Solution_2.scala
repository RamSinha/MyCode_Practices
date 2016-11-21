package org.akka

import java.io.{BufferedReader, InputStreamReader}

/**
  * Created by ramsinha on 27/09/16.
  */
object Solution_2 {
  def main(args: Array[String]) {
    import java.io.{BufferedReader, InputStreamReader}
    val reader: BufferedReader = new BufferedReader(new InputStreamReader(System.in))
    val keys = reader.readLine().split(" ")
    val hotel_review = scala.collection.mutable.Map[Int, Int]()
    val numberOfHotel = reader.readLine().toInt
    val default_score = 0

    for (i <- 0 until numberOfHotel) {
      val hotel_id = reader.readLine().toInt
      val review = reader.readLine()
      var score = default_score
      for (k <- keys) {
        if (review.contains(k)) {
          score += 1
        }
      }
      if (hotel_review.contains(hotel_id)) {
        val prev_score: Int = hotel_review.get(hotel_id).get
        var new_score = prev_score + score
        hotel_review += hotel_id -> new_score
      }
      hotel_review += hotel_id -> score
    }

    hotel_review.toSeq.sortBy(_._2)
    for (k <- hotel_review) {
      print(k._1 + " ")
    }
  }
}
