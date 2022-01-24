package co.thebeat.bigdata.takehomeassignment.model

import java.sql.Timestamp

/**
 * Represents an event which has been mapped to a zone based on its latitude and longitude.
 * @param driver the unique identifier of each driver
 * @param timestamp the event creation time
 * @param latitude the latitude geographic coordinate as received from GPS sensors
 * @param longitude the longitude geographic coordinate as received from GPS sensors
 * @param id_zone the ID of the zone that corresponds to the event's latitude and longitude
 */
case class EventWithZone(
  driver: String,
  timestamp: Timestamp,
  latitude: Double,
  longitude: Double,
  id_zone: Long
)
