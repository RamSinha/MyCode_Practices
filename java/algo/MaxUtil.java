import java.util.Arrays;
import java.util.Iterator;
import java.util.List;

public class MaxUtil {

	public static <T extends Comparable< ? super T>> T max(List<? extends T> list) {
		Iterator<? extends T> i = list.iterator();
		T result = i.next();
		while (i.hasNext()) {
			T t = i.next();
			if (t.compareTo(result) > 0)
				result = t;
		}
		return result;
	}
	
	
	public static void main(String[] args) {
	    List<Integer> numList = Arrays.asList(1,2,3,4);
	    Integer num = max(numList);
	    System.out.println(num);
    }
}
