class Codec:
    mapping = {}
    reverse = {}
    count = 0
    def encode(self, longUrl):
        if longUrl in self.reverse:
            return self.reverse[longUrl]
        else:
            k = str(self.count)
            self.count += 1
            self.reverse[longUrl] = k
            self.mapping[k] = longUrl
            return self.reverse[longUrl]

    def decode(self, shortUrl):
        """Decodes a shortened URL to its original URL.
        
        :type shortUrl: str
        :rtype: str
        """
        return self.mapping[shortUrl]
        

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.decode(codec.encode(url))
