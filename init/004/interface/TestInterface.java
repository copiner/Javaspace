interface Singer{
  public static final int id = 1;
  public void sing();
  public void sleep();
}
interface Painter{
  public void paint();
  public void eat();
}
class Student implements Singer{
  private String name;
  Student(String name){
    this.name = name;
  }
  public void study(){
    System.out.println("studying");
  }
  public String getName(){
    return name;
  }
  public void sing(){
    System.out.println("student is singing");
  }
  public void sleep(){
    System.out.println("student is sleeping");
  }
}
class Teacher implements Singer, Painter{
  private String name;
  public String getName(){
    return name;
  }
  Teacher(String name){
    this.name = name;
  }
  public void teach(){
    System.out.println("teaching");
  }
  public void sing(){
    System.out.println("teachering is singing");
  }
  public void sleep(){
    System.out.println("teaching is sleeping");
  }
  public void paint(){
    System.out.println("teaching is painting");
  }
  public void eat(){
    System.out.println("teaching is eating");
  }
}
public class TestInterface{
  public static void main(String args[]){
    Singer s1 = new Student("lee");
    s1.sing();
    s1.sleep();
    //s1.study();
    Singer s2 = new Teacher("Calvin");
    s2.sing();
    s2.sleep();
    //s2.teach();
    Painter p1 = (Painter)s2;
    p1.paint();
    p1.eat();
    //p1.sing();
  }
}
