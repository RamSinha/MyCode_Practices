package model

sealed trait Zone {
  val name: String
  override def toString: String = name
}

object Zone1 extends Zone {
  override val name: String = "zone1"
}

object Zone2 extends Zone {
  override val name: String = "zone2"
}

object Zone3 extends Zone {
  override val name: String = "zone3"
}

object ZoneNotDefined extends Zone {
  override val name: String = "Zone not defined"
}