class Solution {
    public int[] solution(int[][] arr) {
        int[] answer = {0, 0};
        recur(arr, answer, 0, 0, arr.length);
        
        return answer;
    }
    
    private void recur(int[][] arr, int[] answer, int y, int x, int n) {
        int firstValue = arr[y][x];
        for (int i = y; i < y + n; i++) {
            for (int j = x; j < x + n; j++) {
                if (arr[i][j] != firstValue) {
                    int mid = n / 2;
                    recur(arr, answer, y, x, mid);
                    recur(arr, answer, y + mid, x, mid);
                    recur(arr, answer, y, x + mid, mid);
                    recur(arr, answer, y + mid, x + mid, mid);
                    
                    return;
                }
            }
        }
        
        answer[firstValue]++;
    }
}