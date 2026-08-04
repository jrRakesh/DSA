#include<iostream>
#include<cstdlib>
#include<chrono>
#define MAX 100000
void display(int A[],int n)
{
    int i;
    for(i = 0;i<n;i++)
    {
        std::cout << A[i] <<" ";
    }
    std::cout<<"\n" ; 
}
void merge(int A[], int l,int m,int r)
{
    int i = l;
    int j = m;
    int k = l;
    int B[MAX];
    while(i<m && j<= r)
    {
        if(A[i]<=A[j])
            B[k++] = A[i++];
        else
            B[k++] = A[j++];
    }
    for(;i<m;i++, k++)
        B[k] = A[i];
    for(;j<=r;j++, k++)
        B[k] = A[j];
    for(k=l; k<=r; k++)
        A[k] = B[k];
}

void mergeSort(int A[],int l, int r)
{
    int m;
    m = (l+r)/2;
    if (l<r)
    {
        mergeSort(A, l, m);
        mergeSort(A, m+1, r);
        merge(A, l, m+1, r);
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
    display(A,n); // display before sorting
    auto start = std::chrono::steady_clock::now();
   
    mergeSort(A,0,n-1);
    
    auto end =   std::chrono::steady_clock::now();
    display(A,n); // display after sorting
    auto time_taken = std::chrono::duration_cast<std::chrono::nanoseconds>(end-start);
    std::cout<<"Time taken is "<<time_taken.count()*1e-09<<" s\n";
    return 0;

}