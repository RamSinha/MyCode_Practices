package model

sealed trait TravelMode {
  val name : String

  override def toString: String = name
}

object Tube extends TravelMode {
  val name = "Tube"
}
object Bus extends TravelMode {
  val name = "Bus"
}
