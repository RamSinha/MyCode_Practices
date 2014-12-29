
import java.io.BufferedReader;
import java.io.InputStreamReader;

public class FactorialBigNumber {

	public static void main(String[] args) throws Exception {

		BufferedReader a = new BufferedReader(new InputStreamReader(System.in));
		System.out.println("Enter a number \n");
		String s = a.readLine().trim().replaceFirst("^0+(?!$)", ""); // Remove
																		// leading
																		// zeros
		if (!isValidNum(s)) {
			System.out
					.println("Exiting: Wrong input format. Please enter a valid number. Also please make sure number is positive integer");
			System.exit(1);
		}
		if (isZero1(s)) {
			System.out.println("Factorial of " + s + " is: " + 1); // Factorial zero is 1
			System.exit(0);
		}

		System.out.println("Factorial of " + s + " is: " + factorial(s));
	}

	/**
	 * Method return factorial for given big number.
	 * Method Follows below steps
	 * <li>1. Convert the number to int Array in reverse order </li>
	 * <li>2. Decrement the number and convert to int Array in reverse order </li>
	 * <li>3. Multiply the both number using traditional method </li>
	 * 
	 * @param bigInt
	 * @return Factorial of the big number in String format.
	 */
	public static String factorial(String bigInt) {
		String fact = "1";
		while (!isZero1(bigInt)) {
			fact = multiply(reverseRepr(fact), reverseRepr(bigInt));
			bigInt = decrement(bigInt);
		}
		return fact;
	}

	private static int[] reverseRepr(String s) {
		int[] result = new int[s.length()];
		for (int i = s.length() - 1; i >= 0; i--) {
			result[s.length() - 1 - i] = Integer.parseInt(s.charAt(i) + "");
		}
		return result;
	}

	private static int[] getIntArray(String s) {

		int[] repr = new int[s.length()];
		for (int i = 0; i < s.length(); i++) {
			repr[i] = Integer.parseInt(new String(s.charAt(i) + ""));
		}
		return repr;
	}

	private static boolean isValidNum(String input) {
		boolean flag = true;
		for (int i = 0; i < input.length(); i++) {
			if (input.charAt(i) >= '0' && input.charAt(i) <= '9') {
				continue;
			} else {
				flag = false;
				break;
			}
		}

		return flag;
	}

	public static String decrement(String bigInt) {
		int[] repr = decrement(getIntArray(bigInt));
		String result = "";
		for (int i : repr) {
			result += i;
		}

		return result.replaceFirst("^0+(?!$)", "");
	}

	private static int[] decrement(int[] numberInArray) {

		if (isZero(numberInArray)) {
			return numberInArray;
		}

		boolean lookForPreviousNumber = true;

		for (int i = numberInArray.length - 1; i >= 0 && lookForPreviousNumber; i--) {
			if (numberInArray[i] == 0) {
				numberInArray[i] = 9;
			} else {
				numberInArray[i] -= 1;
				lookForPreviousNumber = false;
			}
		}
		return numberInArray;
	}

	private static boolean isZero1(String bigInt) {
		boolean isZero = true;
		for (int i = 0; i < bigInt.length(); i++) {
			if (bigInt.charAt(i) != '0') {
				isZero = false;
			}
		}
		return isZero;
	}

	private static boolean isZero(int[] numberArray) {

		boolean isZero = true;

		for (int i : numberArray) {
			if (i != 0) {
				isZero = false;
				break;
			}
		}
		return isZero;
	}

	public static String multiply(int[] array1, int[] array2) {
		int product[] = new int[array1.length + array2.length];

		for (int i = 0; i < array1.length; i++) {
			for (int j = 0; j < array2.length; j++) {

				int prod = array1[i] * array2[j];
				int prodLength = intLenght(prod);
				int prodAsArray[] = intToArray(prod, prodLength, prodLength);

				for (int k = 0; k < prodAsArray.length; k++) {
					product[i + j + k] += prodAsArray[k];

					int currentValue = product[i + j + k];
					if (currentValue > 9) {
						product[i + j + k] = 0;
						int curValueLength = intLenght(currentValue);
						int curValueAsArray[] = intToArray(currentValue,
								curValueLength);
						for (int l = 0; l < curValueAsArray.length; l++) {
							product[i + j + k + l] += curValueAsArray[l];
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

	private static int[] intToArray(int bigInt, int bigIntLength,
			int arrayLength) {
		int array[] = new int[arrayLength];
		for (int i = 0; i < arrayLength; i++) {
			array[i] = (i < bigIntLength ? getDigitAtIndex(bigInt, bigIntLength
					- i - 1) : 0);
		}
		return array;
	}

	private static int getDigitAtIndex(int longint, int index) {
		return Integer.parseInt(Integer.toString(longint).substring(index,
				index + 1));
	}

	private static String arrayToString(int[] sumArray) {
		String sum = "";
		boolean firstNonZero = false;
		for (int i = sumArray.length - 1; i >= 0; i--) {

			if (!firstNonZero && (sumArray[i] == 0)) {
				continue;
			} else {
				firstNonZero = true;
			}
			sum += sumArray[i];
		}
		String sumStr = sum.length() == 0 ? "0" : sum;
		return sumStr;
	}
}
