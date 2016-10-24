class Trie(object):
  def __init__(self, flag):
    self.flag= flag
    self.children=[None]*26
