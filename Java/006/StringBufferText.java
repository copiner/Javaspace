public class StringBufferText{
  public static void main(String[] args){
    String s = "Calvin";
    char[] ar = {'a','b','c'};
    StringBuffer sb1 = new StringBuffer(s);
    sb1.append('/').append("Anna")
       .append('/').append("Tim");
    System.out.println(sb1);
    StringBuffer sb2 = new StringBuffer("num");
    for(int i = 0; i<=9; i++){
      sb2.append(i);
    }
    System.out.println(sb2);
    sb2.delete(8, sb2.length()).insert(0, ar);
    System.out.println(sb2);
    System.out.println(sb2.reverse());
  }
}
