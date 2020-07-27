class LRUCache {

    public class CacheItem {
        int key;
        int value;
        CacheItem prev;
        CacheItem next;

        public CacheItem(int key, int value) {
            this.key = key;
            this.value = value;
        }
    }

    CacheItem head;
    CacheItem tail;
    int capacity;
    Map<Integer, CacheItem> map;

    public LRUCache(int capacity) {
        this.head = null;
        this.tail = null;
        this.capacity = capacity;
        map = new HashMap<>();
    }

    public int get(int key) {
        if (!map.containsKey(key)) {
            return -1;
        }
        moveToHead(key);

        return head.value;
    }

    public void put(int key, int value) {
        if (get(key) == -1) {
            // insert
            CacheItem item = new CacheItem(key, value);
            map.put(key, item);
            if (head == null) {
                head = item;
                tail = item;
            } else {
                setHead(item);
            }
            if (map.size() > capacity) {
                map.remove(tail.key);
                moveTailToPrev();
            }
        } else {
            // update
            CacheItem cur = map.get(key);
            cur.value = value;
        }
    }

    private void moveToHead(int key) {
        CacheItem cur = map.get(key);
        if (cur == head) return;

        cur.prev.next = cur.next;
        if (cur != tail) {
            cur.next.prev = cur.prev;
        } else {
            moveTailToPrev();
        }
        setHead(cur);
    }

    private void setHead(CacheItem item) {
        item.prev = null;
        item.next = head;
        head.prev = item;
        head = item;
    }

    private void moveTailToPrev() {
        tail = tail.prev;
        tail.next = null;
    }
}

/**
 * Your LRUCache object will be instantiated and called as such:
 * LRUCache obj = new LRUCache(capacity);
 * int param_1 = obj.get(key);
 * obj.put(key,value);
 */