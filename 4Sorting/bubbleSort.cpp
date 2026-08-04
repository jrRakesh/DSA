#include<iostream>
#include<cstdlib>
#include<chrono>
# define MAX 100000
void swap(int *p,int *q)
{
    int temp = *p;
    *p=*q;
    *q=temp;
}
void display(int A[],int n)
{
    int i;
    for(i=0;i<n;i++)
    {
        std::cout<<A[i]<<" ";
    }
    std::cout<<"\n";
}
void Bubble_sort(int A[],int n)
{
    int i,j;
    for(i=0;i<n-1;i++)
    {
        for(j=0;j<n-i-1;j++)
        {
            if(A[j]>A[j+1])
            {
                swap(&A[j],&A[j+1]);

            }
        }
    }
}
int main()
{
    int i,n,A[MAX];
    std::cout<<"enter n";
    std::cin>>n;
    for(i=0;i<n;i++)
    {
        A[i]=rand()%100000;
    }
    display(A,n);
    auto start=std::chrono::steady_clock::now();
    Bubble_sort(A,n);
    auto end=std::chrono::steady_clock::now();
    display(A,n);
    auto time_taken=std::chrono::duration_cast<std::chrono::nanoseconds>(end-start);
    std::cout<<"Time taken is "<<time_taken.count()*1e-9<<"s\n";
    return 0;
}