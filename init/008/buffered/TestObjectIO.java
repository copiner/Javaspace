import java.io.*;

public class TestObjectIO{
  public static void main(String[] args) throws Exception{
    T t = new T();
    t.k = 8;
    FileOutputStream fos =
      new FileOutputStream("e:\\Javaspace\\init\\008\\objectio.log");
    ObjectOutputStream oos = new ObjectOutputStream(fos);
    oos.writeObject(t);
    oos.flush();
    oos.close();

    FileInputStream fis =
      new FileInputStream("e:\\Javaspace\\init\\008\\objectio.log");
    ObjectInputStream ois = new ObjectInputStream(fis);
    T tReaded = (T)ois.readObject();
    System.out.println(tReaded.i+" "+tReaded.j+" "+tReaded.d+" "+tReaded.k);
  }
}

class T implements Serializable{
  int i = 10;
  int j = 9;
  double d = 2.3;
  //int k = 21;
  transient int k = 21;
}
//Externalizable
