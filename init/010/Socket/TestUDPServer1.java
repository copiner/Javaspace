import java.net.*;
import java.io.*;

public class TestUDPServer1{
  public static void main(String args[]){
    try{
      byte buf[] = new byte[1024];
      DatagramPacket dp = new DatagramPacket(buf, buf.length);
      DatagramSocket ds = new DatagramSocket(4553);
      while(true){
        ds.receive(dp);
        ByteArrayInputStream bais = new ByteArrayInputStream(buf);
        DataInputStream dis = new DataInputStream(bais);
        System.out.println(dis.readLong());
      }
    } catch(Exception e){
      e.printStackTrace();
    }
  }
}
