class Solution(object):
    def topKFrequent(self, words, k):
        count = collections.Counter(words)
        candidates = list(count.keys())
        candidates.sort(key = lambda w: (-count[w], w))
        return candidates[:k]