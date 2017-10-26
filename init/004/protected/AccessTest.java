//private default protected public
class Access{
  private int i = 0;
  int j = 0;  //default
  protected int k = 0;
  public int m = 0;
}
class AAccess{
  public void m(){
    Access a = new Access();
    //System.out.println(a.i);
    System.out.println(a.j);
  }
}
