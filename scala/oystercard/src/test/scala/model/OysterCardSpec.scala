package model

import Exceptions.NotEnoughBalanceException
import org.scalatest.{BeforeAndAfterAll, Matchers, WordSpec}

class OysterCardSpec extends WordSpec with Matchers with BeforeAndAfterAll {
  "Oyster card" should {

    val card = OysterCard(30)
    "Have balance of 30 on recharge" in {
      card.getCurrentBalance() shouldBe 30.0f
    }

    "Have balance of 3.0 on deduction of 27.0" in {
      card.debitBalance(27.0f)
      card.getCurrentBalance() shouldBe 3.0f
    }

    "Throw exception on deduction when balance is low" in {
      assertThrows[NotEnoughBalanceException] {
        card.debitBalance(30.0f)
      }
    }
  }
}
