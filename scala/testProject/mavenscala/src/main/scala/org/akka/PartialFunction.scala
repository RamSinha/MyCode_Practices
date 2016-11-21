package org.akka

/**
  * Created by ramsinha on 30/09/16.
  */
object PartialFunction {

  val fraction = new PartialFunction[Int, Int] {
    def apply(d: Int) = 42 / d

    def isDefinedAt(d: Int) = d != 0
  }

  val fractinWithCase: PartialFunction[Int, Int] = {
    case x: Int if x != 0 => 42 / x
  }
}


// Both Fration and FrationWithCase are same wrt behaviour.