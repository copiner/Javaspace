
public class Switch{
	public static void main(String[] args){
		String name = "zhangsan";
		String sex = "male";
		switch (sex){
			case "male" :
				System.out.println(name+"is"+sex);
				break;
			case "female" :
				System.out.println(name+"is"+sex);
				break;
			default:
				System.out.println(name);
				break;
			}
	}
}
