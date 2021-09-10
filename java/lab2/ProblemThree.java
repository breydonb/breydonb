import java.util.Scanner;

public class ProblemThree{
    public static void main(String[] arg){
        Scanner s = new Scanner(System.in);
        String sValue;
        int iCounter = 1;
        // We can use this equation to find: Math.random() * (max - min + 1) + min  
        int iRandom = (int) (Math.random() * (10 - 1 + 1) + 1);
        Boolean bGameOver = false;

        System.out.println("Come up with a number and let me guess it!");
        
        while(!bGameOver){
            System.out.println("Is it "+iRandom+"? (y/n):\t");
            sValue = s.next();
            sValue = sValue.toLowerCase();
            if(sValue.equals("y")){
                bGameOver = true;
                if(iCounter == 1){
                    System.out.println("It took me "+iCounter+" time to guess your number "+ iRandom);
                }
                else{
                    System.out.println("It took me "+iCounter+" times to guess your number "+ iRandom);
                }
            }
            else{
                iCounter = iCounter+1;
                iRandom = (int) (Math.random() * (10 - 1 + 1) + 1);
            }
        }
        s.close();
    }
}