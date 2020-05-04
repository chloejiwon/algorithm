/************************
 ***BINARY SEARCH TREE***
 ************************

(1) 모든 원소는 서로 다른 유일한 키를 갖는다.
(2) 왼쪽 서브 트리에 있는 원소의 키는 그 루트의 키보다 작다.
(3) 오른쪽 서브 트리에 있는 원소의 키는 그 루트의 키보다 크다.
(4) 왼쪽 서브트리와 오른쪽 서브트리도 이진 탐색 트리이다.

left child value < n < right child value (for every node)

Search : O(logn)
Insert : O(logn)
Delete : O(logn)
 */
#include <stdlib.h>
#include <iostream>
using namespace std;

class node {
    public:
    int data;
    node * left;
    node * right;
    node(int data=0){
        this->data = data;
        this->left = NULL;
        this->right = NULL;
    }

};

class bstree{
    node *root;
    public:
        bstree(int data=0);
        void insert(int key);
        node * search(node * current,int key);
        void preorder(node * current){
            if(current){
                visit(current);
                preorder(current->left);
                preorder(current->right);
            }
        }
        void visit(node * current){
            printf("%d ",current->data);
        }
        node * getRoot(){
            return root;
        }
};

bstree::bstree(int data){
    this->root = new node(data);
}

void bstree::insert(int key){
    // 중복 없다고 가정!
    node * newnode = new node(key);
    if(search(root, key) == NULL){
        node * parent = NULL;
        node * current = root;
        // 작으면 왼쪽, 크면 오른쪽으로 이동
        while(current){
            parent = current;
            if(key < parent->data){
                current = current->left;
            } else {
                current = current->right;
            }
        }
        if(key < parent->data){
            parent->left = newnode;
        } else {
            parent->right = newnode;
        }
    }
}
node * bstree::search(node * current,int key){
    if(!current)
        return NULL;
    if(key == current->data)
        return current;

    if(key < current->data){
        return search(current->left,key);
    }else{
        return search(current->right, key);
    }
}
int main(){
    bstree tree(8);
    
    tree.insert(3);
    tree.insert(4);
    tree.insert(9);
    tree.insert(1);
    tree.insert(10);

    printf("Preorder===========");
    tree.preorder(tree.getRoot());

    node *found = tree.search(tree.getRoot(),4);
    if(found){
        printf("Found!! %d\n", found->data);
    }else{
        printf("[Error] don't exist\n");
    }
    
    return 0;
}