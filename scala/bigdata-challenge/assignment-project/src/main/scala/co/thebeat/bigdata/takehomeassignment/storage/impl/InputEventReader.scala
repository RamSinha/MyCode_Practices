package co.thebeat.bigdata.takehomeassignment.storage.impl

import co.thebeat.bigdata.takehomeassignment.model.InputEvent
import co.thebeat.bigdata.takehomeassignment.storage.Reader
import org.apache.spark.sql.catalyst.util.DropMalformedMode
import org.apache.spark.sql.{Dataset, SparkSession}

import scala.util.Try


/**
 * @author ram.sinha on 9/1/21
 */
class DataSetReader (implicit sparkSession: SparkSession) extends Reader[InputEvent] {
  override def read(path: String): Try[Dataset[InputEvent]] = Try {
    import sparkSession.implicits._
    sparkSession
      .read
      .option( "header", true )
      .option( "mode", DropMalformedMode.name ).csv().as[String].flatMap( InputEvent( _ ) )
  }
}
