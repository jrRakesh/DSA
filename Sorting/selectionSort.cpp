#include<iostream>
#include<cstdlib>
#include<chrono>
#define MAX 300000
void swapp(int *p, int*q)
{
    int temp = *p;
    *p = *q;
    *q =temp;
}
void display(int A[],int n)
{
    int i;
    for(i = 0;i<n;i++)
    {
        std::cout << A[i] <<" ";
    }
    std::cout<<"\n" ; 
}


void SelectionSort(int A[],int n)
{
    int i,j;
    for(i = 0;i<n-1;i++)
    {
        int least = A[i];
        int pos = i;
        for(j=i+1;j<n;j++)
        {
            if(A[j]<least)
            {
                least = A[j];
                pos = j;
            }
        }
        if (i != pos)
        {
            swapp(&A[i],&A[pos]);
        }
    }
}


int main()
{
    int i,n,A[MAX];
    std::cout << "Enter n: ";
    std::cin>>n;

    for(i=0;i<n;i++)
    {
        A[i] = rand()%100000;

    }
    //display(A,n); // display before sorting
    auto start = std::chrono::steady_clock::now();
   
    SelectionSort(A,n);
    
    auto end =   std::chrono::steady_clock::now();
    display(A,n); // display after sorting
    auto time_taken = std::chrono::duration_cast<std::chrono::nanoseconds>(end-start);
    std::cout<<"Time taken is "<<time_taken.count()*1e-09<<" s\n";
    return 0;

}