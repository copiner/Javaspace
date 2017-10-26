public class TestString{
	public static void main(String[] args){
		String s = "ASffkjkk%cco_haH&pxcvbMN";
		int lower = 0, upper = 0, other = 0;
		for(int i = 0; i<s.length();i++){
			char c = s.charAt(i);
			if(c >= "a" && c<= "z"){
				lower ++;
			}else if(c >= "A" && c <="Z"){
		        	upper ++;
			}else{
			        other ++;	
			}
		}
		System.out.println(lower+" "+upper+""+other);
	}
}

