public class NumSort{
  public static void main(String[] args){
    int[] a = new int[args.length];
    for(int i = 0; i<args.length; i++){
      a[i] = Integer.parseInt(args[i]);
    }
    print(a);
    selecSort(a);
    print(a);
  }

  private static void selSort(int[] a){
    for(int i = 0; i <a.length; i++){
      for(int j = i+1; j<a.length; j++){
          if(a[j]<a[i]){
            int temp;
            temp = a[i];
            a[i] = a[j];
            a[j] = temp;
          }
      }
    }
  }
  private static void selecSort(int[] a){
    int x, temp;
    for(int i = 0; i <a.length; i++){
       x = i;
      for(int j = x+1; j<a.length; j++){
          if(a[j]<a[x]){
            x = j;
          }
      }
      if(x != i){
        temp = a[i];
        a[i] = a[x];
        a[x] = temp;
      }
    }
  }

  private static void print(int[] a){
    for(int i = 0; i<a.length; i++){
      System.out.print(a[i] + " ");
    }
    System.out.println();
  }
}
