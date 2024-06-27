import java.io.IOException;
import java.util.*;
import java.io.*;
public class Main {
    static int R, C;
    static char[][] field;
    static boolean[] visited;
    static int[][] dxy = {{-1, 0}, {1, 0}, {0, -1}, {0, 1}};
    static int maxvalue = 1;

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        String[] rc = br.readLine().split(" ");
        R = Integer.parseInt(rc[0]);
        C = Integer.parseInt(rc[1]);

        field = new char[R][C];
        visited = new boolean[26];

        for (int i = 0; i < R; i++) {
            field[i] = br.readLine().toCharArray();
        }

        visited[field[0][0] - 'A'] = true;
        bt(0, 0, 1);
        System.out.println(maxvalue);


    }

    public static void bt(int x, int y, int score) {
        maxvalue = Math.max(score, maxvalue);

        for (int i = 0; i < 4; i++) {
            int nx = x + dxy[i][0];
            int ny = y + dxy[i][1];

            if (0 <= nx && nx <= R-1 && 0 <= ny && ny <= C-1) {
                if (!visited[field[nx][ny] - 'A']) {
                    visited[field[nx][ny] - 'A'] = true;
                    bt(nx, ny, score + 1);
                    visited[field[nx][ny] - 'A'] = false;
                }
            }
        }
    }


}