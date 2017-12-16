#include <stdio.h>

#define QUEUE_SIZE 10
int front,rear;
int queue[QUEUE_SIZE];

void init(){
	front = 0;
	rear = 0;
}
bool isFull(){
	if( (rear+1)%QUEUE_SIZE==front)
		return true;
	return false;
}
bool isEmpty(){
	if( rear ==front)
		return true;
	return false;
}
void enqueue(int data){
	if(isFull()){
		printf("Full\n");
	}else{
		rear = (++rear)%QUEUE_SIZE;
		queue[rear]=data;
	}
}
int dequeue(){
	int result;
	if(isEmpty()){
		printf("Empty\n");
		return -1;
	}else{
		
		front = (++front)%QUEUE_SIZE;
		result = queue[front];
	}
}

void main(){

}