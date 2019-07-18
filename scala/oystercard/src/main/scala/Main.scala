import Uitls.{ApplicationConstants, FairCalculationStrategyBuilder}
import model._

object Main extends App {

  val oysterCard = OysterCard(30)

  val holBorn = Station("Holborn", List(Zone1))
  val earlsCourt = Station("Earl’s Court", List(Zone1, Zone2))
  val wimbledon = Station("Wimbledon", List(Zone3))
  val hammerSmith = Station("Hammersmith", List(Zone2))
  val chelsea = Station("Chelsea", Nil)

  val holBronToEarlsCourt = Itinerary(holBorn, earlsCourt, Tube, oysterCard)
  val fairI1 = FairCalculationStrategyBuilder.createStrategy(oysterCard).calculateFair(holBronToEarlsCourt)
  println(fairI1)
  oysterCard.debitBalance(fairI1)
  holBronToEarlsCourt.completeItinerary()

  val earlsCourtToChelsea = Itinerary(earlsCourt, chelsea, Bus, oysterCard)
  val fairI2 = FairCalculationStrategyBuilder.createStrategy(oysterCard).calculateFair(earlsCourtToChelsea)
  println(fairI2)
  oysterCard.debitBalance(fairI2)
  earlsCourtToChelsea.completeItinerary()


  val earlsCourtToHammerSmith = Itinerary(earlsCourt, hammerSmith, Tube, oysterCard)
  val fairI3 = FairCalculationStrategyBuilder.createStrategy(oysterCard).calculateFair(earlsCourtToHammerSmith)
  println(fairI3)
  oysterCard.debitBalance(fairI3)
  earlsCourtToHammerSmith.completeItinerary()


  println(s"Remaining balance is ${oysterCard.getCurrentBalance()}")
}