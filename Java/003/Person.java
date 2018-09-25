public class Person{
  int id;
  int age = 20;

  Person(int _id, int _age){
    id = _id;
    age = _age;
  }
//默认会有一个构造函数Person(){},如果自己定义了构造函数，系统就不会再创建构造函数了
  public static void main(String[] args){
     Person parker = new Person(114215, 26);
     Point p = new Point();
     System.out.println(parker.id);
     System.out.println(p.x);
  }
}

class Point{
  int x = 50;
  int y = 50;
}
