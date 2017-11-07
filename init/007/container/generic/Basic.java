import java.util.*;

class Box<T> {
    private T ob;

    public Box(T ob) {
        this.ob = ob;
    }

    public T getOb() {
        return ob;
    }

    public void showType() {
        System.out.println("reality T : " + ob.getClass().getName());
    }
}

public class Basic{
  public static void main(String args[]) {
      Box<Integer> intOb = new Box<Integer>(100);
      intOb.showType();
      System.out.println("value : " + intOb.getOb());
      
      System.out.println("--------------------------");

      Box<String> strOb = new Box<String>("Calvin");
      strOb.showType();
      System.out.println("value : " + strOb.getOb());
  }
}
