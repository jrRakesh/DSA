//Implementation of BST
#include<stdio.h>
#include<stdlib.h>
struct BST 
{
    int data;
    struct BST *left;
    struct BST *right;
    struct BST *parent;
};
struct BST* insert(struct BST *root, struct BST *NewNode)
{
    if(root == NULL)
        root = NewNode;
    else if(NewNode ->data < root->data)
    {
        root-> left = insert(root->left, NewNode);
        root -> left->parent = root;
    }
    else{
        root->right = insert(root->right, NewNode);
        root->right->parent = root;
    }
    return root;
}

struct BST* search(struct BST *root, int element)
{
    if(root == NULL || element == root ->data)
        return root;
    
}
struct BST* find_max(struct BST *root)
{
    while (root->right != NULL )
    {
        root = root ->right;
    }
    return root;
}
struct BST* find_min(struct BST *root)
{
    while (root->left != NULL )
    {
        root = root ->left;
    }
    return root;
    
}
struct BST* delete(struct BST *root, int element)
{
    if(root == NULL)
    {
        return root;
    }
    else if( element < root -> data)
    {
        root ->left = delete(root->left, element);
        if(root->left) root->left->parent = root;
    }
    else if( element > root -> data)
    {
        root ->right = delete(root->right, element);
        if(root->right) root->right->parent = root;
    }
    else
    {
        // case 1 and 2: no children
        if(root -> left == NULL)
        {
            struct BST *temp = root ->left;
            if(temp) temp->parent = root -> parent;
            free(root);
            return temp;
        } else
        {
            // case 3
            struct BST *temp = find_min(root->right);
            root->data = temp->data;
            root->right = delete(root->right, temp ->data);
            if(root->right) root->right->parent = root;
        }
    }
    return root;
}

void preorder(struct BST *root){
    if(root != NULL)
    {
        printf("%d\t", root->data);
        preorder(root->left);
        preorder(root->right);
    }
}
void inorder(struct BST *root)
{
    if(root != NULL)
    {
        inorder(root->left);
        printf("%d\t", root->data);
        inorder(root->right);
    }
}
void postorder(struct BST *root){
    if(root != NULL)
    {
        postorder(root->left);
        postorder(root->right);
        printf("%d\t", root->data);
    }
}
int main()
{
    struct BST *root, *temp;
    root = NULL;
    int choice, data;
    do
    {
        printf("\n0.CREATE\n1.INSERT\n2.DELETE\n3.SERACH\n4.MAX\n5.MIN\n6.TRAVERSE\n7.EXIT\n");
        printf("Enter your choice : ");
        scanf("%d", &choice);
        int A[] = {70,40,75,77,65,30,28,72};

        switch (choice)
        {
        case 0:
        for(int i=0; i<8; i++)
        {
            temp = (struct BST*)malloc(sizeof(struct BST));
            temp ->data = A[i];
            temp ->left = temp -> right = temp->parent = NULL;
            root = insert(root, temp);

        }

        case 1:
            printf("Enter your data \t");
            scanf("%d", &data);
            temp = (struct BST*)malloc(sizeof(struct BST));
            temp ->data = data;
            temp ->left = temp->right = temp->parent = NULL;
            root = insert (root, temp);
            break;
        case 2:
            printf("Enter your data : ");
            scanf("%d", &data);
            root = delete(root, data);
            break;
        case 3:
            printf("Enter your data : ");
            scanf("%d", &data);
            temp = search(root, data);
            if(temp)
                printf("Element found!");
            else
                printf("Element not found!");
            break;
        case 4:
           temp = find_max(root);
           if(temp)
            printf("MAXIMUM IS %d \n", temp->data);
            break;
        case 5:
           temp = find_min(root);
           if(temp)
            printf("MINIMUM IS %d \n", temp->data);
            break;
        case 6:
            printf("PREORDER: \n");
            preorder(root);
            printf("\n");
            printf("INORDER: \n");
            inorder(root);
            printf("\n");
            printf("POSTORDER: \n");
            postorder(root);
            printf("\n");
            break;
        case 7:
            break;
        
        default:
            printf("Wrong input!");
            break;
        }
    }while (choice != 7);
    return 0;
    
}

