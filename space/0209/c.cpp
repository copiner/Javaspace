/*
  constructor destructor
*/

#include <iostream>
#include <string>
#include <fstream>

class StoreQuote
{
public:
  std::string quote, author;
  std::ofstream fileOutput;

  StoreQuote();
  ~StoreQuote();

  void inputQuote();
  void inputAuthor();
  bool write();
};

StoreQuote::StoreQuote()
{
  fileOutput.open("text",std::ios::app);
}

StoreQuote::~StoreQuote()
{
  fileOutput.close();
}


void StoreQuote::inputQuote()
{
  std::getline(std::cin, quote);
}

void StoreQuote::inputAuthor()
{
  std::getline(std::cin, author);
}

bool StoreQuote::write()
{
  if(fileOutput.is_open()){

    fileOutput << quote <<"|"<<author<<"\n";
    return true;

  } else {
    
    return false;
  }

}


int main()
{
  StoreQuote quote;

  std::cout<<"input quote: \n";
  quote.inputQuote();

  std::cout<<"input author: \n";
  quote.inputAuthor();

  if(quote.write()){
      
      std::cout<<"write suc\n";

  } else {

      std::cout<<"write err\n";

  }
  return 0;
}
