pulic class TestFinal{
  public static void main(String[] args){
    TF t = new TF();
    //t.i = 9;
  }
}
class TF{
  final int i = 0;//final
  public void m(final int j){
    //j = 9;
  }
  public final void f(){

  }
}

class TFF extends TF{
  public void f(){

  }
}
