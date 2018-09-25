 class Parent{
   protected void print(String s){
     System.out.println(s);
   }
   Parent(){print("parent");}
   public void fun(){
     print("Parent.fun");
   }
 }

 class Child extends Parent{
   Child(){print("child");}
   public void fun(){
     print("child.func");
   }
   public static void main(String arg[]){
     Child sub = new Child();
     sub.fun();
   }
 }
