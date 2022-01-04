import java.util.ArrayList;

public class ProblemOne {
    public static void main(String[] args){
        ArrayList<String> al = new ArrayList<>();
        al.add("test");
        al.add("test12");
        al.add("longest string");
        al.add("test2");
        al.add("test1235");
        al.add("longestest string");
        System.out.println(maxLength(al));
        System.out.println(al);
        
    }
    public static int maxLength(ArrayList<String> al){
        if(al.size() != 0){
            String temp = al.get(0);
            for(int i = 0; i < al.size(); i++){
                // System.out.println("al.get(al.size() - i - 1): "+ al.get(al.size() - i - 1) +"\t Temp: "+temp);
                if(al.get(al.size() - i - 1).length() > temp.length() ){
                    temp = al.get(al.size() - i - 1);
                }
            }
            return temp.length();
        }

        return 0;
        
    }
}
