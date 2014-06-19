import org.apache.oozie.client.OozieClient;
import org.apache.oozie.client.OozieClientException;

import java.util.Properties;

public class RunOozieWorkflow {
    public static void main(String[] args) {
        RunOozieWorkflow oozieWorkflow = new RunOozieWorkflow();
        oozieWorkflow.run(args);
    }

    private void run(String[] args) {
        if (args[0].contains("help") || args[0].contains("-h") || args[0].contains("?")) {
            printHelp();
            return;
        }

        OozieClient wc = new OozieClient("http://" + args[0] + ":8080/oozie");
        Properties conf = wc.createConfiguration();
        String nameNode = "hdfs://" + args[0] + ":9000/oozie/";
        conf.setProperty(OozieClient.APP_PATH, nameNode + "UrlToMdn/IndexBasedSearch");
        conf.setProperty("jsonPath", args[1]);
        //conf.setProperty("startTime", "1363000000");
        //conf.setProperty("endTime", "1388372400");
        conf.setProperty("startTime", args[2]);
        conf.setProperty("endTime", args[3]);
        conf.setProperty("nameNode", args[0] + ":9000");
        conf.setProperty("jobTracker", args[0] + ":9001");
        conf.setProperty("user.name", "root");
        conf.setProperty("reportFileName", args[4]);
        conf.setProperty("ftpUserName", "admin");
        conf.setProperty("ftpPassword", "admin@123");
        conf.setProperty("rgeMaster", args[5]);
        conf.setProperty("csvDumpBaseDir", "/data/rge");

        try {
            System.out.println("Configuration is " + conf);
            System.out.println(wc.run(conf));
        } catch (OozieClientException e) {
            e.printStackTrace();
        }
    }
    
    private void printHelp() {
        System.out.println("Argument expected: <Oozie Server IP> <URL> <StartTime> <EndTime> <ReportID> <RGE IP>");
    }
}
