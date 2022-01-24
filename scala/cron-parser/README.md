## SBT

* **Dependencies**
```scala
scala: 2.11.8
sbt: 1.3.8
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
sbt "run --expr cron-expr-with-command"
example: sbt "run --expr */15 0 1,15 * 1-7 /usr/bin/find"
output: 
    minute        : 0 15 30 45
    hour          : 0
    day_of_month  : 1 15
    month         : 1 2 3 4 5 6 7 8 9 10 11 12
    day_of_week   : 1 2 3 4 5 6 7
    command       : /usr/bin/find
```

* **Run test**
```scala
sbt test 
``` 

     
