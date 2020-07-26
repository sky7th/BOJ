class Solution {
    public class Point {
        int x;
        int y;
        boolean isStart;
        public Point (int x, int y, boolean isStart) {
            this.x = x;
            this.y = y;
            this.isStart = isStart;
        }
    }

    public List<List<Integer>> getSkyline(int[][] buildings) {
        List<Point> list = new ArrayList<>();
        for (int[] b : buildings) {
            list.add(new Point(b[0], b[2], true));
            list.add(new Point(b[1], b[2], false));
        }

        Collections.sort(list, (a, b) -> {
            if (a.x != b.x) {
                return a.x - b.x;
            } else if (a.isStart && !b.isStart) {
                return -1;
            } else if (!a.isStart && b.isStart) {
                return 1;
            } else if (a.isStart && b.isStart) {
                return b.y - a.y;
            } else {
                return a.y - b.y;
            }
        });

        PriorityQueue<Integer> pq = new PriorityQueue<>(5, (a, b) -> b - a);
        pq.offer(0);

        List<List<Integer>> ret = new ArrayList<>();
        for (Point p : list) {
            int max = pq.peek();

            if (p.isStart) {
                pq.offer(p.y);
            } else {
                pq.remove(p.y);
            }

            if (max != pq.peek()) {
                ret.add(new ArrayList<Integer>(Arrays.asList(p.x, pq.peek())));
            }
        }

        return ret;
    }
}