name := "ScalaKafkaExamples"

version := "1.0"

scalaVersion := "2.11.8"
val sparkVersion = "2.1.0"
val sparkRedshiftVersion = "3.0.0-preview1"
val sparkAvroVersion = "3.2.0"

enablePlugins(UniversalPlugin)
libraryDependencies ++= Seq(
  "org.apache.kafka" %% "kafka" % "1.1.0",
  "org.apache.kafka" % "kafka-clients" % "1.1.0",
  "org.apache.spark" %% "spark-core" % sparkVersion,
  "org.apache.spark" %% "spark-hive" % sparkVersion,
  "org.apache.spark" %% "spark-sql" % sparkVersion,
  "com.databricks" %% "spark-redshift" % sparkRedshiftVersion,
  "com.databricks" %% "spark-avro" % sparkAvroVersion,
  "org.apache.spark" % "spark-mllib_2.11" % sparkVersion
)
libraryDependencies += "org.apache.spark" %% "spark-yarn" % sparkVersion
// https://mvnrepository.com/artifact/com.typesafe/config
libraryDependencies += "com.typesafe" % "config" % "1.2.1"
// https://mvnrepository.com/artifact/joda-time/joda-time
libraryDependencies += "joda-time" % "joda-time" % "2.8.1"

autoCompilerPlugins := true

addCompilerPlugin(
  "org.scala-lang.plugins" % "scala-continuations-plugin_2.11.6" % "1.0.2")

libraryDependencies +=
  "org.scala-lang.plugins" %% "scala-continuations-library" % "1.0.2"

// https://mvnrepository.com/artifact/org.typelevel/cats-core
libraryDependencies += "org.typelevel" %% "cats-core" % "1.2.0"
libraryDependencies += "com.typesafe.akka" %% "akka-actor" % "2.4.10"
libraryDependencies += "com.typesafe.akka" %% "akka-http-experimental" % "2.4.10"
libraryDependencies += "com.typesafe.akka" %% "akka-http-spray-json-experimental" % "2.4.10"
libraryDependencies += "com.github.tototoshi" %% "scala-csv" % "1.3.5"
// https://mvnrepository.com/artifact/org.apache.kafka/kafka-streams
libraryDependencies += "org.apache.kafka" % "kafka-streams" % "1.0.2"
libraryDependencies += "com.typesafe.slick" %% "slick" % "3.2.1"
libraryDependencies += "com.typesafe.slick" %% "slick-hikaricp" % "3.2.1"
libraryDependencies += "com.typesafe.slick" %% "slick-codegen" % "3.2.1"
libraryDependencies += "org.postgresql" % "postgresql" % "42.0.0"
libraryDependencies += "org.apache.spark" %% "spark-streaming" % sparkVersion 
libraryDependencies += "org.apache.spark" % "spark-streaming-kafka-0-10_2.11" % sparkVersion
libraryDependencies += "org.apache.spark" %% "spark-sql-kafka-0-10" % sparkVersion
libraryDependencies += "com.fasterxml.jackson.module" %% "jackson-module-scala" % "2.9.6"
libraryDependencies += "za.co.absa" %% "abris" % "2.2.2"


libraryDependencies += "org.apache.avro" % "avro" % "1.8.1"
libraryDependencies += "io.confluent" % "kafka-avro-serializer" % "3.2.1"


resolvers ++= Seq(
  "confluent" at "http://packages.confluent.io/maven",
  "ossrh" at "https://oss.sonatype.org/service/local/staging/deploy/maven2/"
)
scalacOptions += "-P:continuations:enable"

mappings in Universal := {
  val universalMappings = (mappings in Universal).value
  val fatJar = (assembly in Compile).value
  val filtered = universalMappings filter {
    case (_, nm) =>  ! nm.endsWith(".jar")
  }
  filtered ++ Seq(
    fatJar -> fatJar.getName
  )
}
