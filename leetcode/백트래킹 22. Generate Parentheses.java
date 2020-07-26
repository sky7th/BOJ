class Solution {
    public List<String> generateParenthesis(int n) {
        List<String> ret = new ArrayList<>();
        recur(n, 0, 0, "", ret);
        return ret;
    }

    private void recur(int n, int openedCount, int closedCount, String str, List<String> ret) {
        if (openedCount == n && closedCount == n) {
            ret.add(str);
            return;
        }
        if (openedCount < n) {
            recur(n, openedCount + 1, closedCount, str + "(", ret);
        }
        if (openedCount > closedCount) {
            recur(n, openedCount, closedCount + 1, str + ")", ret);
        }
    }
}