#include <iostream>
#include <cstdlib>
#include <chrono>
#define MAX 300000
void swapp(int *p, int *q)
{
    int temp = *p;
    *p = *q;
    *q = temp;
}
void display(int A[], int n)
{
    int i;
    for (i = 0; i < n; i++)
    {
        std::cout << A[i] << " ";
    }
    std::cout << "\n";
}

void shellSort(int A[], int n)
{
    int gap, i, temp, j;
    for (gap = n / 2; gap > 0; gap /= 2)
    {
        for (i = gap; i < n; i++)
        {
            temp = A[i];
            j = i;
            while (j >= gap && A[j - gap] > temp)
            {
                A[j] = A[j - gap];
                j = j - gap;
            }
            A[j] = temp;
        }
    }
}

int main()
{
    int i, n, A[MAX];
    std::cout << "Enter n: ";
    std::cin >> n;

    for (i = 0; i < n; i++)
    {
        A[i] = rand() % 100000;
    }
    display(A, n); // display before sorting
    auto start = std::chrono::steady_clock::now();
    shellSort(A, n);
    auto end = std::chrono::steady_clock::now();
    display(A, n); // display after sorting
    auto time_taken = std::chrono::duration_cast<std::chrono::nanoseconds>(end - start);
    std::cout << "Time taken is " << time_taken.count() * 1e-09 << " s\n";
    return 0;
}
