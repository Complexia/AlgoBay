//bubble sort
//O(n^2) complexity
public class BubbleSort {

	public static void main(String[] args) {
		int[] array = {10,5,9,8,7,1,2,25,101};
		for(int i=0;i<array.length;i++) {
			for(int j=i+1;j<array.length;j++) {
				if(array[j] < array[i]) {
					int x = array[i];
					array[i] = array[j];
					array[j] = x;
				}
			}
		}
		for(int i=0;i<array.length;i++) {
			System.out.println(array[i]);
		}

	}
}
