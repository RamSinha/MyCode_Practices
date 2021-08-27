
name := "cookies"

version := "0.1"

scalaVersion := "2.11.8"

val scallopVersion = "3.3.2"
val scalaTestVersion = "3.0.1"

libraryDependencies ++= Seq(
  "org.rogach" %% "scallop" % scallopVersion,
  "com.typesafe" % "config" % "1.3.1",
  "joda-time" % "joda-time" % "2.10",
  "org.scalatest" %% "scalatest" % scalaTestVersion % "test"
)


assemblyJarName in assembly := "topCookie.jar"

mainClass in (Compile, packageBin) := Some("com.qc.driver.CookieApp")
