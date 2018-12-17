package com.careem.kafka.examples.api.service.responseformat

import spray.json.{DefaultJsonProtocol, JsObject, JsString, JsValue, RootJsonFormat}


object ResponseProtocol extends DefaultJsonProtocol {

  case class Ratio(at: String, value: String)
  case class HistoricalRatio(from: String, to: String, value: String)

  implicit object MetricsDataJsonFormat extends RootJsonFormat[Ratio] {
    def write(entry: Ratio) = JsObject(Map(
      "at" -> JsString(entry.at),
      "value" -> JsString(entry.value)
    ))

    def read(value: JsValue): Ratio = ???
  }

  implicit object MetricsHistoricalDataJsonFormat extends RootJsonFormat[HistoricalRatio] {
    def write(entry: HistoricalRatio) = JsObject(Map(
      "from" -> JsString(entry.from),
      "to" -> JsString(entry.to),
      "value" -> JsString(entry.value)
    ))

    def read(value: JsValue): HistoricalRatio = ???
  }
}