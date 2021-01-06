//bubble sort
//O(n^2) complexity
//todo: implement a better way to find size of array
#include <iostream>

int main() {
	int size = 9;
	int array[size] = {10,5,9,8,7,1,2,25,101};
	
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
		std::cout << array[i];
		std::cout << "\n";
	}
}
