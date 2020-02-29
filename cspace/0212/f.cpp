/*
  static
  堆，栈，自由存储区，全局/静态储存区，常量存储区
*/
#include <iostream>
#include <string>

class Pet
{
public:
  Pet(std::string tname);

  ~Pet();
  
  static int getCount();//static method

protected:
  std::string name;

private:
  static int count;//static prop

};

class Dog : public Pet
{
public:
  Dog(std::string tname);
};

class Cat : public Pet
{
public:
  Cat(std::string tname);
};

int Pet::count = 0;//init

Pet::Pet(std::string tname)
{
  name = tname;
  count++;

  std::cout <<"one pet born "<<name<<"\n";
}

Pet::~Pet()
{
  count--;
  std::cout<<"one pet "<<name<<" died\n";

}

int Pet::getCount()
{
  return count;
}

Dog::Dog(std::string tname):Pet(tname)
{
  /*
      当调用Dog()时（以tname作为输入参数），
      Pet()也将被调用（tname输入参数也会传递给它），
      赋值动作将实际发生在Pet()方法里
   */
  std::cout<<"Dog constructor: "<<name<<std::endl;

  std::cout<<"this: "<<this<<std::endl;
}

Cat::Cat(std::string tname):Pet(tname)
{
    std::cout<<"Cat constructor: "<<name<<std::endl;
}


int main()
{
  Dog dog("kiki");

  Cat cat("lulu");
  std::cout<<"dog: "<<&dog<<"\n\n";
  std::cout << "born "<<Pet::getCount()<<" pet\n\n";

  {//scope

    Dog dog2("lili");
    Cat cat2("lyly");
    std::cout << "born now "<<Pet::getCount()<<" pet\n\n";
  }

  std::cout << "born end "<<Pet::getCount()<<" pet\n\n";
  return 0;
}
