#include <stdio.h>
#include <iostream>
#include <queue>

using namespace std;

void dfs(int start);
void bfs(int start);
int N,M,V;
int adj[1001][1001];
bool isVisited[1001];
int cnt = 0;
int main(){
	scanf("%d %d %d",&N,&M,&V);

	// adj initialize
	for (int i=0; i<N+1; i++){
		isVisited[i] = false;
		for(int j=0; j<N+1; j++){
			adj[i][j]=0;
		}
	}
	
	// make adj table
	for (int i=0; i< M; i++){
		int a,b;
		scanf("%d %d",&a,&b);
		adj[a][b] = 1;
		adj[b][a] = 1;
	}
	
	// make sure adj table is ready
/*	for (int i=0; i<=N; i++){
		for(int j=0; j<=N; j++){
			printf("%d ",adj[i][j]);
		}
		printf("\n");
	}*/
	dfs(V);
	printf("\n");
	for(int i=0; i<=N; i++)
		isVisited[i] = false;
	isVisited[V]=true;
	bfs(V);
	printf("\n");
	return 0;
}

void dfs(int start){
	if(cnt >= N){
	//	printf("\n");
		return;
	}
	isVisited[start]=true;
	printf("%d ",start);
	cnt++;
	for(int i=1; i<=N; i++){
		if(adj[start][i] == 1 && isVisited[i] ==false){
			dfs(i);
		}
	}		
}
void bfs(int start){
	queue<int> q;
	q.push(start);
	isVisited[start] = true;
	while(!q.empty()){
		int x = q.front();
		q.pop();
		printf("%d ",x);
		for(int i=1; i<=N; i++)
		{
			if(adj[x][i] == 1 && isVisited[i]==false){
				isVisited[i] = true;
				q.push(i);
			}
		}

	}
}
