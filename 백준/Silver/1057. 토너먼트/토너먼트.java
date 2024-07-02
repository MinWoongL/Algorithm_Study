import java.io.IOException;
import java.util.*;
import java.io.*;
public class Main {

    public static void main(String[] args) throws IOException {
    BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

    String[] input = br.readLine().split(" ");
    int N = Integer.parseInt(input[0]);
    int K = Integer.parseInt(input[1]);
    int L = Integer.parseInt(input[2]);

    int cnt = 0;
    while (K!=L) {
        K = (K + 1)/2;
        L = (L + 1)/2;
        cnt++;
    }

    System.out.println(cnt);


    }


}