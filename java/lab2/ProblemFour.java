import java.io.File;
import java.io.FileNotFoundException;
import java.util.NoSuchElementException;
import java.util.Scanner;

public class ProblemFour{
    public static void main(String[] args) throws NoSuchElementException{
        Scanner s = new Scanner(System.in);

        System.out.println("What is the name of the first file?");
        String sFileName = s.nextLine();
        File firstFile = new File(sFileName);

        System.out.println("What is the second file name?");
        String sSecondName = s.nextLine();
        File secondFile = new File(sSecondName);
        

        try{
            Scanner fileOne = new Scanner(firstFile);
            Scanner fileTwo = new Scanner(secondFile);
            int line = 1;
            System.out.println("There are some differences found:\n");
            while(fileOne.hasNextLine() || fileTwo.hasNextLine()){
                String data = fileOne.nextLine();
                String data2 = fileTwo.nextLine();
                // System.out.println(data);
                if(!data.equals(data2)){
                    System.out.println("Line "+line+":");
                    System.out.println("< "+data);
                    System.out.println("> "+ data2+"\n");
                    
                    line = line + 1;
                }else{
                    line = line + 1;
                }

            }
            fileOne.close();
            fileTwo.close();
        }catch(FileNotFoundException e){
            System.out.println("Error "+e);
        }
        s.close();
    }
}