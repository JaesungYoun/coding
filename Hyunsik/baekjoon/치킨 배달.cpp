#include <bits/stdc++.h>
using namespace std;

int N,M;
int ch[51][51];
int chk[51][51];
vector<vector<int>> chickenList;
vector<pair<int,int>> house,chicken;

void combi(int start,vector<int> v){
	// 여기서 최대 M개씩 고른 치킨집 리스트들을 반환할겁니다.
	if(v.size()==M){
		chickenList.push_back(v);
		return;
	}
	else{ //다음 지표로 넘어가서 조합을 구현한다. 재귀를 통한 조합 구현. 
		for(int i=start+1;i<chicken.size();i++){
			v.push_back(i);
			combi(i,v);
			v.pop_back(); //벡터의 pop_back연산도 존재합니다.
			              //완전탐색을 위한 경우의 수 초기화. 
		}	
	} 
}


int main() {
	cin>>N>>M;
	for(int i=1;i<=N;i++){
		for(int j=1;j<=N;j++){
			cin>>ch[i][j];
			if(ch[i][j]==1){
				house.push_back({i,j});
			}
			else if(ch[i][j]==2){
				chicken.push_back({i,j});
			}
		}
	}
	
	vector<int> v;
	combi(-1,v);
	
	int rettt=2147000000;
	for(vector<int> a:chickenList){
		int rett = 0;
		for(pair<int,int> b : house){
			int minn=2147000000;
			for(int ch : a){
				int dis = abs(b.first - chicken[ch].first) + abs(b.second - chicken[ch].second);
				minn = min(dis,minn);
			} //minn에는 한집에 있어서 제일 작은값이 초기화될것. 
			rett += minn; 
		}
		rettt = min(rett,rettt);
	}
	cout<<rettt;
	
}
