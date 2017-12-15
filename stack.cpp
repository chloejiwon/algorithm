#include <stdio.h>

#define MAXSIZE 10

int stack[MAXSIZE];
int top;

void init_stack(){
	top = -1;
}
bool isFull(){
	if(top==MAXSIZE)
		return true;
	return false;
}
bool isEmpty(){
	if(top==-1)
		return true;
	return false;
}
void push(int data){
	if(!isFull()){
		stack[++top]=data;
	}
	printf("Stack overflow\n");
}	
int pop(){
	int result=-1;
	if(!isEmpty()){
		result = stack[top--];
	}
	return result;
}
int main(){
	
}