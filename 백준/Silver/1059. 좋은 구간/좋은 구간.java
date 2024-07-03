import java.io.IOException;
import java.util.*;
import java.io.*;
public class Main {

    public static void main(String[] args) throws IOException {
    BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

    int L = Integer.parseInt(br.readLine());

    String[] nums = br.readLine().split(" ");
    int n = Integer.parseInt(br.readLine());

    Set<Integer> num_set = new TreeSet<>();

    for (String num: nums) {
        num_set.add(Integer.parseInt(num));
    }

    Integer[] sorted_set = num_set.toArray(new Integer[0]);

    int lower = 0;
    int upper = Integer.MAX_VALUE;

    for (int i = 0; i < sorted_set.length; i++) {
        if (sorted_set[i] < n) {
            lower = sorted_set[i];
        }
        if (sorted_set[i] > n && upper == Integer.MAX_VALUE) {
            upper = sorted_set[i];
        }
    }

//    if (lower == 0){
//        lower = 1;
//    }

    if (upper == Integer.MAX_VALUE) {
        upper = n + 1;
    }

    if (num_set.contains(n)){
        System.out.println(0);
        return;
    }

    int cnt = 0;
    for (int A=lower+1; A<n+1; A++){
        for (int B=n; B<upper; B++) {
            if (A<B) {
                cnt++;
            }
        }
    }

    System.out.println(cnt);

    }


}