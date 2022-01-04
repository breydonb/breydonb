import java.util.HashMap;

public class ProblemSix {
    public static void main(String[] args){
        HashMap<String,String> subMap = new HashMap<String, String>();
        HashMap<String,String> map = new HashMap<String, String>();

        map.put("Marty", "205-9024");
        map.put("Hawking", "123-4567");
        map.put("Smith", "949-9024");
        map.put("Newton", "123-4527");

        subMap.put("Smith", "949-9024");
        subMap.put("Marty", "205-9224");
        System.out.println(subMap(map, subMap));
    }

    public static boolean subMap(HashMap<String,String> map ,HashMap<String,String> subMap){
        // We need a nested for loop
        for(String i : map.values()){
            for(String j : subMap.values()){
                if(i.equals(j)){
                    return true;
                }
            }
        }
        return false;
    }
}
