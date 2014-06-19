package ProblemsAndDataStructures;

public class HeapSort {

	public static void heapSort(int a[]) {
		int length = (a.length - 1) / 2;
		for (int i = length; i >= 0; i--) {
			helper(a, i, a.length);
		}
	}

	public static void helper(int a[], int i, int l) {
		int lSon = 2 * (i) + 1;
		int rSon = 2 * (i) + 2;
		int largest = i;
		if (lSon < l && a[lSon] > a[i]) {
			largest = lSon;
		}
		if (rSon < l && a[rSon] > a[largest]) {
			largest = rSon;
		}

		if (largest != i) {
			swap(a, largest, i);
			helper(a, largest, l);
		}
	}

	public static void swap(int a[], int i, int j) {
		int temp = a[i];
		a[i] = a[j];
		a[j] = temp;
	}
}
