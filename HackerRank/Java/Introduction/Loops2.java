import java.util.*;
import java.lang.Math;

class Solution{
    public static void main(String []args){
        Scanner in = new Scanner(System.in);
        int q=in.nextInt();
        for(int i=0;i<q;i++){
            int a = in.nextInt();
            int b = in.nextInt();
            int n = in.nextInt();
            int s=a;
            for(int j=0;j<n;j++){
                a=(int)(a+(Math.pow(2,j)*b));
                System.out.print(a + " ");
            }
            System.out.println();
        }
        in.close();
    }
}
