public class Fibonacci{
  public static void main(String[] args){
    System.out.println(fib(5));
  }
  public static long fib(int index){
    if(index < 1){
      System.out.println("error parameter");
      return -1;
    }
    if(index == 1 || index== 2){
      return 1;
    }

    long f1 = 1L;
    long f2 = 1L;
    long f = 0;

    for(int i = 0; i<index-2; i++){
      f = f1 + f2;
      f1 = f2;
      f2 = f;
    }
    return f;
  }
}
