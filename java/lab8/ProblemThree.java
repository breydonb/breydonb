import java.util.ArrayList;

public class ProblemThree {
    public static void main(String[] args){
        ArrayList<String> al = new ArrayList<>();
        al.add("test");
        al.add("tests");
        al.add("test12");
        al.add("Hi I'm odd");
        removeEvenLength(al);
        System.out.println(al);

    }

    public static void removeEvenLength(ArrayList<String> al){
        if(al.size() != 0){
            for(int i = 0; i < al.size(); i++){
                if(al.get(i).length() % 2 == 0){
                    al.remove(i);
                }
            }
        }
    }
}
