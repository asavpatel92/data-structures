#===============================================================================
# implementation of a stack using linked list. i.e stack size is dynamic
#===============================================================================

class Node:
    
    def __init__(self,key, value):
        self.key = key
        self.value = value
        self.next = None
        
    def __str__(self):
        return "[(%d, %s)]" %(self.key, self.value)
    
class Stack:
    
    def __init__(self):
        self.head = None
        self.tail = None
    
    def __str__(self):
        l = []
        print "___________________________________"
        print "Top of the stack = %s" % (self.head)
        current = self.head
    
        if not current:
            return "[]"

        while(current):
            l.append("%s" % (current, ))
            current = current.next
        
        return " --> ".join(l)
    
    def push(self, key, value):
        node = Node(key, value)
        if (self.head is None):
            self.head = node
            self.tail = node
            print "PUSH : element pushed to the stack, key: %s | value: %s" %(key, value)
        else:
            head = self.head
            self.head = node
            self.head.next = head
            print "PUSH : element pushed to the stack, key: %s | value: %s" %(key, value)
            
    def pop(self):
        if self.head is None:
            print "Stack is already empty"
        else:
            print "POP: element deleted from top of the stack, key: %s | value: %s" %(self.head.key, self.head.value)
            self.head = self.head.next
            
    
    def peek(self):
        if self.head is None:
            print "Stack is already empty"
        else:
            print "PEEK: key: %s | value: %s is on top of the stack" %(self.head.key, self.head.value)
            
def main():
    new_stack = Stack()
    new_stack.push(1, "hello")
    new_stack.push(2, "world")
    new_stack.push(5, "test")
    new_stack.push(7, "test2")
    new_stack.pop()
    new_stack.peek()
    print new_stack
    
if __name__ == '__main__':
    main()        
        
        
        
        
        