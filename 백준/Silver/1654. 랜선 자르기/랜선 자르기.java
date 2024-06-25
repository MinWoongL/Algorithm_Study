import java.util.*;
import java.io.*;
public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));

        String[] input = br.readLine().split(" ");
        int K = Integer.parseInt(input[0]);
        int N = Integer.parseInt(input[1]);

        int[] Lan = new int[K];
        int maxValue = 0;

        for (int i = 0; i < K; i++){
            Lan[i] = Integer.parseInt(br.readLine());
            if (Lan[i] > maxValue){
                maxValue = Lan[i];
            }
        }

        long l = 1;
        long r = maxValue;
        long ans = 0;

        while (l <= r){
            long mid = (l+r)/2;

            long cnt = 0;
            for (long wire : Lan){
                cnt += (wire/mid);
            }

            if (cnt >= N){
                ans = mid;
                l = mid + 1;
            } else {
                r = mid - 1;
            }
        }

        bw.write(String.valueOf(ans));
        bw.flush();
        bw.close();
        br.close();
    }
}

