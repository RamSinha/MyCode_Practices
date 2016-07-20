git clone https://github.com/RamSinha/MyCode_Practices.git  
cd MyCode_Practices/scala/testProject/mavenscala  
mvn clean install  
scala -cp target/mavenscala-1.0-SNAPSHOT-jar-with-dependencies.jar  org.processors.FileDownloaderDriver <localDirectoryPath> file_1 file_2 file_3   
