package model

import Uitls.ApplicationConstants

case class Itinerary(startStation: Station,
                     endStation: Station,
                     travelMode: TravelMode,
                     paymentMode: PaymentMode){
  assert(paymentMode.getCurrentBalance >= ApplicationConstants.MAX_FAIR, "Insufficient balance")
  paymentMode.debitBalance(ApplicationConstants.MAX_FAIR)


  def completeItinerary(): Unit = {
    paymentMode.creditBalance(ApplicationConstants.MAX_FAIR)
    println(s"Completed journey from $startStation to $endStation via $travelMode")
  }
}
