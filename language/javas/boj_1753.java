import java.io.*;
import java.util.*;

class Node implements Comparable<Node> {
    int id, weight;

    public Node(int id, int weight) {
        this.id = id;
        this.weight = weight;
    }

    @Override
    public int compareTo(Node o) {
        return weight - o.weight;
    }
}


public class boj_1753 {
    static List<Node>[] graph;
    static int[] dist;
    static int V, E, K;
    static final int INF = (int) 1e9;

    public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));

        String inputs = br.readLine();
        StringTokenizer st = new StringTokenizer(inputs);
        V = Integer.parseInt(st.nextToken()); 
        E = Integer.parseInt(st.nextToken()); 
        K = Integer.parseInt(br.readLine()); 

        graph = new ArrayList[V+1];
        dist = new int[V+1];

        for (int i = 1; i <= V; i++) {
            graph[i] = new ArrayList<>();
        }
        for (int i = 0; i < E; i++) {
            inputs = br.readLine();
            st = new StringTokenizer(inputs);
            int u = Integer.parseInt(st.nextToken()); 
            int v = Integer.parseInt(st.nextToken()); 
            int w = Integer.parseInt(st.nextToken()); 
            graph[u].add(new Node(v, w));
        }


        dijkstra(K);

        // 출력
        StringBuilder sb = new StringBuilder();
        for (int i = 1; i <= V; i++) {
            if (dist[i] == INF)
                sb.append("INF"+"\n");
            else
                sb.append(dist[i]+"\n");
        }

        bw.write(sb.toString());

        bw.flush();
        bw.close();

	}

    

    private static void dijkstra(int start) {
        Arrays.fill(dist, INF);
        dist[start] = 0;
        PriorityQueue<Node> pq = new PriorityQueue<>();
        pq.add(new Node(start, 0));

        while(!pq.isEmpty()) {
            Node curNode = pq.poll();
            int curId = curNode.id;
            int curWeight = curNode.weight;

            if (dist[curId] < curWeight)    continue;

            for(Node next: graph[curId]) {
                int newWeight = curWeight + next.weight;

                if(dist[next.id] > newWeight) {
                    dist[next.id] = newWeight;
                    pq.add(new Node(next.id, newWeight));
                }
            }
        }


    }



}