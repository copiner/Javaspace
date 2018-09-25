import java.net.*;

public class TestUDPServer{
  public static void main(String args[]){
    try{
      byte buf[] = new byte[1024];
      DatagramPacket dp = new DatagramPacket(buf, buf.length);
      DatagramSocket ds = new DatagramSocket(4553);
      while(true){
        ds.receive(dp);
        System.out.println(new String(buf,0,dp.getLength()));
      }
    } catch(Exception e){
      e.printStackTrace();
    }
  }
}
