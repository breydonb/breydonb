import java.util.Scanner;

public class ProblemOne{
    public static void main(String[] args){
        String sBirthOne,sBirthTwo,sDate;

        Scanner s = new Scanner(System.in);
        
        System.out.println("What is the first person's birthday?");
        sBirthOne = s.nextLine();
        System.out.println("What is the second person's birthday?");
        sBirthTwo = s.nextLine();
        System.out.println("What is today's date?");
        sDate = s.nextLine();

        String[] aBirthOne = sBirthOne.split("/");
        String[] aBirthTwo = sBirthTwo.split("/");
        String[] aDate = sDate.split("/");

        int monthOne = Integer.parseInt(aBirthOne[0]);
        int daysOne = Integer.parseInt(aBirthOne[1]);

        int monthTwo = Integer.parseInt(aBirthTwo[0]);
        int daysTwo = Integer.parseInt(aBirthTwo[1]);

        int monthDate = Integer.parseInt(aDate[0]);
        int dayDate = Integer.parseInt(aDate[1]);
        
        int absDaysOne = calculateDate(monthOne, daysOne);
        int absDaysTwo = calculateDate(monthTwo,daysTwo);
        int todayDay = calculateDate(monthDate,dayDate);

        int daysUntilOne = absDaysOne - todayDay;
        int daysUntilTwo = absDaysTwo - todayDay;
        int x = 0;
        while(x <= 1){
            if(daysUntilOne < 0){
                daysUntilOne = daysUntilOne + 365;
            }else if(daysUntilOne == 0 || daysUntilTwo == 0){
                System.out.println("Happy Birthday!");
            }else if(daysUntilTwo < 0){
                daysUntilTwo = daysUntilTwo + 365;
            }
            x+=1;
        }
        System.out.println(daysUntilOne+ " until person one's birthday");
        System.out.println(daysUntilTwo+ " until person two's birthday");

        if(daysUntilOne < daysUntilTwo){
            System.out.println("Person One's birthday is closer");
        }else{
            System.out.println("Person Two's birthday is closer");
        }

        s.close();
        // For the sake of simplicity, lets use a REALLY long switch statement to cover for the changing days in a year
        
    }
    public static int calculateDate(int month, int days){
        int absDays;
        switch(month){
            case 1:  month = 1;
                absDays = days;
                return absDays;
            case 2: month = 2;
                absDays = days + 31;
                return absDays;
            case 3: month = 3;
                absDays = days + 31 + 28;
                return absDays;
            case 4: month = 4;
                absDays = days + (31 * 2) + 28;
                return absDays;
            case 5:  month = 5;
                absDays = days + (31 * 2) + 28 + 30;
                return absDays;
            case 6: month = 6;
                absDays = days + (31 * 3) + 28 + 30;
                return absDays;
            case 7: month = 7;
                absDays = days + (31 * 3) + 28 + (30 * 2);
                return absDays;
            case 8: month = 8;
                absDays = days + (31 * 4) + 28 + (30 * 2);
                return absDays;
            case 9:  month = 9;
                absDays = days + (31 * 5) + 28 + (30 * 2);
                return absDays;
            case 10: month = 10;
                absDays = days + (31 * 5) + 28 + (30 * 3);
                return absDays;
            case 11: month = 11;
                absDays = days + (31 * 6) + 28 + (30 * 3);
                return absDays;
            case 12: month = 12;
                absDays = days + (31 * 6) + 28 + (30 * 4);
                return absDays;
            default:
                System.out.println("Error: Invalid Date");
                return 0;

        }  
    }   
}