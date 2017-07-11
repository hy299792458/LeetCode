class LRUCache(object):

    def __init__(self, capacity):
        self.cache = collections.OrderedDict()
        self.cap = capacity

    def get(self, key):
        value = self.cache.pop(key, None)
        if not value:
            return -1
        self.cache[key] = value
        return value

    def put(self, key, value):
        if self.cache.get(key, None):
            self.cache.pop(key)
        self.cache[key] = value
        if len(self.cache) > self.cap:
            self.cache.popitem(last = False)


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
