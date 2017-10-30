
public class ProducerConsumer{
  public static void main(String args[]){
    SyncStack ss = new SyncStack();
    Producer p = new Producer(ss);
    Consumer c = new Consumer(ss);
    new Thread(p).start();

    // new Thread(p).start();
    // new Thread(p).start();

    new Thread(c).start();
  }
}

class WowoTou{
  int id;
  WowoTou(int d){
    this.id = d;
  }
  public String toString(){
    return "WowoTou : " + id;
  }
}

class SyncStack{
  int index = 0;
  WowoTou arrWwT[] = new WowoTou[6];

  public synchronized void push(WowoTou wwt){
    while(index == arrWwT.length){
      try{
        this.wait();
      } catch (InterruptedException e){
        e.printStackTrace();
      }
    }
    this.notify();
    //this.notifyAll();
    arrWwT[index] = wwt;
    index++;
  }

  public synchronized WowoTou pop(){
    while(index == 0){
      try{
        this.wait();
      } catch (InterruptedException e){
        e.printStackTrace();
      }
    }
    this.notify();
    //this.notifyAll();
    index--;
    return arrWwT[index];
  }
}

class Producer implements Runnable{
  SyncStack ss = null;
  Producer(SyncStack ss){
    this.ss = ss;
  }

  public void run(){
    for(int i=0; i<20; i++){
      WowoTou wwt = new WowoTou(i);
      ss.push(wwt);
      System.out.println("Produce : "+wwt);
      try{
        Thread.sleep((int)(Math.random()*500));
      } catch (InterruptedException e){
        e.printStackTrace();
      }
    }
  }
}

class Consumer implements Runnable{
  SyncStack ss = null;
  Consumer(SyncStack ss){
    this.ss = ss;
  }

  public void run(){
    for(int i=0; i<20; i++){
      WowoTou wwt = ss.pop();
      System.out.println("Consume : "+ wwt);
      try{
        Thread.sleep((int)(Math.random()*1000));
      } catch(InterruptedException e){
        e.printStackTrace();
      }
    }
  }
}
