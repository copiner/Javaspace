import java.net.*;
import java.io.*;

public class TCPClient {
  public static void main(String args[]) throws Exception{
    Socket s = new Socket("127.0.0.1", 6543);
    OutputStream os = s.getOutputStream();
    DataOutputStream dos = new DataOutputStream(os);
    dos.writeUTF("Anna");
    dos.flush();
    dos.close();
    s.close();
  }
}
