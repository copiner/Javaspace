class Animal{
  private String name;
  Animal(String name){this.name = name;}
  public void scream(){
    System.out.println("scream...");
  }
}
class Cat extends Animal{
  private String eyesColor;
  Cat(String n, String c){
    super(n);
    eyesColor = c;
  }
  public void scream(){
    System.out.println("cat screaming...");
  }
}
class Dog extends Animal{
  private String furColor;
  Dog(String n, String c){
    super(n);
    furColor = c;
  }
  public void scream(){
    System.out.println("dog screaming...");
  }
}
class Bird extends Animal{
  Bird(){
    super("bird");
  }
  public void scream(){
    System.out.println("bird sceam...");
  }
}
 class Girl{
   private String name;
   private Animal pet;
   Girl(String name, Animal pet){
     this.name = name;
     this.pet = pet;
   }
   public void girlScream(){
     pet.scream();
   }
 }
 public class Poly{
   public static void main(String args[]){
     Cat c = new Cat("catname", "blue");
     Dog d = new Dog("dogname", "black");

     Bird b = new Bird();

     Girl g1 = new Girl("g1", c);
     Girl g2 = new Girl("g2", d);

     Girl g3 = new Girl("g3", b);

     g1.girlScream();
     g2.girlScream();

     g3.girlScream();
   }
 }
