import java.util.ArrayList;
import java.util.LinkedList;
import java.util.Queue;

public class TopologicalSort {

    //process the indegree array while constructing the graph

    static void topologicalSort(ArrayList<Integer>[] adj, int[] indegree) {
        Queue<Integer> q = new LinkedList<Integer>();
        for(int i = 0; i < indegree.length; i++) {
            if(indegree[i] == 0) {
                q.add(i);
            }
        }
        while(!q.isEmpty()) {
            int v = q.poll();
            System.out.print(v + " ");
            for(int edge : adj[v]) {
                if(--indegree[edge] == 0) {
                    q.add(edge);
                }
            }
        }
    }

}