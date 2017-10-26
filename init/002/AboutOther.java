public class AboutOther{
  public static void main(String[] args){
    int skip = 4;
    for(int i =1; i<=5; i++){
      if(i == skip) continue;
      System.out.println("i : "+i);
    }
  }
}
