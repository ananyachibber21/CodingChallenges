import java.util.*;
public class HasNext
{
	public static void main(String args[]){
		Scanner scan = new Scanner(System.in);   
        System.out.println("Enter: "); 
        int i = 1; 
        while (scan.hasNext()){  
        	String ch = scan.nextLine();
            System.out.println(i +" "+ ch);  
            i++;
        }  
        scan.close();
	}
}
