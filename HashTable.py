class HashTable(object):
  def __init__(self, size):
    self.size=size
    self.key = [None] * size
    self.value= [None] * size

  def put(self, key, value):
    hashValue=self.hashFunc(key, self.size)

    if self.key[hashValue]==None:
      self.key[hashValue]=key
      self.value[hashValue]=value
    else:
      hashValue=self.rehashFunc(key, self.size)
      self.key[hashValue]=key
      self.value[hashValue]=value

  def hashFunc(self, key, size):
    return key%size

  def rehashFunc(self, key, size):
    return (key+1)%size#
  def delete(self, key):
    hashValue=self.hashFunc(key, self.size)
    self.key[hashValue]=None
    self.value[hashValue]=None


a=HashTable(10)
a.put(1, "book")
a.put(15, "text")
a.put(11,"clash")

#a.delete(1)
print a.value