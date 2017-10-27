import java.util.*;
public class TestArgsWords{
  //private static final Integer ONE = new Integer(1);
  private static final int ONE = 1;
  public static void main(String args[]){
    Map m = new HashMap();
    for(int i = 0; i<args.length; i++){
      //Integer freq = (Integer)m.get(args[i]);
      int freq = (Integer)m.get(args[i]) == null ? 0 : (Integer)m.get(args[i]);
      m.put(args[i], (freq == 0 ? ONE : freq + 1));
    }
    System.out.println(m.size() + " Calvin is a girl");
    System.out.println(m);
  }
}
