#include<iostream>
using namespace std;
class Box{
public:
  Box(double l,double w,double h){
    length = l;
    width = w;
    height = h;
  }
  double Volume(){
    return length*width*height;
  }
private:
  double length;
  double width;
  double height;
  
};
int main(){
  Box Box1(3.3,1.2,1.5);
  Box Box2(8.5,6.0,2.0);
  Box *ptrBox;//declare pointer to class

  ptrBox = &Box1;
  
  cout<<"Volume: "<<ptrBox->Volume()<<endl;

  ptrBox = &Box2;

  cout<<"Volume: "<<ptrBox->Volume()<<endl;

  return 0;
  
}
