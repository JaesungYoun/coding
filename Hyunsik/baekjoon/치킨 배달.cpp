#include <bits/stdc++.h>
using namespace std;

int N,M;
int ch[51][51];
int chk[51][51];
vector<vector<int>> chickenList;
vector<pair<int,int>> house,chicken;

void combi(int start,vector<int> v){
	// ���⼭ �ִ� M���� �� ġŲ�� ����Ʈ���� ��ȯ�Ұ̴ϴ�.
	if(v.size()==M){
		chickenList.push_back(v);
		return;
	}
	else{ //���� ��ǥ�� �Ѿ�� ������ �����Ѵ�. ��͸� ���� ���� ����. 
		for(int i=start+1;i<chicken.size();i++){
			v.push_back(i);
			combi(i,v);
			v.pop_back(); //������ pop_back���굵 �����մϴ�.
			              //����Ž���� ���� ����� �� �ʱ�ȭ. 
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
			} //minn���� ������ �־ ���� �������� �ʱ�ȭ�ɰ�. 
			rett += minn; 
		}
		rettt = min(rett,rettt);
	}
	cout<<rettt;
	
}
