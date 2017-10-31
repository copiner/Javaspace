
import java.net.*;
import java.io.*;

public class TestUDPClient1{
  public static void main(String args[]){
    try{
      long n = 10000L;
      ByteArrayOutputStream baos = new ByteArrayOutputStream();
      DataOutputStream dos = new DataOutputStream(baos);
      dos.writeLong(n);
      byte buf[] = baos.toByteArray();
      System.out.println(buf.length);

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
