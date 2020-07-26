class Solution {
    public boolean possibleBipartition(int N, int[][] dislikes) {
        List<List<Integer>> adjList = new ArrayList<>();
        boolean[] visited = new boolean[N];
        boolean[] color = new boolean[N];

        for (int i = 0; i < N; i++) {
            adjList.add(new ArrayList<>());
        }

        for (int[] d: dislikes) {
            int a = d[0] - 1;
            int b = d[1] - 1;
            adjList.get(a).add(b);
            adjList.get(b).add(a);
        }

        for (int i = 0; i < N; i++) {
            if (!visited[i]) {
                visited[i] = true;
                if (!isBipartiteDfs(i, adjList, visited, color)) return false;
            }
        }

        return true;
    }

    private boolean isBipartiteDfs(int cur, List<List<Integer>> adjList, boolean[] visited, boolean[] color) {
        for (int next : adjList.get(cur)) {
            if (!visited[next]) {
                visited[next] = true;
                color[next] = !color[cur];
                if (!isBipartiteDfs(next, adjList, visited, color)) return false;

            } else if (color[cur] == color[next]) {
                return false;
            }
        }

        return true;
    }
}