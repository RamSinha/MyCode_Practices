package Uitls

import Exceptions.FairCalculationStrategyNotFound
import model._

trait FairCalculationStrategy {
  def calculateFair[T <: Itinerary](itinerary: T): Float
}


object FairCalculationStrategyBuilder {
  def createStrategy(paymentMode: PaymentMode): FairCalculationStrategy = {
    paymentMode match {
      case _: OysterCard => new OysterCardPaymentStrategy
      case _ => throw new FairCalculationStrategyNotFound(
        s"No strategy found to calculate fair for mode: ${paymentMode.displayName}"
      )
    }
  }
}


class OysterCardPaymentStrategy extends FairCalculationStrategy {


  sealed trait ZoneCondition

  object SourceDestinationInZoneOne extends ZoneCondition

  object SourceAndDestinationOutSideZoneOne extends ZoneCondition

  object OneOfSourceOrDestinationInZoneOneOtherInZoneTwo extends ZoneCondition

  object OneOfSourceOrDestinationInZoneOneOtherInZoneThree extends ZoneCondition

  final val ANYWHERE_IN_ZONE_ONE_FAIR: Float = 2.5f
  final val ANY_ZONE_OUTSIDE_ZONE_ONE_FAIR: Float = 2.0f
  final val ANY_TWO_ZONE_INCLUDING_ZONE_ONE_FAIR: Float = 3.0f
  final val ANY_TWO_ZONE_EXCLUDING_ZONE_ONE_FAIR: Float = 2.25f
  final val ANY_THREE_ZONE_FAIR: Float = 3.20f
  final val BUS_FAIR: Float = 1.8f

  def calculateFair[T <: Itinerary](itinerary: T): Float = {
    val fair = itinerary.travelMode match {
      case _: Bus.type => BUS_FAIR
      case _: Tube.type => findZoneConditions(itinerary)
    }
    fair
  }

  private def findZoneConditions(itinerary: Itinerary): Float = {

    val allTravelledZones = (
      itinerary.startStation.zones ++ itinerary.endStation.zones
      ).map(_.name)

    val startZones = itinerary.startStation.zones.map(_.name)
    val endZones = itinerary.endStation.zones.map(_.name)

    allTravelledZones
      .filter(
        _.equalsIgnoreCase("zone1")
      ).size match {
      case 2 => ANYWHERE_IN_ZONE_ONE_FAIR
      case 1 if startZones.contains("zone2") && endZones.contains("zone2") => ANY_ZONE_OUTSIDE_ZONE_ONE_FAIR
      case 1 if startZones.contains("zone3") && endZones.contains("zone3") => ANY_ZONE_OUTSIDE_ZONE_ONE_FAIR
      case 1 => ANY_TWO_ZONE_INCLUDING_ZONE_ONE_FAIR
      case 0 if allTravelledZones.toSet[String].size == 1 => ANY_ZONE_OUTSIDE_ZONE_ONE_FAIR
      case 0 => ANY_TWO_ZONE_EXCLUDING_ZONE_ONE_FAIR
    }
  }
}