import java.io.*;
import java.net.*;

public class TalkClient{
  public static void main(String args[]){
    try{
      Socket socket = new Socket("127.0.0.1", 4600);

      BufferedReader sin = new BufferedReader(
        new InputStreamReader(System.in));
      PrintWriter os = new PrintWriter(socket.getOutputStream());
      BufferedReader is = new BufferedReader(
        new InputStreamReader(socket.getInputStream()));

      String readLine = null;
      readLine = sin.readLine();
      while(!readLine.equals("exit")){
        os.println(readLine);
        os.flush();
        System.out.println("Client : " + readLine);
        System.out.println("Server : " + is.readLine());
        readLine = sin.readLine();
      }

      os.close();
      is.close();
      socket.close();
    } catch (Exception e){
      System.out.println("error : "+e);
    }
  }
}
