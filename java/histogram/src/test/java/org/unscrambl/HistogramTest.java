package org.unscrambl;

import org.junit.Test;

import java.util.ArrayList;
import java.util.List;

/**
 * Created by ramsinha on 18/12/16.
 */


public class HistogramTest {

    @Test(expected = IllegalArgumentException.class)
    public void testWithOverappingSampleIntervals() {
        Interval<Float> i1 = new Interval<>(3f, 4.1f);
        Interval<Float> i2 = new Interval<>(8.5f, 8.7f);
        Interval<Float> i3 = new Interval<>(0f, 1.1f);
        Interval<Float> i4 = new Interval<>(31.5f, 41.27f);
        Interval<Float> i5 = new Interval<>(30f, 40f);
        List<Interval<Float>> l1 = new ArrayList<>();
        l1.add(i1);
        l1.add(i2);
        l1.add(i3);
        l1.add(i4);
        l1.add(i5);
        Histogram<Float> h = Histogram.getInstance(l1);
    }


    @Test(expected = IllegalArgumentException.class)
    public void testEmptyList() {
        new Interval<>(5f, 4.1f);
    }

    @Test
    public void testMeanAndVariance() {
        Interval<Float> i1 = new Interval<>(3f, 4.1f);
        Interval<Float> i2 = new Interval<>(8.5f, 8.7f);
        Interval<Float> i3 = new Interval<>(0f, 1.1f);
        Interval<Float> i4 = new Interval<>(31.5f, 41.27f);
        Interval<Float> i5 = new Interval<>(19f, 25f);

        List<Interval<Float>> l1 = new ArrayList<>();
        l1.add(i1);
        l1.add(i2);
        l1.add(i3);
        l1.add(i4);
        Histogram<Float> h = Histogram.getInstance(l1);
        h.insertSample(40.1f);
        h.insertSample(8.1f);
        h.insertSample(8.2f);
        h.insertSample(30f);
        h.insertSample(31.51f);
        h.insertSample(1f);
        h.insertSample(41.27f);
        assert (h.printMean().intValue() == 24);
        assert (h.printVariance().intValue() == 422);
    }
}
