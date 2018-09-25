public class StringMethod{
  public static void main(String[] args){
	  String s1 = "calvin", s2 = "anna";
	  String s3 = "Calvin";
	  System.out.println(s1.charAt(1));
	  System.out.println(s1.length());
	  System.out.println(s1.indexOf("vin"));
	  System.out.println(s1.indexOf("ann"));
	  System.out.println(s1.equals(s3));
	  System.out.println(s1.equalsIgnoreCase(s3));

	  String s4 = "francis is a account";
	  String sr = s4.replace("francis","cuuk");
	  System.out.println(sr);

	  String s5 = "Welcome to The World";
	  String s6 = " programe process ";
	  System.out.println(s5.startsWith("Welcome"));
	  System.out.println(s5.endsWith("World"));
	  
	  String s5L = s5.toLowerCase();
	  String s5U = s5.toUpperCase();
	  System.out.println(s5L);
	  System.out.println(s5U);

	  String subs = s5.substring(11);
	  System.out.println(subs);
	  
	  String st = s6.trim();
	  System.out.println(st);
  }
 

}
