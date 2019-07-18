package Exceptions

final case class NotEnoughBalanceException(val message: String,
                                           val cause: Throwable = None.orNull)
  extends Exception(message, cause)


final case class FairCalculationStrategyNotFound(val message: String,
                                           val cause: Throwable = None.orNull)
  extends Exception(message, cause)
