import java.util.Arrays;

public class StringInfo{
  public static void main(String[] args){
    String s1 = "hello";
    String s2 = "world";
    String s3 = "hello";
    System.out.println(s1 == s3);//true

    String s5 = new String("hello");
    String s6 = new String("hello");
    System.out.println(s5 == s6);//false
    System.out.println(s5.equals(s6));//true

    char c[] = {'s', 'u', 'n',' ', 'j', 'a', 'v','a'};
    String s4 = new String(c);
    String s7 = new String(c, 4, 4);
    System.out.println(s4);
    System.out.println(s7);

    int j = 123456;
    String num = String.valueOf(j);
    System.out.println(num + " : "+ num.length());
    String k = "Calvin,Anna,Francis,Rose";
    String kstr[] = k.split(",");
    System.out.println(Arrays.toString(kstr));
  }
}
