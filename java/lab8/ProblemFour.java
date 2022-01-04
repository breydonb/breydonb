import java.util.ArrayList;
import java.util.Arrays;
import java.util.HashSet;

public class ProblemFour {
    public static void main(String[] args){
        ArrayList<Integer> a1 = new ArrayList<>(Arrays.asList(2,3,6,8));
        ArrayList<Integer> a2 = new ArrayList<>(Arrays.asList(1,3,5,8));

        System.out.println(symmetricSetDifference(a1, a2));
        
    }

    public static HashSet<Integer> symmetricSetDifference(ArrayList<Integer> a1, ArrayList<Integer> a2){
        HashSet<Integer> hs = new HashSet<>();
        if(a1.size() > a2.size()){
            for(int i = 0; i < a1.size(); i++){
                System.out.println(a1.get(i));
                if(!a2.contains(a1.get(i))){
                    hs.add(a1.get(i));
                }

            }
        }
        else if(a1.size() < a2.size()){
            for(int i = 0; i < a2.size();i++){
                if(!a1.contains(a2.get(i))){
                    hs.add(a2.get(i));
                }
            }
        }else{
            for(int i = 0; i < a1.size(); i++){
                if(!a1.contains(a2.get(i))){
                    hs.add(a2.get(i));
                    hs.add(a1.get(i));
                }
            }
        }
        return hs;
    }
}
