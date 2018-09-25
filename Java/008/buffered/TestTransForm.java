import java.io.*;
public class TestTransForm{
  public static void main(String args[]){
    try{
      OutputStreamWriter osw = new OutputStreamWriter(
        new FileOutputStream("e:\\Javaspace\\init\\008\\buffered\\char.txt"));
      osw.write("Miscrosoft");
      System.out.println(osw.getEncoding());
      osw.close();
      osw = new OutputStreamWriter(
        new FileOutputStream("e:\\Javaspace\\init\\008\\buffered\\char.txt",true),"ISO8859_1");
      osw.write("MiscrosoftApple");
      System.out.println(osw.getEncoding());
      osw.close();
    } catch(IOException e){
      e.printStackTrace();
    }
  }
}
