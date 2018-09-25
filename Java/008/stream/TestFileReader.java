import java.io.*;

public class TestFileReader{
	public static void main(String args[]){
		FileReader fr = null;
		int c = 0;
		try{
			fr = new FileReader("e:\\java\\init\\008\\input\\linux.txt");
			int ln = 0;
			while((c = fr.read()) != -1){
				System.out.print((char)c);
			}
			fr.close();
		}catch(FileNotFoundException e){
			System.out.println("not found");
		} catch(IOException e){
			System.out.print("read err");
		}
	}
}
