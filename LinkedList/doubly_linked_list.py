#===============================================================================
# implementation for Doubly Linked List
#===============================================================================
class Node:
    
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None
        self.previous = None

    def __str__(self):
        return "[(%d, %s)]" %(self.key, self.value)

class DoublyList:
    
    def __init__(self):
        self.head = None
        self.tail = None
        
    def add_node(self, key, value):
        node = Node(key, value)
        if( self.head is None ):
            self.head = node
            self.tail = node
        else:
            self.tail.next = node
            node.previous = self.tail
            self.tail = node
    
    def add_to_front(self, key , value):
        node = Node(key, value)
        if self.head is None:
            self.head = node
        else:
            old_head = self.head
            self.head.previous = node
            self.head = node
            self.head.next = old_head
    
    def move_to_front(self, value):
        current_node = self.head
        previous_node = self.head
        if current_node.value is value:
            print "Node is already in front."
            return None
        else:
            while current_node.value is not value:
                if current_node.next is None:
                    print "No matching node found in list"
                    return None
                else:
                    previous_node = current_node
                    current_node = current_node.next
            previous_node.next = current_node.next
            print "Node %s moved to front of the list" %(current_node)
            self.add_to_front(current_node.key, current_node.value)
            
    def remove_first(self):
        if self.head is None:
            print "List is already empty"
        else:
            print "First node removed."
            self.head = self.head.next
            
    def remove_node(self, value):
        current_node = self.head
        previous_node = self.head
        if current_node.value is value:
            self.remove_first()
        else:
            while current_node.value is not value:
                if current_node.next is None:
                    print "No matching node found in list"
                    return None
                else:
                    previous_node = current_node
                    current_node = current_node.next
            previous_node.next = current_node.next
            print "Node %s removed from the list" %(current_node)
            previous_node.next = current_node.next
            
    def find_node(self, value):
        if self.head is None:
            print "List is already empty."
        else:
            if self.head.value is value:
                print "Node with value %s found in list, Node : %s" %(value, self.head)
            else:
                current_node = self.head
                while current_node.value is not value:
                    if current_node.next is None:
                        print "No matching node found in List"
                        return None
                    else:
                        current_node = current_node.next
                print "Node : %s found in list" %(current_node)
                return current_node
                        
    
    
    def __str__(self):
        l = []
        print "___________________________________"
        print "Head = %s" % (self.head)
        print "Tail = %s" % (self.tail)
        current = self.head
    
        if not current:
            return "[]"

        while(current):
            l.append("%s" % (current, ))
            current = current.next
        
        return " --> ".join(l)
    

def main():
    l = DoublyList()
    l.add_node(5, "Data Structures")
    l.add_node(9, "Algorithms")
    l.add_node(8, "Operating Systems")
    l.add_to_front(7, "Data Mining")
    l.move_to_front("Algorithms")
    l.remove_first()
    l.remove_node("Operating Systems")
    l.find_node("Data Structures")
    l.find_node("Asav")
    print l
    

if __name__ == '__main__':
    main()