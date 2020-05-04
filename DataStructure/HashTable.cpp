/* Hash Table (linked list) */
#include <iostream>
#include <stdlib.h>
using namespace std;

#define MAX_HASH_TABLE 47

typedef struct node{
    int value;
    struct node * next;
}node;

node hashtable[MAX_HASH_TABLE];
int hashfunction(int value){
    return value % MAX_HASH_TABLE;
}
void insert(int value){
    int key = hashfunction(value);

    // make new node
    node * newnode = (node * )malloc(sizeof(node));
    newnode->next = NULL;
    newnode->value = value;

    // find the right inserting space 
    node * cur = &hashtable[key];
    while(cur->next){cur = cur->next;}
    cur->next = newnode;
}
void remove(int value){
    int key = hashfunction(value);
    // find the right node to delete!
    node * target_prev = &hashtable[key];
    while(target_prev->next){
        if(target_prev->next->value == value){
            // find the right node ! 
            break;
        }
        target_prev = target_prev->next;
    }
    if(target_prev->next){
        // delete target_prev allocated memory
        node * target = target_prev->next;
        target_prev->next = target->next;
        free(target);
    }else{
        // there is no target 
        printf("[Error] NO ELEMENT contains value(%d)\n",value);
    }
    
}
void print_hashtable(){
    printf("=====================\n");
    for(int i=0; i<MAX_HASH_TABLE;i++){
        node * cur = &hashtable[i];
        if(cur){
            printf("hashtable[%d] : ",i);
            cur = cur->next;
        }
        
        while(cur){
            printf("-> %d ", cur->value);
            cur = cur->next;
        }
        printf("\n");
    }
}
int main(){
    insert(3);
    insert(4);

    print_hashtable();

    remove(3);
    remove(6);
    print_hashtable();
    return 0;
}