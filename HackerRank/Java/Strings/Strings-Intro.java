import java.io.*;
import java.util.*;

public class Solution {

    public static void main(String[] args) {
        
        Scanner sc=new Scanner(System.in);
        String A=sc.next();
        String B=sc.next();
      
        int count;
        int a = A.length();
        int b = B.length();
        count = a+b;
        System.out.println(count);
        char a1 = A.charAt(0);
        char b1 = B.charAt(0);
        if(a1>b1){
            System.out.println("Yes");
        }
        else{
            System.out.println("No");
        }
        String first = A.substring(0,1);
        String rem1 = A.substring(1);
        first = first.toUpperCase();
        String tot1 = first + rem1;
        System.out.print(tot1);
        System.out.print(" ");
        String second = B.substring(0,1);
        String rem2 = B.substring(1);
        second = second.toUpperCase();
        String tot2 = second + rem2;
        System.out.print(tot2);        
    }
}



