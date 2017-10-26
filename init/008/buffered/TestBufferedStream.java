import java.io.*;
public class TestBufferedStream{
	public static void main(String args[]){
		try{
      BufferedWriter bw =
        new BufferedWriter(new FileWriter("e:\\java\\init\\008\\buffered\\Circle.dat"));
      BufferedReader br =
        new BufferedReader(new FileReader("e:\\java\\init\\008\\buffered\\CircleTest.java"));
      String s = null;
      for(int i=0;i<=100;i++){
        s = String.valueOf(Math.random());
        bw.write(s);
        bw.newLine();
      }
      bw.flush();
      while((s=br.readLine())!=null){
        System.out.println(s);
      }
      bw.close();
      br.close();
    }catch(IOException e){
      e.printStackTrace();
    }
  }
}
