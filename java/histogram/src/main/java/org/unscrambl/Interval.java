package org.unscrambl;

import org.apache.commons.lang3.builder.EqualsBuilder;
import org.apache.commons.lang3.builder.HashCodeBuilder;

/**
 * Created by ramsinha on 18/12/16.
 */

/**
 * Class representing sample interval for histogram.
 * @param <T>  T can be either float or double.
 */
public class Interval<T extends Number & Comparable<T>> implements Comparable<Interval<T>> {
    private T startRange;
    private T endRange;

    /**
     * Public constructor
     * @param start startrange for histogram interval
     * @param end endrange for histogram interval
     * @throws  IllegalArgumentException if start &gt end
     */
    public Interval(T start, T end) {

        if (start.compareTo(end) > 0) {
            throw new IllegalArgumentException("start range should be less that end range");
        }
        this.startRange = start;
        this.endRange = end;

    }

    /**
     * Overriding default equal method.
     * @param obj
     * @return true if other object is logically equal to this.
     */
    public boolean equals(Object obj) {
        if (obj == null) {
            return false;
        }
        if (obj == this) {
            return true;
        }
        if (obj.getClass() != getClass()) {
            return false;
        }
        Interval other = (Interval) obj;
        return new EqualsBuilder()
                .appendSuper(super.equals(obj))
                .append(this.startRange, other.startRange)
                .append(this.endRange, other.endRange)
                .isEquals();
    }

    /**
     * Overriding default hashcode method.
     * @return Hash value
     */
    public int hashCode() {
        return new HashCodeBuilder(17, 37).
                append(this.startRange).
                append(this.endRange).
                toHashCode();
    }


    /**
     * Overriding compareTo method for sorting later.
     * @param o
     * @return
     */
    public int compareTo(Interval<T> o) {
        return this.startRange.compareTo(o.startRange);
    }

    /**
     * getter method
     * @return startRange of sample interval
     */
    public T getStartRange() {
        return this.startRange;
    }

    /**
     * getter method
     * @return endrange of sample interval
     */
    public T getEndRange() {
        return this.endRange;
    }

    /**
     * Print interval with left closed and right open ended.
     * @return
     */
    public String toString() {
        return "[ " + this.getStartRange() + " , " + this.getEndRange() + " )";
    }
}


