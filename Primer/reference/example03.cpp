#include<iostream>
using namespace std;

const maxCard = 100;

class Set{
  int elems[maxCard];
  int card;
public:
  Set(){ card=0;}
  friend Set operator *(Set,Set);
  // friend Set operator *(Set &,Set &);
};

Set operator *(Set Set1,Set Set2){
  Set res;
  for(int i=0;i<Set1.card;++i){
    for(int j=0;j<Set2.card;++i){
      if(Set1.elems[i] == Set2.elems[j]){
	res.elems[res.card++]=Set1.elems[i];
	break;
      }
    }
  }
  return res;
}
Set operator *(Set &Set1,Set &Set2){
  Set res;
  for(int i=0;i<Set1.card;++i){
    for(int j=0;j<Set2.card;++i){
      if(Set1.elems[i] == Set2.elems[j]){
	res.elems[res.card++]=Set1.elems[i];
	break;
      }
    }
  }
  return res;
}
