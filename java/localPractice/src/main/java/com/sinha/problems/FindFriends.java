package com.sinha.problems;

import java.util.HashSet;
import java.util.Iterator;
import java.util.Objects;
import java.util.Set;

public class FindFriends {
	static int friendCircles(String[] friends) {

		Set<Set<Integer>> initialState = new HashSet<>();
		for (int i = 0; i < friends.length; i++) {
			Set<Integer> temp = new HashSet<>();
			temp.add(i);
			initialState.add(temp);
		}

		Set<Pair> pairs = new HashSet<>();

		for (int i = 0; i < friends.length; i++) {
			for (int j = 0; j < friends[i].length(); j++) {
				if ((friends[i].charAt(j) + "").equalsIgnoreCase("y") && i != j) {
					pairs.add(new Pair(i, j));
				}
			}
		}
		Set<Set<Integer>> toBeRemoved = new HashSet<>();
		for (Pair p : pairs) {
			Set<Set<Integer>> toBeMergerd = new HashSet<>();
			Iterator<Set<Integer>> it = initialState.iterator();
			while (it.hasNext()) {

				Set<Integer> temp1 = it.next();

				toBeMergerd.clear();
				if (temp1.contains(p.a)) {
					toBeMergerd.add(temp1);
					toBeRemoved.add(temp1);
				}

				if (temp1.contains(p.b)) {
					toBeMergerd.add(temp1);
					toBeRemoved.add(temp1);
				}
			}

			if (toBeRemoved.size() >= 2) {
				initialState.removeAll(toBeRemoved);
				Set<Integer> finalSet = new HashSet<>();
				for (Set<Integer> s : toBeMergerd) {
					finalSet.addAll(s);
				}
				initialState.add(finalSet);
			}
		}
		return initialState.size();
	}

	static class Pair {

		int a = 0;
		int b = 0;

		@Override
		public String toString() {
			return (a + "," + b);
		}

		@Override
		public boolean equals(Object obj) {
			if (!(obj instanceof Pair)) {
				return false;
			} else {
				Pair that = (Pair) obj;
				return (that.a == this.a && that.b == this.b)
						|| (that.a == this.b && that.b == this.a);
			}
		}

		@Override
		public int hashCode() {
			return Objects.hashCode(a + b);
		}

		Pair(int a, int b) {
			this.a = a;
			this.b = b;
		}
	}

	public static void main(String[] args) {
		System.out.println(friendCircles(new String[] { "YNNNN", "NYNNN", "NNYNN",
				"NNNYN", "NNNNY" }));
	}
}
