class tree():
  def __init__(self,root=None):
    self.root=root
    self.rootNode=True
    self.children=[None] * 2

  def insert(self, val):
    node=tree(val)
    node.rootNode=False
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
      return True, currentNode
    if not found:
      if self.get_LChild():
        currentNode=self.get_LChild()
        (f, fnode )= currentNode.search_preorder(val)
        if f:
          return (f, fnode)
      if self.get_RChild():
        currentNode=self.get_RChild()
        return currentNode.search_preorder(val)
      return False,tree()

  def search_postorder(self,val):
  	found=False
  	if not found:
  	  if self.get_LChild():
  	  	(f,fnode)=self.get_LChild().search_postorder(val)
  	  	if f:
  	  	  return (f,fnode)
  	  if self.get_RChild():
  	  	(f,fnode)=self.get_RChild().search_postorder(val)
  	  	if f:
  	  	  return (f,fnode)

  	if self.get_val()==val:
  	  found=1
  	  return found,self

  	return False, tree()

  def search_inorder(self,val):
  	found=False
  	if not found:
  	  if self.get_LChild():
  	  	(f,fnode)=self.get_LChild().search_inorder(val)
  	  	if f:
  	  	  return f,fnode

  	if self.get_val()==val:
  	  found=True
  	  return found, self

  	if self.get_RChild():
  	  return self.get_RChild().search_inorder(val)

  	return found, tree()

  def tree_BFS(self, val):
  	q=[]
  	found=False
  	count=0
  	if self.rootNode:
  	  q.append(self)
  	while q !=[]:
  	  currentNode=q.pop(0)
  	  count+=1
	  if currentNode.get_LChild():
  	    q.append(currentNode.get_LChild())
  	  if currentNode.get_RChild():
  	    q.append(currentNode.get_RChild())
  	  if currentNode.get_val()==val:
  	    found=True
  	    break
  	return found, count

  def depth(self):
    left_depth = self.get_LChild().depth() if self.get_LChild() else 0
    right_depth = self.get_RChild().depth() if self.get_RChild() else 0
    return max(left_depth, right_depth) + 1

  def get_val(self):
  	return self.root
  def get_LChild(self):
  	return self.children[0]
  def get_RChild(self):
  	return self.children[1]

def tree_depth(tr):
  if tr.get_LChild():
    left_depth = tree_depth(tr.get_LChild())+1
  else:
     left_depth=0
  if tr.get_RChild():
    right_depth = tree_depth(tr.get_RChild())+1  
  else:
    right_depth= 0
  return max(left_depth, right_depth)

a=tree(1)
a.insert(2)
a.insert(3)
a.insert(4)
a.insert(5)
a.insert(6)

# (found, b)=a.search_inorder(2)

# if found:
#   print b.get_val()

(found, b)=a.tree_BFS(2)
print found, b
print "depth:",a.depth()
print "alt depth:", tree_depth(a)