#include<iostream>
#include<string>

using namespace std;

int main(){
  string st("The expense of spirit\n");

  cout<<"The size: "<<st.size()<<endl;

  if(st.empty()){
    cout<<"empty"<<endl;
  }

  string st3(st);
  if(st == st3){
    cout<<"equal"<<endl;
  }
  string st2 = st3;

  cout<<"st2: "<<st2<<endl;

  string s1("hello, ");
  string s2("world\n");

  s1 += s2;

  cout<<"s1: "<<s1<<endl;

  const char *pc = ", ";
  string t1("hello");
  string t2("world");
  cout<<"pc: "<<pc<<endl;
  string t3 = t1 + pc + t2 + "\n";

  cout<<"t3: "<<t3<<endl;
}
