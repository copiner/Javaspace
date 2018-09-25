import java.io.*;
import java.net.*;

public class TalkServer{
  public static void main(String args[]){
    try{
      ServerSocket server = new ServerSocket(4600);
      Socket socket = server.accept();

      BufferedReader is = new BufferedReader(
        new InputStreamReader(socket.getInputStream()));
      PrintWriter os = new PrintWriter(socket.getOutputStream());
      BufferedReader sin = new BufferedReader(
        new InputStreamReader(System.in));
      System.out.println("Client : "+is.readLine());

      String line = null;
      line = sin.readLine();
      while(!line.equals("exit")){
        os.println(line);
        os.flush();
        System.out.println("Server : " + line);
        System.out.println("Client : " + is.readLine());
        line = sin.readLine();
      }
      is.close();
      os.close();
      socket.close();
      server.close();
      } catch (Exception e){
        System.out.println("error : "+e);
      }
  }
}
