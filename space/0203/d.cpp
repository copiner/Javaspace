#include <fstream>
#include <iostream>

using namespace std;

int main()
{
  fstream fp("text",ios::in | ios::out);
  if(!fp){
    cerr << "open file fail!"<<endl;
    return 0;
  }

  fp << "wrqlo";

  static char str[100];

  fp.seekg(ios::beg);//ios::beg begin , ios::end end
  fp >> str;
  cout << str <<endl;

  fp.close();

  return 0;
}
