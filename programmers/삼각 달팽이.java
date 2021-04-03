class Solution {
    public int[] solution(int n) {
        return new Triangle(n).convertTo1DArray();
    }
}

class Triangle {
    private static final int AVAILABLE = -1;

    public int[][] field;
    public final int lastNum;

    public Triangle(int n) {
        this.lastNum = (n * (n + 1)) / 2;
        initField(n);
        fill();
    }

    private void initField(int n) {
        this.field = new int[n][n];
        for (int i = 0; i < n; i++) {
            for (int j = 0; j <= i; j++) {
                this.field[i][j] = AVAILABLE;
            }
        }
    }

    private void fill() {
        int i = 0, j = 0, k = 1;
        while (k <= this.lastNum) {
            while (i < field.length && isAvailableSpot(i, j)) {
                this.field[i++][j] = k++;
            }
            i--; j++;
            while (j < field.length && isAvailableSpot(i, j)) {
                this.field[i][j++] = k++;
            }
            i--; j -= 2;
            while (i >= 0 && isAvailableSpot(i, j)) {
                this.field[i--][j--] = k++;
            }
            i += 2; j++;
        }
    }

    private boolean isAvailableSpot(int i, int j) {
        return this.field[i][j] == AVAILABLE;
    }

    public int[] convertTo1DArray() {
        int[] arr = new int[this.lastNum];
        int k = 0;
        for (int i = 0; i < field.length; i++) {
            for (int j = 0; j <= i; j++) {
                arr[k++] = this.field[i][j];
            }
        }

        return arr;
    }
}