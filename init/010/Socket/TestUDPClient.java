import java.net.*;
import java.io.*;

public class TestUDPClient{
  public static void main(String args[]){
    try{
      byte buf[] = (new String("Anna")).getBytes();
      DatagramPacket dp = new DatagramPacket(
        buf, buf.length, new InetSocketAddress("127.0.0.1",4553));
      DatagramSocket ds = new DatagramSocket(8000);

      ds.send(dp);
      ds.close();

    } catch(Exception e){
      e.printStackTrace();
    }
  }
}
