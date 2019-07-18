package model

import Exceptions.NotEnoughBalanceException
import Uitls.ApplicationConstants

trait PaymentMode {
  val displayName: String

  def getCurrentBalance: Float

  def setNewBalance(newBalance: Float): Unit

  def creditBalance(creditValue: Float): Unit

  def debitBalance(debitValue: Float): Unit
}

case class OysterCard(currentBalance: Float) extends PaymentMode {

  override val displayName: String = ApplicationConstants.OYSTER_CARD_NAME

  private[this] var availBalance = currentBalance

  def getCurrentBalance() = availBalance

  def setNewBalance(newBalance: Float) = availBalance = newBalance

  def creditBalance(creditValue: Float) = {
    availBalance = availBalance + creditValue
  }

  def debitBalance(debitValue: Float): Unit = {
    assert(availBalance >= debitValue, throw new NotEnoughBalanceException("Not enough Balance available."))
    availBalance = availBalance - debitValue
  }
}
