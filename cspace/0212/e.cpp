
#include<iostream>

class Point
{
private:
  int x, y;
public:
  Point(int a, int b)
  {
    x = a;
    y = b;
  }

  void MovePoint(int a, int b);
  {
    x = a;
    y = b;
    /*
      this->x = a;
      this->y = b;
     */
  }

  void print()
  {
    std::cout<<"x = "<<x<<" y = "<<y<<std::endl;
  }
};

int main()
{
  Point point1(10,10);
  /*
    void MovePoint(Point *this, int a, int b);
   */
  point1.MovePoint(2,2); 
  point1.print();
  return 0;
}
/*
  1.当对象point1调用MovePoint(2,2)函数时，即将point1对象的地址传给了this指针。
  
  2.MovePoint函数的原型事实上应该是void MovePoint(Point *this, int a, int b);第一个参数是指向该类对象的一个指针，我们在定义成员函数时没看见是因为这个参数在类中是隐含的。

   3.这样point1的地址传给了this，所以在MovePoint函数中便可以显式的写成：void MovePoint(int a, int b) { this->x = a; this->y = b;}
*/
