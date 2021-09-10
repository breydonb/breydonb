import java.lang.reflect.Array;
import java.util.Arrays;

public class ProblemTwo{
    public static void main(String[] args){
        System.out.println("The range is: "+digitRange(68437));
    }
    public static int digitRange(int iNumber){
        int length = (int)(Math.log10(iNumber)+1);
        // Range is Max - Min +1
        int max, min;
        int[] digit = new int[length];
        for(int i = 0; i < length; i++){
            // This was the easiest way to split the single digits into an array without strings
            // We take 10 to the i + 1 power to get our modulus, then 10^i to get our divider;

            int iMod = (int) (Math.pow(10, (i + 1)));
            int iDivider = (int) (Math.pow(10, (i)));
            digit[i] = (iNumber % iMod) / iDivider;
        }
        Arrays.sort(digit);
        max = digit[length - 1];
        min = digit[0];
        int iRange = (max - min) + 1;
        return iRange;
    }
}