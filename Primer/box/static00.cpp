#include<iostream>
using namespace std;

class Text{
public:
  static int count;
};
int Text::count = 0;

int main(){
  Text t1;
  Text t2;

  t1.count = 100;
  cout<<"count: "<<t2.count<<endl;
  return 0;
}
