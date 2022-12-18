/*
	Implenting the Quick Select Algorithm.
	Finds the k'th largest item in an unsorted array.
*/

#include <iostream>
using namespace std;

void swap_vals(int& x, int& y) {
	int z = x;
	x = y;
	y = z;
}


// returns the index of the pivot
int partition(int array[], int num) {
	// swap the pivot to the end of the array
	swap_vals(array[num/2], array[num - 1]);

	int lo_index = 0, hi_index = num - 2;

	// invariant: throughout the algorithm we have
	// array[i] < array[num-1] for every i < lo_index and
	// array[j] >= array[num-1] for every j > hi_index
	while (lo_index <= hi_index) {
		if (array[lo_index] < array[num - 1]) {
			lo_index++;
		}
		else if (array[hi_index] >= array[num - 1]) {
			hi_index--;
		}
		else {
			// just swap their values, the next iteration will adjust indices
			swap_vals(array[lo_index], array[hi_index]);
		}
	}

	// move the pivot to its proper location
	swap_vals(array[num - 1], array[hi_index + 1]);
	return hi_index + 1;
}


int quick_select(int array[], int num, int k) {
// select a pivot and rearrange the array around this pivot
int pivot_index = partition(array, num);

if (k == pivot_index) {
	// BASE CASE: if the pivot landed exactly at the index we are looking for, just return it
	return array[k];
}
else if (k < pivot_index) {
	// if the index of the pivot is > k, then we just search the part of the array
	// that is left of the pivot
	return quick_select(array, pivot_index, k);
}
else {
	// search the part of the array that is right of the pivot
	// the value k changes because we are skipping over some items
	int skipped = pivot_index+1;
	return quick_select(array + skipped, num - skipped, k - skipped);
}
}




int main() {
    int *array;
	int num = 8;

    array = new int[num];

    cout << "Filling an array with " << num << " random values..." << endl << endl;

    for (int i = 0; i < num; i++) {
            array[i] = rand();
    }

    cout << "The new array is: [ ";
    for (int i = 0; i < num; i++) {
    	cout << array[i] << ' ';
    }
    cout << "]" << endl << endl;

    int k = 5;

    int kth_value = quick_select(array, num, k);

    cout << "The " << k << "'th largest value is: " << kth_value << endl << endl;

    delete[] array;

    return 0;





}



