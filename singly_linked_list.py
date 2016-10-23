class LinkedNode(object):
  def __init__(self, data=None):
    self.data=data
    self.nextNode=None
    self.previousNode=None

  def get_data(self):
    return self.data

  def get_nextNode(self):
    return self.nextNode

  def get_previousNode(self):
  	return self.previousNode

  def set_data(self, data):
    self.data=data

  def set_nextNode(self, node):
    self.nextNode=node
    node.previousNode=self #setting input node as the previous node since this node is its next node

  def set_previousNode(self, node):
  	self.previousNode=node




#linked list
#
#

class LinkedList(object):
  def __init__(self):
  	self.head=None
  	self.tail=None
  	self.numNodes=0
  	self.existFlag=0

  def get_head(self):
  	return self.head

  def get_tail(self):
  	return self.tail

  def insert(self, data):
  	newNode= LinkedNode(data)
  	if self.head==None:
  	  self.head=newNode
  	  self.tail=self.head
  	else:
  	  self.tail.set_nextNode(newNode)
  	  self.tail=newNode
  	self.numNodes+=1

  def get_numNode(self):
  	return self.numNodes

  def search(self, data):
  	currentNode=self.head
  	while currentNode:
  	  if currentNode.get_data()==data:
  	  	print "Found!"
  	  	return currentNode
  	  else:
  	  	currentNode=currentNode.get_nextNode()
  	print "Data Not found!"
  	return LinkedNode()

  def delete(self, data):
  	delnode=self.search(data)
  	if delnode.get_nextNode() or delnode.get_previousNode():
  	  delnode.get_nextNode().set_previousNode(delnode.get_previousNode())
  	  delnode.get_previousNode().set_nextNode(delnode.get_nextNode())
  	  self.numNodes-=1
  	  print "and deleted!"
  	else:
  	  print "and nothing to delete!"

lst=LinkedList()
lst.insert("a")
lst.insert("b")
lst.insert("c")
lst.insert("d")
lst.insert("c")
lst.insert("a")
lst.insert("f")


lst.search("q")
lst.delete("b")


print lst.get_numNode()
