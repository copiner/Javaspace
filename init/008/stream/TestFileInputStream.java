import java.io.*;

public class TestFileInputStream{
  public static void main(String args[]){
    int b = 0;
    FileInputStream in = null;
    try{
      in = new FileInputStream("e:\\java\\init\\008\\input\\linux.txt");
    } catch (FileNotFoundException e){
      System.out.println("not found file");
      System.exit(-1);
    }

    try{
      long num = 0;
      while((b=in.read())!= -1){
        System.out.print((char)b);
        num++;
      }
      in.close();
      System.out.println();
      System.out.println("total read " + num +" bytes");
    } catch(IOException e1){
      System.out.println("read err");
      System.exit(-1);
    }
  }
}
