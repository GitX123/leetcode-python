# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)

'''
Elements we need
* Hash map: hold the key-value data (node).
* Doubly linked list: sort from LRU to MRU data.
* Two pointers: tell LRU (least recently used) and MRU (most recently used) data. 
'''

class Node:
    def __init__(self, key, val) -> None:
        self.key = key
        self.val = val
        self.prev: Node = None
        self.next: Node = None

class LRUCache:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = {}

        self.lru = Node(0, 0)
        self.mru = Node(0, 0)
        self.lru.next = self.mru
        self.mru.prev = self.lru

    '''
    Remove node from linked list.
    '''
    def remove_node(self, node: Node):
        prev_node, next_node = node.prev, node.next
        prev_node.next, next_node.prev = next_node, prev_node

    '''
    Insert node to the rightmost (left to MRU pointer).
    '''
    def insert_node(self, node: Node):
        prev_node = self.mru.prev
        prev_node.next = node
        self.mru.prev = node
        node.prev = prev_node
        node.next = self.mru

    '''
    Return if key exists and move retrieved node to MRU.
    '''
    def get(self, key: int) -> int:
        if key in self.cache:
            # move to MRU
            self.remove_node(self.cache[key])
            self.insert_node(self.cache[key])
            return self.cache[key].val
        return -1

    '''
    Store data into cache.
    1. If data exists:
        a. Remove node from linked list.
        b. Add data normally.
    2. If number of data surpass cache capacity:
        a. Remove LRU node from liked list.
        b. Remove LRU data from hash map.
    '''
    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self.remove_node(self.cache[key])
        self.cache[key] = Node(key, value)
        self.insert_node(self.cache[key])

        if len(self.cache) > self.capacity:
            lru_node = self.lru.next
            self.remove_node(lru_node)
            del self.cache[lru_node.key]