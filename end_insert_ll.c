#include <stdio.h>
#include <stdlib.h>


 
struct node{
    int n;
    struct node* next;
 };

 struct node *make_node(int val){
    struct node *N= (struct node *)malloc(1*sizeof(struct node));
    N->n= val;
    N->next= NULL;
    return N;
 }


 struct node * insert(int val, struct node *head){
    struct node *new= make_node(val);
    struct node *cur=head;
    if(head==NULL) head=new;
    else{
        while(cur!=NULL){
            cur=cur->next;
        }
        cur->next= new;
    }
    return head;
 }


 void display(struct node *head){
    struct node *cur=head;
    while(cur!=NULL){
        printf("%d ", cur->n);
        cur=cur->next;

        
    }
    printf("\n");
 }


 int main()
 {
    struct node *head=NULL;
    int val;
    scanf("%d ", &val);
    while(val!=-1)
    {
        head= insert(val, head);
        scanf("%d ", &val);
    }
    display(head);
 }