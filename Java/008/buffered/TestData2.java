import java.io.*;

public class TestData2 {
  public static void main(String args[]) throws IOException{
        InputStream in=new FileInputStream("e:\\test.txt");
        //缓冲流
        BufferedInputStream buf=new BufferedInputStream(in);
        //数据输出流
        DataInputStream ds=new DataInputStream(buf);
        //数据读取
        int age=ds.readInt();
        String data=ds.readUTF();
        float ok=ds.readFloat();

        System.out.println("整数为："+age+"\n"+"字符串为："+data+"\n"+"浮点数为："+ok);
        //关闭流
        ds.close();
        buf.close();
        in.close();

      }
}
