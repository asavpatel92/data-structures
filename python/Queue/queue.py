#===============================================================================
# implementation of Queue and Priority Queue using Arrays
#===============================================================================
import numpy
import random

class Queue:
    
#===============================================================================
#     Arrays, linked lists, trees, etc. are best for
#     data that represents real objects.
# 
#     Stacks & Queues are instead used to complete a 
#     task and are soon after discarded.
# 
#     Stacks & Queues
#     1. Allow only a single item to be added or removed at a time
#     2.  Queues allow access to the first item inserted (FIFO)
#===============================================================================
    
    #===========================================================================
    # initializing Queue with specific size
    #===========================================================================
    def __init__(self, queue_size):
        self.queue_size = queue_size
        self.queue_array = numpy.array([None] * queue_size)

        #Sets stack as empty
        self.front , self.rear, self.number_of_items = 0, 0, 0
        
        print "Queue of size %d initialized." %(self.queue_size)
        self.display_queue()
        
    def display_queue(self):
        print "[ " ,
        for element in self.queue_array:
            if element != None:
                if self.queue_array[self.rear - 1] == element and self.queue_array[self.front] == element:
                    print element, " [F] [R], " ,
                elif self.queue_array[self.front] == element:
                    print element, " [F], " ,
                elif self.queue_array[self.rear - 1] == element:
                    print element, " [R], " ,
                else:
                    print element, " ," ,
            else:
                print " ," ,
        print " ]"
        
    def insert(self, value):
        if self.number_of_items + 1 <= self.queue_size:
            self.queue_array[self.rear] = value
            self.rear += 1
            self.number_of_items += 1
            print "INSERT : %s added in Queue" %(value)
            self.display_queue()
        else:
            print "Sorry but Queue is already full."
            self.display_queue()
            
    def insert_many(self, multiple_value):
        for value in multiple_value:
            self.insert(value)

    #===========================================================================
    # This priority insert will add items in order from high to low
    #===========================================================================
    def priority_insert(self, value):
        if ( self.number_of_items == 0):
            self.insert(value)
        else:
            for i in range(self.number_of_items - 1, -1, -1):
                if( value > self.queue_array[i]):
                    self.queue_array[i + 1] = self.queue_array[i]
                else: break
            self.queue_array[self.front] = value
            self.rear += 1
            self.number_of_items += 1
        self.display_queue()            

    def priority_insert_many(self, multiple_value):
        for value in multiple_value:
            self.priority_insert(value)
    
    def remove(self):
        if self.number_of_items > 0:
            print "REMOVE : value %s was removed from Queue" %(self.queue_array[self.front])
            self.queue_array[self.front] = None
            self.front += 1
            self.number_of_items -= 1
            self.display_queue()
        else:
            print "Queue is already empty"
            self.display_queue()
    
    def peek(self):
        if self.number_of_items > 0:
            print " %s is the first element in Queue" %(self.queue_array[self.front])
        else:
            print "Queue is already empty"
            

queue_size = int(raw_input("Enter the Queue size : "))
new_queue = Queue(queue_size)
new_queue.insert_many(random.sample(xrange(0, 100), queue_size))
new_queue.remove()
new_queue.peek()
#new_queue.priority_insert_many(random.sample(xrange(0, 100), queue_size))


            