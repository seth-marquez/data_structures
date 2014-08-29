class node:                       #base code for a node
  def __init__(self, info):
    self.info = info
    self.next = None

class list_of_linking:
  head = None
  tail = None
  node_count = 0

  def add_node(self, info):       #appends a node to the list
    new_node = node(info)
    new_node.info = info
    if self.head == None:
      self.head = new_node
      self.tail = new_node
    else:
      self.tail.next = new_node
      self.tail = new_node
    self.node_count += 1

  def remove_node(self, index):   #removes that bitch ass node at an indicated index
    prev = None
    node = self.head
    i = 0
    while ( node != None ) and ( i < index ):
       prev = node
       node = node.next
       i += 1
    if prev == None:
       self.head = node.next
    else:
       prev.next = node.next

  def print_list(self):           #iterates through the list of available nodes and prints their data
    node = self.head
    while node != None:
      print(node.info)
      node = node.next

#some testing

bob = list_of_linking()

bob.add_node(1)
bob.add_node(2)
bob.add_node(3)
bob.add_node(4)

bob.print_list( )
print()

bob.remove_node(0)                #removes node 0 then truncates the indexes and moves them
bob.remove_node(1)                #removes the now node 1 (previously node 2) and removes it

bob.print_list( )