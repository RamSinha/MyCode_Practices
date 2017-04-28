api
===============

Movie reservation servie API.
Built with spray-router running on spray-can -- http://spray.io, Akka, Slick, Postgres
Project maintainer: ramsinha

DOCUMENTATION:
=============

REQUIREMENTS:
=========

install postgres

BUILDING:
=========

from project root:


$ mvn clean package

CREATE TABLE:
=========
java -cp <jarName> com.veon.ticket.service.core.api.dao.DAOSlick 

<For simplicity postgres should have a database running by name "postgres" at localhost  without usrname and password restriction>
above command will create the required tables.

RUNNING:
=======

java -cp <jarname> com.veon.ticket.service.core.api.ReservationServiceMain
