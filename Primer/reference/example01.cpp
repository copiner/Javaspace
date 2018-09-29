#include<iostream>
using namespace std;

int *temp = 0; 
int *temping = 0;
void change1(int n){
  cout<<"change1: "<<&n<<endl;
  cout<<"1_n: "<<n<<endl;
  temping = &n;
  n++;
  temp = &n;
}

void change2(int &n){
  cout<<"change2: "<<&n<<endl;
  cout<<"2_n: "<<n<<endl;  
  n++;
}

void change3(int *n){
  cout<<"change3: "<<n<<endl;
  cout<<"3_n: "<<n<<endl;
  *n=*n+1;
}

int main(){
  int n = 10;
  cout<<"n: "<<&n<<endl;
  change1(n);
  cout<<"1-n: "<<n<<endl;
  change2(n);
  cout<<"2-n: "<<n<<endl;
  change3(&n);
  cout<<"3-n: "<<n<<endl;

  cout<<"*temping: "<<*temping<<endl;  
  cout<<"*temp: "<<*temp<<endl;
}
