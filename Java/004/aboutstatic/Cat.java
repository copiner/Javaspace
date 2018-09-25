public class Cat{
  private static int sid = 0;//静态变量存放在数据区data segment,只有一份，属于类
  private String name;
  int id;
  Cat(String name){
    this.name = name;
    id = sid++;
  }
  public void info(){
    System.out.println("name : " + name +"No. : "+id );
  }

  public static void main(String arg[]){
    Cat.sid = 100; //静态变量用类名访问
    Cat mi = new Cat("mi");//字符串常量也存放数据区data segment
    Cat pi = new Cat("pi");
    mi.info();
    pi.info();
  }
}
