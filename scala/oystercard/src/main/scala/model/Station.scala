package model

case class Station(name: String, zones: List[Zone]) {
  override def toString: String = s"$name in {${zones.mkString("/")}}"
}