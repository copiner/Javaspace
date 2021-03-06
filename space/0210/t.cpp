/*
 friends
*/
#include <iostream>
#include <string>

class Lovers
{
public:
  Lovers(std::string tname);

  void kiss(Lovers *lover);
  void squabble(Lovers *lover, std::string sth);

protected:
  std::string name;

  friend class Others;
};

class Boyfriend : public Lovers
{
public:
  Boyfriend(std::string tname);
};

class Girlfriend : public Lovers
{
public:
  Girlfriend(std::string tname);
};


class Others
{
public:
  Others(std::string tname);
  
  void kiss(Lovers *lover);

protected:
  std::string name;
};


Lovers::Lovers(std::string tname)
{
  name = tname;
}

void Lovers::kiss(Lovers *lover)
{
  std::cout << name << " lover kiss.."<<lover->name<<std::endl;
}

void Lovers::squabble(Lovers *lover, std::string sth)
{
  std::cout<<"squabble.."<<lover->name<<" result of..."<<sth<<std::endl;
}


Boyfriend::Boyfriend(std::string tname) : Lovers(tname)
{

}

Girlfriend::Girlfriend(std::string tname):Lovers(tname)
{

}

Others::Others(std::string tname)
{
  name = tname;
}

void Others::kiss(Lovers *lover)
{
  std::cout<<name<<" others kissing..."<<lover->name<<std::endl;
}

int main()
{
  Boyfriend boy("B");
  Girlfriend girl("G");

  Others others("O");

  girl.kiss(&boy);
  girl.squabble(&boy,"wash");

  std::cout<<"angry other...\n"<<std::endl;
  others.kiss(&girl);

  return 0;
}
