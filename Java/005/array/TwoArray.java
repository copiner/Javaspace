public class TwoArray{
  public static void main(String[] args){
    // int a[][] = {{1,3},{3,4,5,6}, {7,8,9}};
    // int a[][] = new int[3][];
    // a[0] = new int[2];
    // a[1] = new int[4];
    // a[2] = new int[3];
    int a[][] = {{1,3},{3,4,5,6}, {7,8,9}};
    for(int i = 0; i<a.length; i++){
      for(int j = 0; j<a[i].length; j++){
        System.out.print(i + "_" + j + ":" + a[i][j]+ " ");
      }
    }
  }
}
