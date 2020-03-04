# Node class. It stores the single data field and the next node pointer
class Node(object):
    def __init__(self, val):
        self.val = val
        self.next = None

    def get_data(self):
        return self.val

    def set_data(self, val):
        self.val = val

    def get_next(self):
        return self.next

    def set_next(self, next):
        self.next = next

# LinkedList class
class LinkedList(object):
    def __init__(self, head=None):
        self.head = head
        self.count = 0

    def get_count(self):
        return self.count

    def insert(self, data):
        # insert a new node at the beginning
        new_node = Node(data)
        new_node.set_next(self.head)
        self.head = new_node
        self.count += 1

    def find(self, val):
        item = self.head
        while ( item != None):
            if item.get_data() == val:
                return item
            else:
                item = item.get_next()
        return None

    def deleteAt(self, index):
        if index > self.count -1:
            return
        if index == 0:
            self.head = self.head.get_next()
        else:
            tempidx = 0
            node = self.head
            while tempidx < index - 1:
                node = node.get_next()
                tempidx += 1
            node.set_next(node.get_next().get_next())
            self.count -= 1
    
    def dump_list(self):
        tempnode = self.head
        while( tempnode != None):
            print("Node: ", tempnode.get_data())
            tempnode = tempnode.get_next()

# create a linked list and insert some items
itemList = LinkedList()
itemList.insert(38)
itemList.insert(49)
itemList.insert(13)
itemList.insert(15)
itemList.dump_list()

# traverse the list
print("Item count: ", itemList.get_count())
print("Finding item: ", itemList.find(13))
print("Finding item: ", itemList.find(78))

#delete an item
itemList.deleteAt(3)
print("Item count: ", itemList.get_count())
print("Finding item: ", itemList.find(38))
itemList.dump_list()
        