class Node:
    
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None
    
    def __str__(self):
        return "[(%d, %s)]" %(self.key, self.value)
        

class SinglyList:
    
    def __init__(self):
        self.head = None
        self.tail = None
        
    def add_node(self, key, value):
        node = Node(key, value)
        #=======================================================================
        # if list is empty make this node the first node in list
        #=======================================================================
        if ( self.head is None ):
            self.head = node
            self.tail = node
        else:
            #===================================================================
            # place node we are inserting right next to tail of the list and slide the tail to the latest node inserted
            #===================================================================
            self.tail.next = node
            self.tail = node
           
    def remove_first(self):
        #=======================================================================
        # make the next node to the head as head so automatically head will be removed as there will be no address to reference it
        #=======================================================================
        if self.head is not None :
            self.head = self.head.next
            print "First node removed."
        else:
            print "Linked list is already empty."
            
    def find_link(self, value):
        #=======================================================================
        # check if list is empty or not
        #=======================================================================
        if self.head is None:
            print "Linked list is empty"
        elif self.head.value == value:
            #===================================================================
            # if node we are searching for is the first node then return it as in linked list we always start searching from the first node
            #===================================================================
            print "Link found %s" %(self.head)
            return self.head
        else:
            current = self.head
            while( current.value is not value):
                #===============================================================
                # this means we have reached to the end of the list and still our desired not has not been found yet
                #===============================================================
                if current.next is None:
                    print "Node not found in list"
                    return None
                else:
                    #===========================================================
                    # here i'm changing the current node in every iteration
                    #===========================================================
                    current = current.next
            print "Node found with value: %s " %(current.value)
            return current
    
    def remove_link(self, value):
        #=======================================================================
        # same logic as finding the node just we need to keep track of two reference nodes which is current node and a previous node
        #=======================================================================
        current_link = self.head
        previouse_link = self.head
        if( current_link is None ):
            print "Linkedlist is already empty."
        else:
            while( current_link.value is not value):
                if( current_link.next is None ):
                    print "Node not found in List"
                    return None
                else:
                    previouse_link = current_link
                    current_link = current_link.next
        if( current_link is self.head ):
            self.remove_first()
        else:
            print "Found a Match"
            print "current node : %s " %(current_link)
            print "previous node : %s " %(previouse_link)
            #===================================================================
            # this will delete the node which is in middle i.e current node [previous node]-->[current node]-->[] to [previous node]-->[current node's next]
            #===================================================================
            previouse_link.next = current_link.next
        return current_link
    
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
    l = SinglyList()
    l.add_node(5, "Data Structures")
    l.add_node(9, "Algorithms")
    l.add_node(8, "Operating Systems")
    l.add_node(7, "Data Mining")
    l.find_link("Operating Systems")
    l.remove_link("Hello")
    print l
    
if __name__ == '__main__':
    main()
            