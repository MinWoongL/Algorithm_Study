import java.io.IOException;
import java.util.*;
import java.io.*;
public class Main {


    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int K = Integer.parseInt(br.readLine());

        int[] arr = new int[1001];
        int s = Integer.MAX_VALUE;
        int e = 0;
        Stack<Integer> stack = new Stack<>();

        for (int i = 0; i<K; i++){
            StringTokenizer st = new StringTokenizer(br.readLine());
            int L = Integer.parseInt(st.nextToken());
            int H = Integer.parseInt(st.nextToken());

            arr[L] = H;
            s = Math.min(L, s);
            e = Math.max(L, e);
        }

        int tmp = arr[s];
        for (int i = s+1; i <= e; i++) {
            if (arr[i] < tmp) {
                stack.push(i);
            }
            else {
                while (!stack.isEmpty()) {
                    int x = stack.pop();
                    arr[x] = tmp;
                }
                tmp = arr[i];
            }
        }

        stack.clear();

        tmp = arr[e];

        for (int i = e-1; i >= s; i--){
            if (arr[i] < tmp) {
                stack.push(i);
            }
            else {
                while (!stack.isEmpty()) {
                    int x = stack.pop();
                    arr[x] = tmp;
                }
                tmp = arr[i];
            }
        }

        int ans = 0;
        for (int i = s; i <= e; i++) {
            ans += arr[i];
        }

        System.out.println(ans);


    }




}