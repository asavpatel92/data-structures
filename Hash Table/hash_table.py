#===============================================================================
# implementation of hash table using arrays
#===============================================================================
import numpy
import random
from math import floor

 #==============================================================================
 # If we think of a Hash Table as an array
 # then a hash function is used to generate
 # a unique key for every item in the array.
 # The position the item goes in is known
 # as the slot. Hashing doesn't work very well
 # in situations in which duplicate data
 # is stored. Also it isn't good for searching
 # for anything except a specific key. 
 # However a Hash Table is a data structure that 
 # offers fast insertion and searching capabilities.
 #==============================================================================

class HashTable:
    
    def __init__(self, hash_table_size):
        self.array = numpy.array([None] * hash_table_size)
        self.hash_table_size = hash_table_size 
        self.no_of_items = 0
        
    def __str__(self):
        table = []
        for element in self.array:
            if element != None:
                table.append(element)
            else:
                table.append("")
        return "".join(str(table))
    
    #===========================================================================
    # Simple Hash Function that puts values in the same
    # index that matches their value
    #===========================================================================

    def hash_function1(self, multiple_values):
        for value in multiple_values:
            self.array[int(value)] = value
        return self.array
    
    #===========================================================================
    #     Now let's say we have to hold values between 0 & 999
    #     but we never plan to have more than 15 values in all.
    #     It wouldn't make sense to make a 1000 item array, so
    #     what can we do?
    # 
    #     One way to fit these numbers into a 30 item array is
    #     to use the mod function. All you do is take the modulus
    #     of the value versus the array size
    #     The goal is to make the array big enough to avoid
    #     collisions, but not so big that we waste memory
    #===========================================================================
    def hash_function2(self, multiple_values):
        for value in multiple_values:
            
            #===================================================================
            # Create an index to store the value in by taking
            # the modulus
            #===================================================================
            array_index = int(value) % 27
            print "Modulus Index: %d  for value: %d " %(array_index, int(value))
            #===================================================================
            # Cycle through the array until we find an empty space    
            #===================================================================
            while( self.array[array_index] is not None):
                array_index += 1
                print "Collision occured try index: %d instead" %(array_index)
                #===============================================================
                # If we get to the end of the array go back to index 0
                #===============================================================
                array_index %= self.hash_table_size
            self.array[array_index] = value 
        return self.array
    
    #===========================================================================
    # Returns the value stored in the Hash Table
    #===========================================================================
    def find_key(self, key):
        #=======================================================================
        # Find the keys original hash key
        #=======================================================================
        array_index = int(key) % 27
        temp = array_index -1
        #=======================================================================
        # temp variable here is to stop going this function into infinite loop. 
        # it checks if array_index has completed whole cycle through array if it does then breaks out of loop 
        #=======================================================================
        while( self.array[array_index] is not None and array_index != temp ):
            if( self.array[array_index] is int(key)):
                #===============================================================
                # Found the key so return it
                #===============================================================
                print "Key found of value : %d at index : %d" %(int(key), array_index)
                return self.array[array_index]
            array_index += 1
            array_index = array_index % self.hash_table_size
        print "No key of value: %d found in table" %(key)
        #=======================================================================
        # Couldn't locate the key
        #=======================================================================
        return None

def main():
    hash_table_size = int(raw_input("Enter the size of Hash Table: "))
    new_hash_table = HashTable(hash_table_size)
    # items_to_add = random.sample(xrange(0, hash_table_size), hash_table_size - int(floor(hash_table_size/2)))
    # new_hash_table.hash_function1(items_to_add)
    items_to_add = random.sample(xrange(0, 999), hash_table_size)
    new_hash_table.hash_function2(items_to_add)
    print new_hash_table
    new_hash_table.find_key(99)
    
if __name__ == '__main__':
    main()