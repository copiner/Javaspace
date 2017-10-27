public class TestYield{
  public static void main(String args[]){
    MyThread2 t1 = new MyThread2("t1");
    MyThread2 t2 = new MyThread2("t2");
    t1.start();
    t2.start();
  }
}

class MyThread2 extends Thread{
  MyThread2(String s){super(s);}
  public void run(){
    for(int i=0; i<=100; i++){
      System.out.println(getName() + " is here :" + i);
      if(i%10==0){
        yield();
      }
    }
  }
}
