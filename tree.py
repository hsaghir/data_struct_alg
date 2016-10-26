class tree():
  def __init__(self,root=None):
    self.root=root
    self.children=[None] * 2

  def insert(self, val):
    node=tree(val)
    if self.children[0]:
      if self.children[1]:
        temp=self.children[0]
        self.children[0]=node
        node.children[0]=temp
      else:
        temp=self.children[1]
        self.children[1]=node
        node.children[0]=temp
    else:
      self.children[0]=node

  def search_preorder(self, val):
    currentNode=self
    found=False
    if currentNode.get_val()==val:
      found=True
      print "this is:", currentNode.get_val()
      return currentNode
    if currentNode.get_LChild():
      currentNode=currentNode.get_LChild()
      currentNode.search_preorder(val)
    if currentNode.get_RChild():
      currentNode=currentNode.get_RChild()
      currentNode.search_preorder(val)
    
    return tree()

  def get_val(self):
  	return self.root
  def get_LChild(self):
  	return self.children[0]
  def get_RChild(self):
  	return self.children[1]

a=tree(1)
a.insert(2)
a.insert(3)
a.insert(4)
a.insert(5)


print a.search_preorder(3).get_val()