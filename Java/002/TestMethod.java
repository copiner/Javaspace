public class TestMethod{
  public static void main(String[] args){
    m();
    mm(5);
    mmm('3', 4);
    int i = mmmm(4, 6);
    System.out.println(i);

  }

  public static void m(){
    System.out.println("ok");
  }

  public static void mm(int i){
    if(i > 3)
      return;
    System.out.println(i);

  }

  public static void mmm(int i, int j){//ascii
    System.out.println(i + j);
  }

  public static int mmmm(int i, int j){
    return i > j ? i : j;
  }
}
