class SuperClass{
  private int n;

  SuperClass(){
    System.out.println("SuperClass()");
  }

  SuperClass(int n){
    System.out.println("SuperClass(" + n + ")");
    this.n = n;
  }
}

class SubClass extends SuperClass{
  private int n;
  SubClass(){
    super(300);//调用子类构造函数，必须要先调用父类构造函数
    System.out.println("SubClass()");
  }

  SubClass(int n){
    System.out.println("SubClass(" + n + ")");
    this.n = n;
  }
}

public class SuperThis{
  public static void main(String arg[]){
    SubClass sc1 = new SubClass();//调用子类构造函数，必须要先调用父类构造函数
    SubClass sc2 = new SubClass(400);
  }
}
