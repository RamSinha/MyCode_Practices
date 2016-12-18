package org.unscrambl.utils;

import org.unscrambl.Interval;

import java.util.*;
import java.util.concurrent.Callable;
import java.util.concurrent.ExecutorService;
import java.util.concurrent.Executors;
import java.util.stream.Collectors;

/**
 * Created by ramsinha on 18/12/16.
 */

/**
 * Util class performing various operation on Histogram datastructure.
 */
public class HistogramUtil {
    public enum Operations {
        PRINTHISTOGRAM,
        GETMEAN,
        GETVARIANCE
    }

    /**
     * Service is used to print histogram.
     */
    public static ExecutorService executor = Executors.newFixedThreadPool(5);

    /**
     * Using methods to validate if there is any overlapping in sample intervals.
     * And if yes, then proper error is flagged.
     *
     * @param inputIntervals
     * @param <T>
     * @return
     */
    public static <T extends Number & Comparable<T>> List<Interval<T>> findOverLapping(List<Interval<T>> inputIntervals) {
        Collections.sort(inputIntervals);

        Iterator<Interval<T>> iter = inputIntervals.iterator();
        Set<Interval<T>> overLappingIntervals = new HashSet<>();
        Interval<T> prevInterval = null;
        Interval<T> nextInterval = null;
        while (iter.hasNext()) {
            nextInterval = iter.next();
            if (prevInterval == null) {
                prevInterval = nextInterval;
                continue;
            }

            if (prevInterval.getEndRange().compareTo(nextInterval.getStartRange()) > 0) {
                overLappingIntervals.add(prevInterval);
                overLappingIntervals.add(nextInterval);
            }
            prevInterval = nextInterval;
        }

        List<Interval<T>> listOfOverlappingIntervals = overLappingIntervals.stream().collect(Collectors.toList());
        Collections.sort(listOfOverlappingIntervals);
        return listOfOverlappingIntervals;
    }


    /**
     * Add two samples
     *
     * @param first
     * @param second
     * @param <T>
     * @return
     */
    public static <T extends Number & Comparable<T>> T add(T first, T second) {

        if (first instanceof Double) {
            return (T) Double.valueOf((first.doubleValue() + second.doubleValue()));
        } else if (first instanceof Float) {
            return (T) Float.valueOf(((first.floatValue() + second.floatValue())));
        } else if (first instanceof Integer) {
            return (T) Integer.valueOf(((first.intValue() + second.intValue())));
        }
        throw new IllegalArgumentException();
    }

    /**
     * Divide sample with a given number.
     *
     * @param first
     * @param n
     * @param <T>
     * @return
     */
    public static <T extends Number & Comparable<T>> T divide(T first, Integer n) {
        assert (n != 0);
        if (first instanceof Double) {
            return (T) Double.valueOf((first.doubleValue() / n));
        } else if (first instanceof Float) {
            return (T) Float.valueOf((first.floatValue() / n));
        } else if (first instanceof Integer) {
            return (T) Double.valueOf((first.intValue() / (n * 1.0)));
        }
        throw new IllegalArgumentException();
    }

    /**
     * Square sample value.
     *
     * @param first
     * @param <T>
     * @return
     */
    public static <T extends Number & Comparable<T>> T square(T first) {
        if (first instanceof Double) {
            return (T) Double.valueOf(Math.pow(Double.valueOf(first.doubleValue()), 2));
        } else if (first instanceof Float) {
            return (T) Double.valueOf(Math.pow(first.floatValue(), 2));
        } else if (first instanceof Integer) {
            return (T) Double.valueOf(Math.pow(first.intValue(), 2));
        }
        throw new IllegalArgumentException();
    }

    /**
     * Substract two sample values.
     *
     * @param first
     * @param second
     * @param <T>
     * @return
     */
    public static <T extends Number & Comparable<T>> T substract(T first, T second) {
        if (first instanceof Double) {
            return (T) Double.valueOf((first.doubleValue() - second.doubleValue()));
        } else if (first instanceof Float) {
            return (T) Float.valueOf(((first.floatValue() - second.floatValue())));
        } else if (first instanceof Integer) {
            return (T) Integer.valueOf(((first.intValue() - second.intValue())));
        }
        throw new IllegalArgumentException();
    }

    /**
     * Util to print histogram in new thread.
     *
     * @param <T>
     */
    public static class HistogramPrintUtil<T extends Number & Comparable<T>> implements Callable<T> {

        Map<Interval<T>, Queue<T>> snapshot = new HashMap<>();
        List<T> outliers = new ArrayList<>();
        HistogramUtil.Operations operation = null;

        public HistogramPrintUtil(Map<Interval<T>, Queue<T>> samples, List<T> outliers, HistogramUtil.Operations operation) {
            this.snapshot = samples;
            this.outliers = outliers;
            this.operation = operation;
        }

        public T call() {
            T result = null;
            if (this.operation.equals(Operations.PRINTHISTOGRAM)) {
                printHistogram();
            } else if (this.operation.equals(Operations.GETMEAN)) {
                result = printMean();
            } else {
                result = printVariance();
            }
            return result;
        }

        public T printVariance() {
            List<T> samples = new ArrayList<>();
            T mean = null;
            T variance = null;
            List<T> deviationSquare = new ArrayList<>();
            for (Map.Entry<Interval<T>, Queue<T>> entry : snapshot.entrySet()) {
                samples.addAll(entry.getValue());
            }

            if (!samples.isEmpty()) {
                T sampleSum = samples.subList(1, samples.size()).stream().reduce(samples.get(0), (x, y) -> HistogramUtil.add(x, y));
                mean = HistogramUtil.divide(sampleSum, samples.size());
                for (T sample : samples) {
                    deviationSquare.add(HistogramUtil.square(HistogramUtil.substract(sample, mean)));
                }
            }
            T sampleSquare = deviationSquare.subList(1, samples.size()).stream().reduce(deviationSquare.get(0), (x, y) -> HistogramUtil.add(x, y));
            if (samples.size() == 1) {
                variance = (T) Double.valueOf(0);
            } else {
                variance = (HistogramUtil.divide(sampleSquare, samples.size() - 1));
                System.out.println("sample variance: " + variance);
            }
            return variance;
        }

        public T printMean() {
            List<T> samples = new ArrayList<>();
            T mean = (T) (Double.valueOf(-1));
            T variance = null;
            List<T> deviationSquare = new ArrayList<>();
            for (Map.Entry<Interval<T>, Queue<T>> entry : snapshot.entrySet()) {
                samples.addAll(entry.getValue());
            }
            if (!samples.isEmpty()) {
                T sampleSum = samples.subList(1, samples.size()).stream().reduce(samples.get(0), (x, y) -> HistogramUtil.add(x, y));
                mean = HistogramUtil.divide(sampleSum, samples.size());
            }
            System.out.println(mean);
            return mean;
        }

        public T printHistogram() {
            List<T> samples = new ArrayList<>();
            T mean = null;
            T variance = null;
            List<T> deviationSquare = new ArrayList<>();
            for (Map.Entry<Interval<T>, Queue<T>> entry : snapshot.entrySet()) {
                samples.addAll(entry.getValue());
                if (this.operation.equals(Operations.PRINTHISTOGRAM)) {
                    System.out.println(entry.getKey() + ": " + entry.getValue().size());
                }
            }

            if (this.operation.equals(Operations.PRINTHISTOGRAM)) {
                System.out.println("outliers: " + this.outliers);
            }


            if (!samples.isEmpty()) {
                T sampleSum = samples.subList(1, samples.size()).stream().reduce(samples.get(0), (x, y) -> HistogramUtil.add(x, y));
                mean = HistogramUtil.divide(sampleSum, samples.size());

                for (T sample : samples) {
                    deviationSquare.add(HistogramUtil.square(HistogramUtil.substract(sample, mean)));
                }
                if (this.operation.equals(Operations.GETMEAN) || this.operation.equals(Operations.PRINTHISTOGRAM)) {
                    System.out.println("sample mean: " + mean);
                }
            }
            if (!samples.isEmpty()) {

                T sampleSquare = deviationSquare.subList(1, samples.size()).stream().reduce(deviationSquare.get(0), (x, y) -> HistogramUtil.add(x, y));

                if (this.operation.equals(Operations.GETVARIANCE) || this.operation.equals(Operations.PRINTHISTOGRAM)) {
                    if (samples.size() == 1) {
                        System.out.println("sample variance: 0");
                    } else {
                        variance = (HistogramUtil.divide(sampleSquare, samples.size() - 1));
                        System.out.println("sample variance: " + variance);
                    }
                }
            }
            T result = null;
            if (this.operation.equals(Operations.GETMEAN)) {
                result = mean;
            }
            if (this.operation.equals(Operations.GETVARIANCE)) {
                result = variance;
            }
            return result;
        }
    }
}
