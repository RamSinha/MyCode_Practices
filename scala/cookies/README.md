## SBT

* **Dependencies**
```scala
scala: 2.11.8
sbt: 1.3.13
jre: 1.8
```

* **How to build**
```scala
sbt assembly
```

* **How to run**
```scala
sbt "run --help"
```

* **Execute with custom options**
```scala
sbt "run -f <dataFileCSV> -d <date/utc>"
example: sbt "run -f cookie_log.csv -d 2018-12-09"
```

* **Run test**
```scala
sbt test 
```


* **Customization**
-- Please run `sbt "run --help"` to available customization
*   -d, --day  <arg>      Value of day to calculate top cookies, ex: "2018-12-09" // mandatory 
*   -e, --engine  <arg>   Execution env to calculate top cookies // not mandatory default Local
*   -f, --file  <arg>     Log file path to read cookies information // mandatory 

     
