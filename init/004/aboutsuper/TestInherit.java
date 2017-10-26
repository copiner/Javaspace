class FatherClass{
  public int value;
  public void f(){
    value = 100;
    System.out.println("FatherClass.value : "+value);
  }
}

class ChildClass extends FatherClass{
  public int value;
  public void f(){
    super.f();//this指向自身， super指向父对象
    value = 200;
    System.out.println("ChildClass.value : "+value);
    System.out.println(value);
    System.println(super.value);
  }
}
public class TestInherit{
  public static void main(String[] args){
    ChildClass cc = new ChildClass();
    cc.f();
  }
}
