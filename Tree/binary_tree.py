#===============================================================================
# implementation for binary tree
#===============================================================================

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
            
    def post_order_traverse(self, node):
        if( node is not None):
            self.post_order_traverse(node.left_child)
            self.post_order_traverse(node.right_child)
            print "%s" %node

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

if __name__ == '__main__':
    main()