#===============================================================================
# implementation for binary tree
#===============================================================================
import Queue

class Node:
    
    def __init__(self,key, name):
        self.key = key
        self.name = name
        self.left_child = None
        self.right_child = None
    
    def __str__(self):
        return "%s has the key %s" %(self.name, self.key)
    
class BinaryTree:
    
    def __init__(self):
        self.root = None
        
    def add_node(self, key, name):
        #=======================================================================
        # Create a new Node and initialize it
        #=======================================================================
        new_node = Node(key, name)
        if( self.root is None):
            #===================================================================
            # If there is no root this becomes root
            #===================================================================
            self.root = new_node
        else:
            #===================================================================
            # Set root as the Node we will start with as we traverse the tree
            #===================================================================
            focus_node = self.root
            #===================================================================
            # Future parent for our new Node
            #===================================================================
            parent_node = None
            while(True):
                #===============================================================
                # root is the top parent so we start there
                #===============================================================
                parent_node = focus_node
                #===============================================================
                # Check if the new node should go on the left side of the parent node
                #===============================================================
                if( key < focus_node.key ):
                    #===========================================================
                    # Switch focus to the left child
                    #===========================================================
                    focus_node = focus_node.left_child
                    #===========================================================
                    # If the left child has no children
                    #===========================================================
                    if ( focus_node is None ):
                        #=======================================================
                        # then place the new node on the left of it
                        #=======================================================
                        parent_node.left_child = new_node
                        return
                #===============================================================
                # If we get here put the node on the right
                #===============================================================
                else:
                    focus_node = focus_node.right_child
                    #===========================================================
                    # If the right child has no children
                    #===========================================================
                    if ( focus_node is None ):
                        #=======================================================
                        # then place the new node on the right of it
                        #=======================================================
                        parent_node.right_child = new_node
                        return
                    
    def find_node(self, key):
        #Similar logic as adding the node
        if( self.root.key is key):
            return self.root
        else:
            focus_node = self.root
            while( focus_node.key is not key):
                if( key < focus_node.key ):
                    focus_node = focus_node.left_child
                else:
                    focus_node = focus_node.right_child
                if(focus_node is None):
                    print "No matching node found."
                    return None
            print "Node found : %s" %focus_node
            return focus_node
        
    #===========================================================================
    # All nodes are visited in ascending order Recursion is used to go to one node and then go to its child nodes and so forth                
    #===========================================================================
    def in_order_traverse(self, node):
        if ( node is not None):
            #===================================================================
            # Traverse the left node
            #===================================================================
            self.in_order_traverse(node.left_child)
            #===================================================================
            # Traverse the root node i.e currently focused node
            #===================================================================
            print "%s" %node
            #===================================================================
            # Traverse the right node
            #===================================================================
            self.in_order_traverse(node.right_child)
            
    def pre_order_traverse(self, node):
        if( node is not None):
            print "%s" %node
            self.pre_order_traverse(node.left_child)
            self.pre_order_traverse(node.right_child)
            
    def pre_order_traverse_iterative(self, node):
        if node is not None:
            temp_stack = []
            temp_stack.append(node)
            while len(temp_stack) > 0:
                value = temp_stack.pop()
                print value
                if value.right_child: 
                    #notice here we are pushing right child first into the stack because of LIFO structure of stack. 
                    #so left child will be took out first. 
                    temp_stack.append(value.right_child)
                if value.left_child:
                    temp_stack.append(value.left_child)
            return
            
    def post_order_traverse(self, node):
        if( node is not None):
            self.post_order_traverse(node.left_child)
            self.post_order_traverse(node.right_child)
            print "%s" %node

    #===========================================================================
    #     for eg. this is the tree:
    #                 10
    #                /   \  
    #               5    30
    #              / \   /  \ 
    #             4  8  28  42
    #     this is the formula for calculating the height of the tree : height(node) = max(height(node.Left_child), height(node.Right_child)) + 1
    #     here's how below method works : 
    #     height(10) = max(height(5), height(30)) + 1
    # 
    #     height(30) = max(height(28), height(42)) + 1
    #     height(42) = 1 (no children)
    #     height(28) = 1 (no children)
    #     
    #     height(5) =  max(height(4), height(8)) + 1
    #     height(4) = 1 (no children)
    #     height(8) = 1 (no children)
    #     so now,
    #     height(5)  = max(1, 1) + 1
    #     height(30) = max(1, 1) + 1
    #     height(10) = max(2, 2) + 1
    #     height(10) = 3 --> which is the height of the tree          
    #===========================================================================
    def get_height(self, node):
        if node is None:
            return 0
        else:
            return max(self.get_height(node.left_child), self.get_height(node.right_child)) + 1
        
    
    #this is similar to do a BFS on a tree it is also called level order traversal.   
    def print_binary_tree(self, node):
        queue = Queue.Queue()
        queue.put(node)
        queue.put("newline")
        while not queue.empty():
            node = queue.get()
            if node is "newline":
                print "\n"
                if not queue.empty():
                    queue.put("newline")
            else:
                print node , "    " ,
                if node.left_child is not None:
                    queue.put(node.left_child)
                if node.right_child is not None:
                    queue.put(node.right_child)

def main():
    new_binary_tree = BinaryTree()
    new_binary_tree.add_node(50, "Boss");
    new_binary_tree.add_node(25, "Vice President");
    new_binary_tree.add_node(15, "Office Manager");
    new_binary_tree.add_node(30, "Secretary");
    new_binary_tree.add_node(75, "Sales Manager");
    new_binary_tree.add_node(85, "Salesman 1");
    
    print "In Order Traversal:"
    new_binary_tree.in_order_traverse(new_binary_tree.root)
    
    print "\nPre Order Traversal:"
    new_binary_tree.pre_order_traverse(new_binary_tree.root)
    
    print "\nPost Order Traversal:"
    new_binary_tree.post_order_traverse(new_binary_tree.root)
    
    print "\nSearch for key: 25"
    new_binary_tree.find_node(25)
    
    print "Height of the tree:" , new_binary_tree.get_height(new_binary_tree.root)
    
    print "Printing the tree -->"
    new_binary_tree.print_binary_tree(new_binary_tree.root)

if __name__ == '__main__':
    main()