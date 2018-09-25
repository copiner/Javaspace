 public class ArrayInfo{
   public static void main(String[] args){
     int[] s;
     s = new int[5];
     for(int i = 0; i<5; i++){
       s[i] = i;
     }
     for(int i = 0; i<5; i++){
        System.out.println(s[i]);
     }
     for(int i = 0; i<args.length; i++){
        System.out.println(args[i]);
     }
   }
 }
