import java.io.*;

public class TestFileOutputStream{
  public static void main(String args[]){
    int b = 0;
    FileInputStream in = null;
    FileOutputStream out = null;
    try{
      in = new FileInputStream("e:\\java\\init\\008\\input\\linux.txt");
      out = new FileOutputStream("e:\\java\\init\\008\\input\\shell.sh");
      while((b=in.read())!= -1){
        out.write(b);
      }
      in.close();
      out.close();
    } catch (FileNotFoundException e){
      System.out.println("not found file");
      System.exit(-1);
    } catch(IOException e){
      System.out.println("write err");
      System.exit(-1);
    }
    System.out.println("coyped");

  }
}
