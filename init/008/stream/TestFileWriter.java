import java.io.*;

public class TestFileWriter{
	public static void main(String args[]){
		FileWriter fw = null;
		try{
			fw = new FileWriter("e:\\java\\init\\008\\input\\unicode.dat");
			for(int c=0; c<=50000; c++){
        fw.write(c);
      }
			fw.close();
		}catch(IOException e){
      e.printStackTrace();
			System.out.print("write err");
      System.exit(-1);
		}
	}
}
