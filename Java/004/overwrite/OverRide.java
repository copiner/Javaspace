class Person{
  private String name;
  private int age;
  public void setName(String name){ this.name = name; }
  public void setAge(int age){ this.age = age; }
  public String getName(){ return name; }
  public int getAge(){ return age; }
  public String getInfo(){
    return "name : "+name+" age : "+age;
  }

}

class Student extends Person{
  private String school;
  public String getSchool(){ return school; }
  public void setSchool(String school){
    this.school = school;
  }
  public String getInfo(){//override
    return "name : "+getName()+ " age："+getAge()+" school ："+ school;
  }
}
public class OverRide{
  public static void main(String arg[]){
    Person person = new Person();
    Student student = new Student();
    person.setName("francis");
    person.setAge(23);
    student.setName("calvin");
    student.setAge(25);
    student.setSchool("Harbin"); 
    System.out.println(person.getInfo());
    System.out.println(student.getInfo());
  }
}
