api
===============

Movie reservation servie API.
Built with spray-router running on spray-can -- http://spray.io, Akka, Slick, Postgres
Project maintainer: ramsinha

REQUIREMENTS:
=========

install postgres

BUILDING:
=========

from project root:


$ mvn clean package

CREATE TABLE:
=========
java -cp $jarName com.veon.ticket.service.core.api.dao.DAOSlick 

<For simplicity postgres should have a database running by name "postgres" at localhost  without usrname and password restriction>
above command will create the required tables.

RUNNING:
=======

java -cp $jarname com.veon.ticket.service.core.api.ReservationServiceMain


DOCUMENTATION:
=======

API:

Health Check
Request Type: GET
http://localhost:8080/ticketreservation/v1


Register a Movie
Request Type: POST
http://localhost:8080/ticketreservation/v1/registerMovie

{
	"imdbId" : "1",
	"screenId" : "3",
	"availlableSeats": 100
}


Make Reservation:
Request Type: POST
http://localhost:8080/ticketreservation/v1/makeReservation
{
	"imdbId" : "1",
	"screenId" : "3"
}

Get Availability:
Request Type: GET
http://localhost:8080/ticketreservation/v1/getAvailability?imdbId=1&screenId=3


