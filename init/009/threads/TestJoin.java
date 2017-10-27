public class TestJoin{
  public static void main(String args[]){
    MyThread1 t1 = new MyThread1("t1");
    t1.start();
    try{
      t1.join();//combined
    } catch(InterruptedException e){}

    for(int i=1; i<=10; i++){
      System.out.println("main thread");
    }
  }
}

class MyThread1 extends Thread{
  MyThread1(String s){
    super(s);
  }
  public void run(){
    for(int i=0; i<=10; i++){
      System.out.println("Am " + getName());
      try{
        sleep(1000);
      } catch (InterruptedException e){
        return;
      }
    }
  }
}
