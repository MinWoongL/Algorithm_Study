import java.io.IOException;
import java.util.*;
import java.io.*;
public class Main {

    public static void main(String[] args) throws IOException {
    BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

    int N = Integer.parseInt(br.readLine());
    int[][] adjM = new int[N][N];

    for (int i = 0; i < N; i++) {
        StringTokenizer st = new StringTokenizer(br.readLine());
        for (int j = 0; j < N; j++) {
            adjM[i][j] = Integer.parseInt(st.nextToken());
        }
    }

    for (int i = 0; i<N; i++) {
        for (int j = 0; j<N; j++) {
            for (int k = 0; k<N; k ++) {
                if (adjM[j][i] == 1 && adjM[i][k] == 1) {
                    adjM[j][k] = 1;
                }
            }
        }
    }

    BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));

    for (int i = 0; i<N; i++){
        for (int j = 0; j<N; j++){
            bw.write(adjM[i][j]+" ");
        }
        bw.newLine();
    }

    bw.flush();
    bw.close();


    }
    

}