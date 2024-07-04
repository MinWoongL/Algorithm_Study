import java.io.IOException;
import java.util.*;
import java.io.*;
public class Main {

    public static void main(String[] args) throws IOException {
    BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

    int[] nums = new int[5];
    String[] input = br.readLine().split(" ");

    for (int i = 0; i<5; i++){
        nums[i] = Integer.parseInt(input[i]);
    }

    int ans = Integer.MAX_VALUE;

    for (int i = 0; i < 5; i++) {
        for (int j = i + 1; j < 5; j++) {
            for (int k = j + 1; k < 5; k++) {
                int lcmValue = lcm(nums[i], lcm(nums[j], nums[k]));
                if (lcmValue < ans) {
                    ans = lcmValue;
                }
            }
        }
    }

    System.out.println(ans);

    }

    private static int gcd(int a, int b) {
        while (b != 0) {
            int temp = b;
            b = a % b;
            a = temp;
        }
        return a;
    }

    private static int lcm(int a, int b) {
        return a * (b / gcd(a, b));
    }


}