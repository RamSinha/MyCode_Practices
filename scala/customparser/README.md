## SBT

* **How to build**
```scala
sbt assembly
```

* **How to run**
```scala
sbt "run --help"
```

* **Execute for give paths**
```scala
sbt "run --files <path1> <path2>"
```

* **Run test**
```scala
sbt test
example: sbt "run --files /Users/ramsinha/Downloads/test1.csv /Users/ramsinha/Downloads/test.csv --top 2" 
```


* **Customization**
-- Please run "sbt run --help" to available customization
* **--quote**: To set custom quote 
* **--delim**: To set custom delim 
* **--linesep**: To set custom linesep 
* **--header**: To set if first line is header 
* **--encoding**: To set custom encoding 
* **--top**: To display number of records 
* **--format**: "csv" to use spark-native based  
* **--format**: "custom_csv" to use custom csv parser  
* **--top**: To display number of records 


Note: 
    Custom parser doesn't support multiline output
    Output is list of parsed cells //TODO: There shall be custom encoder to make it spark compatible
     
