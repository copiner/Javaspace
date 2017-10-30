import java.util.*;
import java.io.*;

public class TestPrintStream2{
  public static void main(String[] args){
    String s = null;
    BufferedReader br = new BufferedReader(
      new InputStreamReader(System.in));
    try{
      FileWriter fw = new FileWriter("e:\\Javaspace\\init\\008\\test.log", true);
      PrintWriter log = new PrintWriter(fw);
      while((s=br.readLine())!=null){
        if(s.equalsIgnoreCase("exit")) break;
        System.out.println(s.toUpperCase());
        log.println("-----------");
        log.println(s.toUpperCase());
        log.flush();
      }
        Date now = new Date();
        log.println("----"+now+"-------");
        log.flush();
        log.close();
    } catch(IOException e){
      e.printStackTrace();
    }
  }
}
