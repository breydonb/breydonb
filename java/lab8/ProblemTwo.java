import java.util.ArrayList;

public class ProblemTwo {
    public static void main(String args[]){
        ArrayList<Integer> al = new ArrayList<>();
        al.add(4);
        al.add(3);
        System.out.println(hasOdd(al));
    }

    public static boolean hasOdd(ArrayList<Integer> al){
        if(!al.isEmpty()){ 
            for(int i = 0; i < al.size(); i++){
                if(al.get(i) % 2 != 0) return true;
            }
        }
        return false;
    }
}
