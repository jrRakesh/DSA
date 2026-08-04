#include<stdio.h>
#define MAX 5
struct stack{
    int TOP;
    int data[MAX];
};

void PUSH(struct stack *S, int element)
{
    if (S -> TOP == MAX - 1)
        printf("Stack Overflow!");
    else
    {
        S -> TOP++;
        S -> data[S -> TOP] = element;
    }
}

int POP(struct stack *S)
{
    int element = -1;
    if(S -> TOP == -1)
        printf("Stack Underflow!");
    else{
        element = S->data[S->TOP];
        S->TOP--;
    }
    return element;
}

int main(){
    int choice, element;
    struct stack S = {-1};
    do
    {
        printf("\n1.PUSH\n2.POP\n3.EXIT\nEnter your choice :\t");
        scanf("%d",&choice);
        switch(choice){
            case 1:
                printf("\nEnter element :\t");
                scanf("%d", &element);
                PUSH(&S, element);
                break;
            case 2:
                element = POP(&S);
                if(element != -1)
                    printf("\n%d was popped!", element);
                break;
            case 3:
                printf("\nBye\n");
                break;
        } 
    }while(choice != 3);
    return 0;
}