import java.io.*;
//throwable
//error Exception

public class TestEx{
  public static void main(String[] args){
    int[] arr = {1, 2, 3};
    System.out.println(arr[2]);
    //1.............
    // try{
    //   System.out.println(2/0);
    // } catch (ArithmeticException ex){
    //   System.out.println("account an err");
    //   ex.printStackTrace();
    // }

    //2..........
    // TestEx te = new TestEx();
    // te.m(0);

    //3...
    // try{
    //   new TestEx().m(0);
    // } catch(ArithmeticException ex){
    //   System.out.println("ex");
    // }

    FileInputStream in = null;
    try{
      in = new FileInputStream("file.txt");
      int b;
      b = in.read();
      while(b != -1){
        System.out.println((char) b);
        b = in.read();
      }
    } catch (FileNotFoundException ex){
      ex.printStackTrace();
    } catch (IOException ex){
      System.out.println(ex.getMessage());
    } finally {
      try{
        in.close();
      } catch(IOException ex){
        ex.printStackTrace();
      }
    }

  }

  void m(int i) throws ArithmeticException{
    if(i==0){
      throw new ArithmeticException("matherror");
    }
  }

  void f() throws FileNotFoundException, IOException{
    FileNotFoundException in = new FileInputStream("file.txt");
    int b;
    b = in.read();
    while(b != -1){

    }
  }
}
