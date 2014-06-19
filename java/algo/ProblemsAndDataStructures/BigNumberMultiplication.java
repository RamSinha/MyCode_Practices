package ProblemsAndDataStructures;

import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.List;

public class BigNumberMultiplication {
	
	public static void main(String[] args) throws Exception {
		List <String > l = new ArrayList<String>();
		BufferedReader  a = new BufferedReader( new InputStreamReader(System.in));
		System.out.println("Enter the value of pairs");
		String s1 = a.readLine();
		int n = Integer.parseInt(s1);
		while (n > 0){
			String s =  a.readLine();
			l.add(s);
			n--;
		}
		
		for (String s : l){
		int n1 = Integer.parseInt(s.split(" ")[0]);
		int n2 = Integer.parseInt(s.split(" ")[1]);
		System.out.println(product(intToArray(n1, intLength(n1)), intToArray(n2, intLength(n2))));
		}
    }
	
	 public static String product(int[] array1, int[] array2) {
	        int product[] = new int[array1.length + array2.length]; //[n+m]
	        
	        for(int i=0; i<array1.length; i++){        
	            for(int j=0; j<array2.length; j++){ 
	                
	                int prod = array1[i] * array2[j];        int prodLength = intLenght(prod);
	                int prodAsArray[] =  intToArray(prod, prodLength, prodLength); //18-->[8,1]
	                
	                //If the product has 2 digits, the 2nd one should be stored in the next index
	                for (int k =0; k < prodAsArray.length; k++) {//1 to 2 iterations, at most
	                    product[i+j+k] += prodAsArray[k];
	                    
	                    //Handle carry 
	                    int currentValue = product[i+j+k];
	                    if(currentValue>9){
	                        product[i+j+k] = 0;                
	                        int curValueLength = intLenght(currentValue);
	                        int curValueAsArray[] = intToArray(currentValue, curValueLength);
	                        for (int l = 0; l < curValueAsArray.length; l++) {
	                            product[i+j+k+l] += curValueAsArray[l];
	                        }
	                    }
	                }      
	            }
	        }
	        return arrayToString(product);
	    }
	
	
	 
	    private static int[] intToArray(int bigInt, int bigIntLength) {
	        return intToArray(bigInt, bigIntLength, bigIntLength);
	    }
	    private static int intLenght(int bigInt) {
	        return Integer.toString(bigInt).length();
	    }
	    private static int[] intToArray(int bigInt, int bigIntLength, int arrayLength) {
	        int array[] = new int[arrayLength ]; 
	        for (int i = 0; i < arrayLength ; i++) {
	            array[i] = ( i<bigIntLength ?
	                             getDigitAtIndex(bigInt, bigIntLength - i -1) :
	                             0 ); //complete the rest of the array with 0
	        }
	        return array;
	    }
	   
	    private static int getDigitAtIndex(int longint,int index){        
	        return Integer.parseInt(Integer.toString(longint).substring(index, index+1)); 
	    }
	    
	    
	    
	    private static String arrayToString(int[] sumArray) {
	        String sum = "";
	        boolean firstNonZero = false; 
	        for (int i = sumArray.length-1; i >= 0 ; i--) { //from array end to beginning
	            
	            if(!firstNonZero && (sumArray[i]==0)){ //ignore if 1st digits are 0 
	                continue;
	            } else{
	                firstNonZero=true;
	            }
	            sum += sumArray[i];
	            if((i%3 ==0)&&i!=0){ sum +=",";}  //formatting
	        }
	        String sumStr = sum.length()==0?"0":sum; // handle the 0 value (ha, input was not big!)
	        return sumStr;
	    }
	
	    
		public static int intLength(int k){
			String s = String.valueOf(k);
			return s.length();
		}	    
}
