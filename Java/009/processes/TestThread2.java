public class TestThread2{
  public static void main(String args[]){
    Runner2 r = new Runner2();
    Thread t = new Thread(r);
    t.start();
  }
}

class Runner2 implements Runnable{
  public void run(){
    for(int i=0; i<30; i++){
      if(i%10==0 && i != 0){
        try{
          Thread.sleep(2000);
        } catch (InterruptedException e){}
      }
      System.out.println("No. : " + i);
    }
  }
}
