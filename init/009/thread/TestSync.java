public class TestSync implements Runnable{
  Timer timer = new Timer();
  public static void main(String args[]){
    TestSync t = new TestSync();
    Thread t1 = new Thread(t);
    Thread t2 = new Thread(t);

    t1.setName("t1");
    t2.setName("t2");
    t1.start();
    t2.start();
  }
  public void run(){
    timer.add(Thread.currentThread().getName());
  }
}

class Timer{
  private static int num = 0;
  public void add(String name){
    //synchronized (this){
        num++;
        try{
          Thread.sleep(1);
        }catch(InterruptedException e){}

        System.out.println(name+" is the "+num+" user who are using the thread");
      }
  //}
}

//or

// class Timer{
//   private static int num = 0;
//   public synchronized void add(String name){
//         num++;
//         try{
//           Thread.sleep(1);
//         }catch(InterruptedException e){}
//
//         System.out.println(name+" is the "+num+" user who are using the thread");
//       }
// }
