This repository contains code examples of Kafka consumer's, producer's using Scala
This repository contains code examples of micro-service development using Akka-http, Slick
This repository contains code examples of monitoring using grafa

## Building the reposiory

    sbt assembly
    
## Spin up container

docker-compose -f docker-compose.yml up -d

## Running Examples

### Producer

java -cp target/scala-2.11/ScalaKafkaExamples-assembly-1.0.jar com.careem.kafka.examples.MTProducer 

java -cp target/scala-2.11/ScalaKafkaExamples-assembly-1.0.jar com.careem.kafka.examples.MDConsumer


### Consumer
java -cp target/scala-2.11/ScalaKafkaExamples-assembly-1.0.jar com.careem.kafka.examples.MTConsumer

java -cp target/scala-2.11/ScalaKafkaExamples-assembly-1.0.jar com.careem.kafka.examples.MDConsumer

### Monitor Kafka using Kafka Manager

http://localhost:9000/clusters

### Login to Postgres

psql --host=127.0.0.1 --username="grafana"  --dbname=postgres

password -> grafana

### Create tables

java -cp target/scala-2.11/ScalaKafkaExamples-assembly-1.0.jar com.careem.kafka.examples.api.repository.CreateTableScript

### Drop tables

java -cp target/scala-2.11/ScalaKafkaExamples-assembly-1.0.jar com.careem.kafka.examples.api.repository.DropTableScript

### API

Boot Akka-HTTPService

java -cp target/scala-2.11/ScalaKafkaExamples-assembly-1.0.jar com.careem.kafka.examples.api.service.Boot

Get instant supply/demand ratio http://localhost:8899/metrics/v1/ratio?at=<UTC timestamp>

Get historical supply/demand ratio http://localhost:8899/metrics/v1/historicalRatio?from=<UTC timestamp>&to=<UTC timestamp>

### Grafana

1. Create dashboard
2. Add panel for table data. Grafana query are place in grafana-sql folder
