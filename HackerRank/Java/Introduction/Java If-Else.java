import java.util.*;
public class IfElse
{
    public static void main(String args[])
    {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        sc.close(); 
        String var;

        if(n%2==1){
            var="Weird";
        }
        else{
            if(n>=2 && n<=5){
                var="Not Weird";
            }
            else if(n>=6 && n<=20){
                var="Weird";
            }
            else{
                var="Not Weird";
            }
        }
        System.out.println(var);
    }
}
