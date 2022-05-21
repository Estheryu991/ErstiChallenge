// C++-Programm, um den maximal möglichen Wert K zu finden
// so dass das Array mindestens K Elemente hat, die
// sind größer oder gleich K.

#include <iostream>
using namespace std;

// Funktion zur Rückgabe des maximal möglichen Werts K
// so dass das Array mindestens K Elemente hat, die
// sind größer oder gleich K
int findmax(unsigned int arr[], int n)
{
	// output can contain any number from n to 0
	// where n is length of the array

	// We start a loop from n as we need to find
	// maximum possible value
	for (int i = n; i >= 1; i--)
	{
		// count contains total number of elements
		// in input array that are more than equal to i
		int count = 0;

		//Durchlaufen Sie das Eingabearray und finden Sie die Anzahl
		for (int j=0; j<n; j++)
			if (i <= arr[j])
				count++;

		if (count >= i)
		return i;
	}
	return 1;
}

// Driver code
int main()
{
	unsigned int arr[] = {1, 2, 3, 8, 10 };
	int n = sizeof(arr) / sizeof(arr[0]);
	cout << findmax(arr, n);
	return 0;
}
