class Animal{
  public String name;
  Animal(String name){
    this.name = name;
  }
}
class Cat extends Animal{
  public String eyescolor;
  Cat(String n, String c){
    super(n);
    eyescolor = c;
  }
}
class Dog extends Animal{
  public String furColor;
  Dog(String n, String c){
    super(n);
    furColor = c;
  }
}
public class TestCast{
  public static void main(String args[]){
    Animal a = new Animal("name");
    Cat c = new Cat("catname", "blue");
    Dog d = new Dog("dogname", "black");

    System.out.println(a instanceof Animal); //true
    System.out.println(c instanceof Animal);
    System.out.println(d instanceof Animal);
    //System.out.println(a instanceof Cat);



    a = new Dog("dahuang", "yellow");
    System.out.println(a.name);
    //System.out.println(a.furColor);
    System.out.println(a instanceof Animal);
    System.out.println(a instanceof Dog);

    Dog d1 = (Dog)a;//强制转换
    System.out.println(d1.furColor);
  }
}
