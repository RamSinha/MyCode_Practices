
import java.io.IOException;

import com.CustomClassLoader;

public class Test2 {

	public static void main1(String[] args) throws IOException {
//		Configuration conf = new Configuration();
//		Path path = new Path("/data/ram/text");
//		System.out.println(path.toString());
//		FileSystem fs = FileSystem.get(conf);
//		FSDataOutputStream fos = fs.create(path, true);
//		GzipCodec gzipCodec = (GzipCodec) ReflectionUtils.newInstance(GzipCodec.class, conf);
//		Compressor gzipCompressor = CodecPool.getCompressor(gzipCodec);
//		OutputStream compressedOut = gzipCodec.createOutputStream(fos, gzipCompressor);
//		compressedOut.write("hello".getBytes());
//		compressedOut.write("Bloom".getBytes());
//		compressedOut.write("20".getBytes());
//		compressedOut.close();
//		System.out.println("done");
	}
	
	
    public static void main(String[] args) throws Exception {
        CustomClassLoader loader = new CustomClassLoader(
            new Test2().getClass().getClassLoader());
        Class<?> clazz =
            loader.loadClass("com.ram.TestClass");
        Object instance = clazz.newInstance();
        clazz.getMethod("runMe").invoke(instance);
    }

}