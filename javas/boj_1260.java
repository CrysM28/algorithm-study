import java.io.*;
import java.util.*;

public class boj_1260 {
    public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));

        String inputs = br.readLine();
        StringTokenizer st = new StringTokenizer(inputs);
        int N = Integer.parseInt(st.nextToken()); 
        int M = Integer.parseInt(st.nextToken()); 
        int V = Integer.parseInt(st.nextToken()); 

        int[][] adj = new int[N+1][N+1];
        for (int i = 0; i < M; i++) {
            inputs = br.readLine();
            st = new StringTokenizer(inputs);
            int start = Integer.parseInt(st.nextToken());
            int end = Integer.parseInt(st.nextToken());
            adj[start][end] = 1;
            adj[end][start] = 1;
        }
        

        // DFS
        boolean[] visited = new boolean[N+1];
        List<Integer> visitedDFS = new ArrayList<>();
        LinkedList<Integer> stack = new LinkedList<>();
        stack.push(V);


        while(!stack.isEmpty()) {
            int c = stack.pop();
            if(!visited[c]) {
                visited[c] = true;
                visitedDFS.add(c);

                for (int i = N; i >= 0; i--) {
                    if (adj[c][i] == 1) {
                        stack.push(i);
                    }
                }
            }
        }

        for (int num: visitedDFS) {
            bw.write(num + " ");
        }
        bw.newLine();

        
        // BFS
        visited = new boolean[N+1];
        ArrayList<Integer> visitedBFS = new ArrayList<>();
        Queue<Integer> queue = new LinkedList<>();

        visited[V] = true;
        visitedBFS.add(V);
        queue.offer(V);

        while (!queue.isEmpty()) {
            int c = queue.poll();
            

            for (int i = 1; i <= N; i++) {
                if (adj[c][i] == 1 && !visited[i]) {
                    visited[i] = true;
                    queue.offer(i);
                    visitedBFS.add(i);
                }
            }
        }

        for (int num: visitedBFS) {
            bw.write(num + " ");
        }
        bw.newLine();

        bw.flush();
        bw.close();

	}
}