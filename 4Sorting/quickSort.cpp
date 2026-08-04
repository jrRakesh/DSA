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
int Partition(int A[], int l, int r)
{
    int pivot = A[l];
    int x =  l;
    int y = r;
    while(x < y)
    {
        while(A[x] <= pivot && x <= r)
            x++;
        while(A[y] > pivot)
            y--;
        if(x<y)
            swapp(&A[x], &A[y]);
    }
    swapp(&A[l], &A[y]);
    return y;
}

void quickSort(int A[],int l, int r)
{
    int P;
    if (l<r)
    {
        P = Partition(A, l, r);
        quickSort(A, l, P-1);
        quickSort(A, P+1, r);
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
    std::cout<<"\n";
    display(A,n); // display before sorting
    std::cout<<"\n";
    auto start = std::chrono::steady_clock::now();
   
    quickSort(A,0,n-1);
    
    auto end = std::chrono::steady_clock::now();
    display(A,n); // display after sorting
    std::cout<<"\n";
    auto time_taken = std::chrono::duration_cast<std::chrono::nanoseconds>(end-start);
    std::cout<<"Time taken is "<<time_taken.count()*1e-09<<" s\n";
    return 0;

}