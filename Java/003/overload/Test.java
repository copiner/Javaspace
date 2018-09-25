public class Test{
  void max(int a, int b){
    System.out.println(a > b ? a : a + b);
  }

  void max(float a, float b){
    System.out.println(a > b ? a : b);
  }

  public static void main(String[] args){
    Test t = new Test();
    t.max(3, 4);
  }
}
