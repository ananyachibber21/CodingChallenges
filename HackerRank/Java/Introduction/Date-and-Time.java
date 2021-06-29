import java.util.Scanner;
import java.time.LocalDate;

class DateTime{
	public static void main(String[] args){
		Scanner sc = new Scanner(System.in);
		int month= sc.nextInt();
		int day= sc.nextInt();
		int year= sc.nextInt();
		LocalDate date = LocalDate.of(year, month, day);
		System.out.println(date.getDayOfWeek());
    }	
}
