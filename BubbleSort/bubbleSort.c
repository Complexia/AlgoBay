//Bubble Sort
//O(n^2) complexity
#include<stdio.h>

int main() {
	int array[] = {10,5,9,8,7,1,2,25,101};
	size_t size = sizeof(array) / sizeof(array[0]);
	for(int i=0;i<size;i++) {
		for(int j=i+1;j<size;j++) {
			if(array[j] < array[i]) {
				int x = array[i];
				array[i] = array[j];
				array[j] = x;

			}
		}
	}
	for(int i=0;i<size;i++) {
		printf("%d ", array[i]);
		printf("\n");

	}
}
