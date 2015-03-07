import java.util.ArrayList;

/*implementation of a stack using linked list. i.e stack size is dynamic*/

public class LinkedListStack {
	
	public class Node{
		
		private int key;
		private String value;
		private Node next;
		
		public Node(int key, String value){
			this.key = key;
			this.value = value;
		}
		
		public String toString(){
			return "[ (" + key + " , " + value + " )]";
		}
	}
	
	private Node head;
	private Node tail;
	
	public void StackAsLinkedList(){
		head = null;
		tail = null;
	}
	
	public void push(int key, String value){
		Node node = new Node(key, value);
		if (head == null){
			head = node;
			tail = node;
		} else {
			Node temp = head;
			head = node;
			head.next = temp;
		}
		System.out.println(String.format("Push : value %s was added to stack", node));
	}
	
	public void pushMany(Node[] nodes){
		for (Node node : nodes){
			push(node.key, node.value);
		}
	}
	
	public void pop(){
		if ( head != null){
			System.out.println(String.format("Pop : value %s was removed to stack", head));
			head = head.next;
		} else {
			System.out.println("Sorry but Stack is already empty.");
		}
	}
	
	public void popAll(){
		while (head != null){
			pop();
		}
	}
	
	public void peek(){
		if (head != null){
			System.out.println(String.format("Peek : value %s is on top of stack", head));
		} else {
			System.out.println("Sorry but Stack is already empty.");
		}
	}
	public String toString(){
		ArrayList<String> list = new ArrayList<String>();
		StringBuilder output = new StringBuilder();
		System.out.println("Top of the Stack : " + head);
		Node currentNode = head;
		
		if (currentNode == null){
			return output.toString();
		}
		while (currentNode != null){
			list.add(currentNode.toString());
			currentNode = currentNode.next;
		}
		for (String link : list){
			output.append(" --> " + link);
		}
		return output.toString();
	}
	
	public static void main(String [] args){
		LinkedListStack theStack = new LinkedListStack();
		theStack.push(5, "Data Structures");
		theStack.push(9, "Algorithms");
		theStack.push(8, "Operating Systems");
		theStack.push(7, "Data Mining");
		System.out.println(theStack.toString());
		theStack.peek();
		theStack.pop();
		System.out.println(theStack.toString());
	}

}