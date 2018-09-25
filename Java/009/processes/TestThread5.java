public class TestThread5{
  public static void main(String args[]){
    Thread t = new Runner5();
    t.start();

    for(int i=0; i<50; i++){
      System.out.println("main thread : " + i);
    }
  }
}

class Runner5 extends Thread{
  public void run(){
    System.out.println(Thread.currentThread().isAlive());
    for(int i=0; i<50; i++){
      System.out.println("sub thread : " + i);
    }
  }
}
