public class TestThread1{
  public static void main(String args[]){
    Runner1 r = new Runner1();
    Thread t1 = new Thread(r);
    Thread t2 = new Thread(r);
    t1.start();
    t2.start();

  }
}

class Runner1 implements Runnable{
  public void run(){
    for(int i=0; i<30; i++){
      System.out.println("No. : " + i);
    }
  }
}
