package org.unscrambl;

import org.apache.commons.collections4.CollectionUtils;
import org.unscrambl.utils.HistogramUtil;

import java.util.ArrayList;
import java.util.Collections;
import java.util.HashMap;
import java.util.List;
import java.util.concurrent.ConcurrentHashMap;
import java.util.concurrent.ConcurrentLinkedQueue;
import java.util.concurrent.Future;
import java.util.concurrent.locks.Lock;
import java.util.concurrent.locks.ReentrantLock;

/**
 * Created by ramsinha on 18/12/16.
 */

/**
 * Class representing histogram, this is a singleton class.
 *
 * @param <T> T can be either Float or Double
 */
public class Histogram<T extends Number & Comparable<T>> {


    /**
     * Singleton instance
     */
    private static volatile Histogram instance = null;
    /**
     * This will hold all the current interval
     */
    private List<Interval<T>> samplingIntervals = null;
    /**
     * This concurrent map will hold sample interval as key and corresponding samples in a list.
     */
    private ConcurrentHashMap<Interval<T>, ConcurrentLinkedQueue<T>> histogramSampleIntervalToSampleMap = new ConcurrentHashMap<>();

    /**
     * This concurrentQueue will hold the outliers values.
     */
    private ConcurrentLinkedQueue<T> outliers = new ConcurrentLinkedQueue<>();

    /**
     * This lock is used only when a print histogram request comes in.
     * And to make sure locking time is as less as possible, print histogram call is executed in a separate thread.
     * using {@link Histogram#printHistogram } and {@link HistogramUtil.HistogramPrintUtil#operate()} method.
     */
    private Lock printLock = new ReentrantLock();

    /**
     * private constructor
     *
     * @param sampleIntervals List of input samples.
     */
    private Histogram(List<Interval<T>> sampleIntervals) {
        this.samplingIntervals = sampleIntervals;
        Collections.sort(this.samplingIntervals);
        this.samplingIntervals.forEach(x -> histogramSampleIntervalToSampleMap.put(x, new ConcurrentLinkedQueue()));
    }

    /**
     * Factory method to generate singleton class for Histogram.
     *
     * @param sampleIntervals List of input samples.
     * @param <T>
     * @return Singleton instance for {@link Histogram}
     */
    public static <T extends Number & Comparable<T>> Histogram<T> getInstance(List<Interval<T>> sampleIntervals) {

        if (CollectionUtils.isEmpty(sampleIntervals)) {
            throw new IllegalArgumentException("sampleIntervals can't be null or empty");
        }
        if (instance == null) {
            synchronized (Histogram.class) {
                if (instance == null) {
                    List<Interval<T>> overlappingIntervals = HistogramUtil.findOverLapping(sampleIntervals);
                    if (overlappingIntervals.isEmpty()) {
                        instance = new Histogram(sampleIntervals);
                    } else {
                        throw new IllegalArgumentException(String.format("There is overlapping in below listed input sample intervals :\n %s \n kindly provide correct input.", overlappingIntervals));
                    }
                }
            }
        }
        return instance;
    }

    /**
     * Not allowed
     */
    private Histogram() {
        throw new UnsupportedOperationException("Initialization without interval is not permitted");
    }

    /**
     * <pre>
     * This method is used to insert a sample in Histogram.
     * <b>Execution is as follows</b>
     * <ul>
     *   <li>Find the right sample interval for the given sample</li>
     *   <li>if the sample doesnt map to any of the interval, then mark it as an outlier and return.</li>
     *   <li>Check if printhistogram call is executed at this time.</li>
     *   <li>if yes, then wait till new printhistogram thread is spawned</li>
     *   <li>Else update the datastructure to hold this new sample.</li>
     * </ul>
     * </pre>
     *
     * @param sample
     */
    public void insertSample(T sample) {
        Interval<T> sampleInterval = getSampleInterval(sample);
        if (sampleInterval == null) {
            outliers.add(sample);

        } else {
            while (!printLock.tryLock()) {
            }
            this.histogramSampleIntervalToSampleMap.get(sampleInterval).add(sample);
        }

    }

    /**
     * <pre>
     * This method finds the most suitable interval for given sample.
     * <b>Below is algo</b>
     * <ul>
     *     <li> Do a binary search on sorted list of intervals</li>
     *     <li> if sample is less than starttange of pivot interval then move to left</li>
     *     <li> if sample is greater than starttange of pivot interval then check if sample is endrange of pivot </li>
     *     <li> if yes, then pivot is required interval </li>
     *     <li> if no, then search in right half</li>
     * </ul>
     * </pre>
     *
     * @param sample
     * @return
     */
    public Interval<T> getSampleInterval(T sample) {
        int lower_index = 0;
        int higher_index = this.samplingIntervals.size() - 1;


        while (lower_index <= higher_index) {
            int mid_index = lower_index + (higher_index - lower_index) / 2;

            if (this.samplingIntervals.get(mid_index).getStartRange().compareTo(sample) == 0) {
                return this.samplingIntervals.get(mid_index);
            }

            if (this.samplingIntervals.get(mid_index).getStartRange().compareTo(sample) < 0) {
                if (this.samplingIntervals.get(mid_index).getEndRange().compareTo(sample) > 0) {
                    return this.samplingIntervals.get(mid_index);
                }
                lower_index = mid_index + 1;
            } else if (this.samplingIntervals.get(mid_index).getStartRange().compareTo(sample) > 0) {
                higher_index = mid_index - 1;
            }
        }
        return null;
    }

    /**
     * This method first takes the lock to make sure right snapshot of datastructure is taken.
     * And then spawns a new thread to print histogram, and as soon as it creates the new thead, it relreases the lock.
     * So that other threads can continue sampling data.
     */
    public void printHistogram() {
        try {
            printLock.lock();
            HistogramUtil.HistogramPrintUtil printThread = new HistogramUtil.HistogramPrintUtil(new HashMap<>(histogramSampleIntervalToSampleMap), new ArrayList(outliers), HistogramUtil.Operations.PRINTHISTOGRAM);
            HistogramUtil.executor.submit(printThread);
        } finally {
            printLock.unlock();
        }
    }

    /**
     * This method first takes the lock to make sure right snapshot of datastructure is taken.
     * And then spawns a new thread to print mean, and as soon as it creates the new thead, it relreases the lock.
     * So that other threads can continue sampling data.
     */
    public Double printMean() {
        Double mean = null;
        try {
            printLock.lock();
            HistogramUtil.HistogramPrintUtil printThread = new HistogramUtil.HistogramPrintUtil(new HashMap<>(histogramSampleIntervalToSampleMap), new ArrayList(outliers), HistogramUtil.Operations.GETMEAN);
            Future<T> result = HistogramUtil.executor.submit(printThread);
            mean = result.get().doubleValue();

        } catch (Exception ex) {
            ex.printStackTrace();
        } finally {
            printLock.unlock();
        }
        return mean;
    }

    /**
     * This method first takes the lock to make sure right snapshot of datastructure is taken.
     * And then spawns a new thread to print variance, and as soon as it creates the new thead, it relreases the lock.
     * So that other threads can continue sampling data.
     */
    public Double printVariance() {
        Double variance = null;
        try {
            printLock.lock();
            HistogramUtil.HistogramPrintUtil printThread = new HistogramUtil.HistogramPrintUtil(new HashMap<>(histogramSampleIntervalToSampleMap), new ArrayList(outliers), HistogramUtil.Operations.GETVARIANCE);
            Future<T> result = HistogramUtil.executor.submit(printThread);
            variance = result.get().doubleValue();

        } catch (Exception ex) {
            ex.printStackTrace();
        } finally {
            printLock.unlock();
        }
        return variance;
    }
}
