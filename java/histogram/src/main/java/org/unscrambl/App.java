package org.unscrambl;


import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.List;


public class App {
    public static void main(String[] args) {
        BufferedReader br = null;
        String input = "";
        List<Interval<Double>> intervals = new ArrayList<>();
        try {
            br = new BufferedReader(new InputStreamReader(System.in));

            System.out.println("Number of Interval ");
            Integer noOfSamples = Integer.parseInt(br.readLine());

            System.out.println("Enter comma separated sample intervals ");

            for (int i = 0; i < noOfSamples; i++) {
                String[] range = br.readLine().split(",");
                Double left = Double.parseDouble(range[0]);
                Double right = Double.parseDouble(range[1]);
                intervals.add(new Interval<>(left, right));
            }


            Histogram<Double> histogram = Histogram.getInstance(intervals);

            System.out.println("Enter sample values");

            while (true) {
                input = br.readLine();

                if ("q".equals(input)) {
                    System.out.println("Exit!");
                    System.exit(0);
                }
                if ("p".equals(input)) {
                    histogram.printHistogram();
                    continue;
                }
                if ("m".equals(input)) {
                    histogram.printMean();
                    continue;
                }
                if ("v".equals(input)) {
                    histogram.printVariance();
                    continue;
                } else {
                    System.out.println("Sampling " + input);
                    histogram.insertSample(Double.parseDouble(input));
                }
            }
        } catch (IOException e) {
            e.printStackTrace();
        } finally {
            if (br != null) {
                try {
                    br.close();
                } catch (IOException e) {
                    e.printStackTrace();
                }
            }
        }
    }
}