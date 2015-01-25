#===============================================================================
# implementation of Stack using Array
#===============================================================================
import numpy
import random

class Stack:
    
#===============================================================================
#     Arrays, linked lists, trees, etc. are best for
#     data that represents real objects.
# 
#     Stacks & Queues are instead used to complete a 
#     task and are soon after discarded.
# 
#     Stacks & Queues
#     1. Allow only a single item to be added or removed at a time
#     2. Stacks allow access to the last item inserted (LIFO)
#===============================================================================

    
    #===========================================================================
    # initializing stack with specific size
    #===========================================================================
    def __init__(self, stack_size):
        self.stack_array = numpy.array([None] * stack_size)
        self.stack_size = stack_size
        
        #Sets stack as empty
        self.top_of_stack = -1
        print "Stack with size %d initialized" %(stack_size)
        self.display_stack()
        
    def display_stack(self):
        print "[ " ,
        for element in self.stack_array:
            if element != None:
                print element , " ," ,
            else:
                print " ," ,
        print "]"
    
    def push(self, input):
        if self.top_of_stack + 1 < self.stack_size:
            self.top_of_stack += 1
            self.stack_array[self.top_of_stack] = input
            print "PUSH : value %s added to stack" %(input)
        else:
            print "Sorry but stack is already full."
        self.display_stack()
        
    def push_many(self, multiple_values):
        for value in multiple_values:
            self.push(value)
    
    def pop(self):
        if( self.top_of_stack >= 0):
            print "POP : value %s removed from stack" %(self.stack_array[self.top_of_stack])
            self.stack_array[self.top_of_stack] = None
            self.top_of_stack -= 1
            self.display_stack()
        else:
            print "Stack is already empty"
    
    def pop_all(self):
        for i in len(self.stack_array):
            self.pop()
            
    def peek(self):
        if ( self.top_of_stack >= 0):
            print "Top of the stack is %s" %(self.stack_array[self.top_of_stack])
        else:
            print "Stack is already empty"

stack_size = int(raw_input("Enter the size of the stack : "))
new_stack = Stack(stack_size)

#===============================================================================
# #Add many to the stack
new_stack.push_many(random.randint(0, 100) for _ in range(stack_size))
#===============================================================================

#===============================================================================
# # Look at the top value on the stack
new_stack.peek()
#===============================================================================

#===============================================================================
# # Remove values from the stack (LIFO)
new_stack.pop()
#===============================================================================

#Remove all from the stack
#new_stack.pop_all()

            
    
                        