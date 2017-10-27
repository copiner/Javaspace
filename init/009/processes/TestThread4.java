public class TestThread4{
  public static void main(String args[]){
    Runner4 r = new Runner4();
    Thread t = new Thread(r);
    t.start();

    try{
      t.join();
    }catch(InterruptedException e){}

    for(int i=0; i<50; i++){
      System.out.println("main thread : " + i);
    }
  }
}

class Runner4 implements Runnable{
  public void run(){
    for(int i=0; i<50; i++){
      System.out.println("sub thread : " + i);
    }
  }
}
