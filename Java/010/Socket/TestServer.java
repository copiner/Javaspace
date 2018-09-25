import java.net.*;
import java.io.*;

public class TestServer{
  public static void main(String args[]){
    try{
      ServerSocket s = new ServerSocket(8000);
      while(true){
        Socket s1 = s.accept();
        OutputStream os = s1.getOutputStream();
        DataOutputStream dos = new DataOutputStream(os);
        dos.writeUTF("Hello, "+s1.getInetAddress()+
          " port : "+s1.getPort()+" see you later");
        dos.close();
        s1.close();
      }
    }catch(IOException e){
      e.printStackTrace();
      System.out.println("sth err"+e);
    }
  }
}
