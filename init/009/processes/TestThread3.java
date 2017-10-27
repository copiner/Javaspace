public class TestThread3{
  public static void main(String args[]){
    Runner3 r = new Runner3();
    Thread t = new Thread(r);
    t.start();
    for(int i=0; i<100; i++){
      if(i%10==0 && i>0){
        System.out.println("in main thread i : " + i);
      }
    }

    System.out.println("main thread over");
    r.shutDown();
  }
}

class Runner3 implements Runnable{
  private boolean flag=true;

  public void run(){
      int i = 0;
      while(flag==true){
        System.out.println(" "+ i++);
      }
    }


  public void shutDown(){
    flag = false;
  }
}
