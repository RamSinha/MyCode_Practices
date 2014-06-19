import com.sun.btrace.annotations.*;
//import static com.sun.btrace.BTraceUtils.*;
import java.util.*;
public class ArrayListTrace {
	@OnMethod(
			clazz = "java.util.ArrayList",
			method="add"
			)
	 public static void alert(@Self ArrayList self, Object o) {
		System.out.println("Added");
		System.out.println(o);
	}
}



// Follow http://fahdshariff.blogspot.in/2011/07/tracing-java-applications-with-btrace.html for more information 
