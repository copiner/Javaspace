public class TestArgs{
  public static void main(String[] args){
    if(args.length<3){
      System.out.print("Usage: java TestArgs parms1 +-x/ parms2");
      System.exit(-1);
    }
    double d1 = Double.parseDouble(args[0]);
    double d2 = Double.parseDouble(args[2]);
    double d = 0;
    if(args[1].equals("+")){
      d = d1 + d2;
    } else if(args[1].equals("-")){
      d = d1 - d2;
    } else if(args[1].equals("x")){
      d = d1 * d2;
    } else if(args[1].equals("/")){
      d = d1 / d2;
    } else{
      System.out.println("sth err");
    }
    System.out.println(d);

  }
}
