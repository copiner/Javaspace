import java.io.*;

public class TestData1 {
  public static void main(String args[]) throws IOException{
      OutputStream out=new FileOutputStream("e:\\test.txt");
      //缓冲流
      BufferedOutputStream buf=new BufferedOutputStream(out);
      //数据输出流
      DataOutputStream dos=new DataOutputStream(buf);
      //数据输出
      dos.writeInt(18);//写入int
      dos.writeUTF("好好学,天天向上");//写入String
      dos.writeFloat(3.1415f);//写入float
      //关闭流
      dos.close();
      buf.close();
      out.close();
  }
}
