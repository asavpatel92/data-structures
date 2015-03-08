/*implementation for binary tree*/

public class BinaryTree {

	class Node {

		private int key;
		private String value;
		private Node leftChild;
		private Node rightChild;

		public Node(int key, String value) {
			this.key = key;
			this.value = value;
		}

		public String toString() {
			StringBuilder s = new StringBuilder();
			s.append(value + " has the key " + this.key);
			return s.toString();
		}
	}

	private Node root;

	public BinaryTree() {
		root = null;
	}

	public void addNode(int key, String value) {
		// Create a new Node and initialize it
		Node node = new Node(key, value);
		if (root == null) {
			// If there is no root this becomes root
			root = node;
		} else {
			// Set root as the Node we will start with as we traverse the tree
			Node currentNode = root;
			// Future parent for our new Node
			Node parentNode = null;
			while (true) {
				// root is the top parent so we start there
				parentNode = currentNode;
				// Check if the new node should go on the left side of the
				// parent node
				if (key < currentNode.key) {
					// Switch focus to the left child
					currentNode = currentNode.leftChild;
					// If the left child has no children
					if (currentNode == null) {
						// then place the new node on the left of it
						parentNode.leftChild = node;
						return;
					}
				} else {
					// If we get here put the node on the right
					currentNode = currentNode.rightChild;
					if (currentNode == null) {
						parentNode.rightChild = node;
						return;
					}
				}

			}
		}
	}

	public void findNode(int key) {
		if (root != null) {
			Node currentNode = root;
			while (currentNode.key != key) {
				if (key < currentNode.key) {
					currentNode = currentNode.leftChild;
				} else {
					currentNode = currentNode.rightChild;
				}
				if (currentNode == null) {
					System.out.println("No matching node found");
					return;
				}
			}
			System.out.println("Found node : " + currentNode);

		} else {
			System.out.println("Sorry, Tree is empty.");
			return;
		}
	}

	public int getHeight(Node node) {
		if (node == null) {
			return 0;
		} else {
			return Math.max(getHeight(node.leftChild),
					getHeight(node.rightChild)) + 1;
		}
	}

	public void inOrderTraverse(Node node) {
		if (node != null) {
			inOrderTraverse(node.leftChild);
			System.out.println(node);
			inOrderTraverse(node.rightChild);
		}
	}

	public void preOrderTraverse(Node node) {
		if (node != null) {
			System.out.println(node);
			preOrderTraverse(node.leftChild);
			preOrderTraverse(node.rightChild);
		}
	}

	public void preOrderTraverse_Iterative(Node node) {
		if (node != null) {
			java.util.Stack<Node> tempStack = new java.util.Stack<Node>();
			tempStack.push(node);
			while (tempStack.isEmpty()) {
				Node value = tempStack.pop();
				System.out.println(value);
				if (value.rightChild != null) {
					tempStack.push(value.rightChild);
				}
				if (value.leftChild != null) {
					tempStack.push(value.leftChild);
				}
			}
		}
	}

	public void postOrderTraverse(Node node) {
		if (node != null) {
			postOrderTraverse(node.leftChild);
			postOrderTraverse(node.rightChild);
			System.out.println(node);
		}
	}

	public String toString() {
		StringBuilder s = new StringBuilder();
		java.util.Queue<Node> queue = new java.util.LinkedList<Node>();
		queue.add(root);
		queue.add(new Node(1, "newline"));
		while (!queue.isEmpty()) {
			Node node = queue.poll();
			if (node.value == "newline") {
				s.append("\n");
				if (!queue.isEmpty()) {
					queue.add(new Node(1, "newline"));
				}
			} else {
				s.append(node.toString() + "		");
				if (node.leftChild != null) {
					queue.add(node.leftChild);
				}
				if (node.rightChild != null) {
					queue.add(node.rightChild);
				}
			}
		}
		return s.toString();
	}

	public static void main(String[] args) {
		BinaryTree binaryTree = new BinaryTree();
		binaryTree.addNode(50, "Boss");
		binaryTree.addNode(25, "Vice President");
		binaryTree.addNode(15, "Office Manager");
		binaryTree.addNode(30, "Secretary");
		binaryTree.addNode(75, "Sales Manager");
		binaryTree.addNode(85, "Salesman 1");
		System.out.println("In Order Traversal:");
		binaryTree.inOrderTraverse(binaryTree.root);
		System.out.println("Pre Order Traversal:");
		binaryTree.preOrderTraverse_Iterative(binaryTree.root);
		System.out.println("Post Order Traversal:");
		binaryTree.postOrderTraverse(binaryTree.root);
		System.out.println("Search for key: 25");
		binaryTree.findNode(25);
		System.out.println("Printing the tree -->");
		System.out.println(binaryTree.toString());
		System.out.println("Height of the tree : " + binaryTree.getHeight(binaryTree.root));
	}

}