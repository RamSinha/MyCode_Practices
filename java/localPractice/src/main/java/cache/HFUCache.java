package cache;

import java.util.HashMap;
import java.util.Map;
import java.util.PriorityQueue;
/**
 * This is not a generic cache. This simply assumes that the element being entered are Integer only
 * @author ramsinha
 *
 */
public class HFUCache {
		static class CacheEntryObject implements Comparable<CacheEntryObject> {
		private Integer data;
		private Integer frequencyOfKey;

		private CacheEntryObject() {
			// Default Constructor
		}

		private CacheEntryObject(int data, int frequency) {
			this.data = data;
			this.frequencyOfKey = frequency;
		}

		public Integer getData() {
			return data;
		}

		public void setData(Integer data) {
			this.data = data;
		}

		public Integer getfrequencyOfKey() {
			return frequencyOfKey;
		}

		public void setfrequencyOfKey(int frequencyOfKey) {
			this.frequencyOfKey = frequencyOfKey;
		}

		@Override
		public int compareTo(CacheEntryObject o) {
			// For min heap
			return o.getfrequencyOfKey().compareTo(this.getfrequencyOfKey());
		}
	}

	private static Integer cacheCapacity;
	private static volatile HFUCache singelTon = null;
	private static Map<Integer, CacheEntryObject> cache = new HashMap<>();
	private static PriorityQueue<CacheEntryObject> queue = new PriorityQueue<>();
	/**
	 * Factory to create the singelton
	 * @param cacheCapacityValue Capacity of the cache. One time initialization is supported currently.
	 * @return return the shared singelton cache object.
	 */
	public static HFUCache createCache(int cacheCapacityValue) {
		if (cacheCapacityValue <= 0) {
			throw new IllegalArgumentException("Enter Positive value");
		}
		if (singelTon != null) {
			return singelTon;
		} else {
			synchronized (HFUCache.class) {
				if (singelTon == null) {
					singelTon = new HFUCache(cacheCapacityValue);
				}
			}
		}
		return singelTon;

	}

	private HFUCache(int cacheCapacityValue) {
		cacheCapacity = cacheCapacityValue;
	}

	/**
	 * This method does the following operation <li>Step 1: If the value is not
	 * already present, then check if the cache is full. If the cache is full
	 * then remove the minimum frequency element from the priority queue and put
	 * the new entry in the cache as well as in the min priority queue. If cache
	 * is not full then simply create a new entry in the hash and priority queue
	 * </li> <li>
	 * Step 2: If the value is already present remove that entry from queue and
	 * again put the same with update frequency. This ensure that heap is again
	 * heapified</li>
	 * 
	 * @param data
	 *            entry value for the key
	 */
	public static synchronized void addCacheEntryObject(int data) {
		if (!isCacheFull()) {
			if (cache.containsKey(data)) {
				CacheEntryObject existingEntry = cache.get(data);
				queue.remove(existingEntry);
				int frequencyOfExistingEntry = existingEntry
						.getfrequencyOfKey();
				existingEntry.setfrequencyOfKey(frequencyOfExistingEntry + 1);
				queue.add(existingEntry);
				cache.put(data, existingEntry);
			} else {
				CacheEntryObject newEntry = new CacheEntryObject(data, 1);
				queue.add(newEntry);
				cache.put(data, newEntry);
			}
		} else {
			queue.poll(); // Remove the top of queue if cache is full.
			CacheEntryObject newEntry = new CacheEntryObject(data, 1);
			queue.add(newEntry);
			cache.put(data, newEntry);
		}
	}

	public static synchronized boolean isCacheFull() {
		if (cache.size() == cacheCapacity)
			return true;

		return false;
	}

	public static synchronized void printTopElement() {
		StringBuilder output = new StringBuilder();
		for (Integer keys : cache.keySet()) {
			output.append(keys + " ");
		}
		System.out.println(output.toString());
	}
}