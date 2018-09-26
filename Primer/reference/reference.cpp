#include<iostream>
using namespace std;

void r(int &a){//reference c++编译器在编译过程中 使用常量指针 作为引用的内部实现
  a = 5;
}

void p(int *const a){//pointer
  *a = 5;
}
int main(){
  int i = 10;
  
}

//pointer
//A point holds the address of another object,allowing for the indirect manipulation of that object Typical uses of pointers are the creation of linked data structures such as trees and lists, the management of objects dynamically allocated during program execution, and as a function parameter type primarily for passing in arrays and large class objects.

