public class TestToString{
  public static void main(String[] args){
    Dog d = new Dog();
    System.out.println("d :" + d.toString()); //the method toString() inherit from Object. look above
  }
}
// class Dog{
//
// }
class Dog extends Object{
  public String toString(){
    return "calvin";
  }

}
