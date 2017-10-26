
public class Animal{
	private String name;
	private int id;
	public Animal(String myName, int myid){
		name = myName;
		id = myid;
	}

	public void eat(){
		System.outprintln(name+"eating");
	}
	public void sleep(){
		System.outprintln(name+"sleeping");
	}
	public void introduct(){
		System.outprintln("hello everyone "+id+ " NO. "+name+".");
	
	}
}
public class Penguin extend Animal{
	public Penguin(String myName, int myid){
		super(myName, myid);
	}
}
public class Mouse extend Animal{
	public Mouse(String myName, int myid){
		super(myName, myid);
	}
}




