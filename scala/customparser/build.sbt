name := "csvparser"
organization := "com.dot.parsers"
version := "0.1"
scalaVersion := "2.11.8"
val sparkVersion = "2.4.0"
val scallopVersion = "3.3.2"
val scalaTestVersion = "3.0.1"

libraryDependencies ++= Seq(
  "org.apache.spark" %% "spark-sql" % sparkVersion,
  "org.apache.spark" %% "spark-core" % sparkVersion,
  "org.rogach" %% "scallop" % scallopVersion,
  "com.typesafe" % "config" % "1.3.1",
  "org.scalatest" %% "scalatest" % scalaTestVersion % "test"
)

assemblyJarName in assembly := "customParser.jar"

mainClass in (Compile, packageBin) := Some("com.parsers.Runner")

assemblyMergeStrategy in assembly := {
  case PathList("org", "aopalliance", xs@_*) => MergeStrategy.last
  case PathList("javax", "inject", xs@_*) => MergeStrategy.last
  case PathList("javax", "servlet", xs@_*) => MergeStrategy.last
  case PathList("javax", "activation", xs@_*) => MergeStrategy.last
  case PathList("org", "apache", xs@_*) => MergeStrategy.last
  case PathList("com", "google", xs@_*) => MergeStrategy.last
  case PathList("com", "esotericsoftware", xs@_*) => MergeStrategy.last
  case PathList("com", "codahale", xs@_*) => MergeStrategy.last
  case PathList("com", "yammer", xs@_*) => MergeStrategy.last
  case PathList("META-INF", "pom.xml") => MergeStrategy.last

  case PathList("net", "jpountz", _*) => MergeStrategy.last
  case x if x.startsWith("META-INF") => MergeStrategy.discard
  case "git.properties" => MergeStrategy.last
  case PathList("mime.types") => MergeStrategy.last
  case "plugin.properties" => MergeStrategy.last
  case "log4j.properties" => MergeStrategy.last
  case x =>
    val oldStrategy = (assemblyMergeStrategy in assembly).value
    oldStrategy(x)
}