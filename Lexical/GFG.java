import java.util.*;
public class GFG { 
    public static void main(String args[]) 
    { 
        String str = "Geeks Geeks Students"; 
        String[] arrOfStr = str.split(" "); 
        List<String> l = Arrays.<String>asList(arrOfStr);
        ArrayList<String> al = new ArrayList<String>(l);
        System.out.print(al.get(0));

    } 
} 