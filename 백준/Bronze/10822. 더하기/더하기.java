import java.io.IOException;
import java.util.*;
import java.io.*;
public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));


        String[] input = br.readLine().split(",");

        int sum = 0;

        for (int i = 0; i < input.length; i++) {
            sum += Integer.parseInt(input[i]);
        }

        System.out.println(sum);

    }


}