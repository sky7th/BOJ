class Solution {
    public class WordCount {
        String word;
        int count;

        public WordCount (String word) {
            this.word = word;
            this.count = 1;
        }
    }

    public List<String> topKFrequent(String[] words, int k) {
        Map<String, WordCount> map = new HashMap<>();
        for (String word : words) {
            if (!map.containsKey(word)) {
                map.put(word, new WordCount(word));
            } else {
                map.get(word).count++;
            }
        }
        PriorityQueue<WordCount> pq = new PriorityQueue<>(k, (a, b) -> {
            if (a.count != b.count) {
                return b.count - a.count;
            }
            return a.word.compareTo(b.word);
        });
        for (WordCount wordCount : map.values()) {
            pq.offer(wordCount);
        }
        List<String> res = new ArrayList<>();
        for (int i = 0; i < k; i++) {
            System.out.println(pq.peek().word);
            res.add(pq.poll().word);
        }
        return res;
    }
}

// other solution
class Solution {
    public List<String> topKFrequent(String[] words, int k) {
        Map<String, Integer> count = new HashMap();
        for (String word: words) {
            count.put(word, count.getOrDefault(word, 0) + 1);
        }
        List<String> candidates = new ArrayList(count.keySet());
        Collections.sort(candidates, (w1, w2) -> count.get(w1).equals(count.get(w2)) ?
                w1.compareTo(w2) : count.get(w2) - count.get(w1));

        return candidates.subList(0, k);
    }
}