name := "cron-parser"

version := "0.1"

scalaVersion := "2.11.8"


val scallopVersion = "3.3.2"
val scalaTestVersion = "3.0.1"

libraryDependencies ++= Seq(
  "org.rogach" %% "scallop" % scallopVersion,
  "com.typesafe" % "config" % "1.3.1",
  "org.scalatest" %% "scalatest" % scalaTestVersion % "test"
)

assemblyJarName in assembly := "cron-parser.jar"
mainClass in (Compile, packageBin) := Some("com.dl.driver.CronParserApp")
