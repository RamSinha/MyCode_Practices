package samples

import org.junit._
import Assert._
import org.processors.FileDownloaderDriver
import java.io.File

@Test
class AppTest {

  @Test
  def testOK() = assertTrue(true)

  @Test
  def downloadOK(): Unit = {
    val args = Array[String]("/Users/ramsinha/Downloads/processedFiles", "http://google.co.in:80/index.html")
    FileDownloaderDriver.main(args)

    /*
    File should be downloaded at
    /Users/ramsinha/Downloads/processedFiles/index_1.html
    /Users/ramsinha/Downloads/processedFiles/index.html
     */

    assert (new File("/Users/ramsinha/Downloads/processedFiles/index.html").exists() == true )

  }


}


