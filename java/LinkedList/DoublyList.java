import java.util.ArrayList;

public class DoublyList {
	
	class Node{
		
		private int key;
		private String value;
		private Node next;
		private Node previous;
		
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
	
	public DoublyList(){
		head = null;
		tail = null;
	}
	
	public void addNode(int key, String value){
		Node node = new Node(key, value);
		if (head == null){
			head = node;
			tail = node;
		} else {
			tail.next = node;
			node.previous = tail;
			tail = node;			
		}
	}
	
	public void addNodeToFront(int key, String value){
		Node node = new Node(key, value);
		if ( head == null ){
			head = node;
			tail = node;
		} else {
			Node oldHead = head;
			head.previous = node;
			head = node;
			head.next = oldHead;
		}
		
	}
	
	public void removeFirst(){
		if (head != null){
			System.out.println("First Link deleted!." + head);
			head = head.next;
		} else {
			System.out.println("Linked list is already empty.");
		}
	}
	
	public void removeLast(){
		if (tail != null){
			System.out.println("Last Link Deleted : " + tail.toString());
			tail = tail.previous;
			tail.next = null;
		}
	}
	
	public void removeLink(int key){
		if (head != null){
			Node currentNode = head;
			while (currentNode.key != key){
				if (currentNode.next == null){
					System.out.println("Link not found!");
					return;
				}
				currentNode = currentNode.next;
			}
			System.out.println("Link Deleted : " + currentNode.toString());
			currentNode.previous.next =currentNode.next;
		} else {
			System.out.println("Linked list is already empty.");
			return;
		}
	}
	
	public void findLink(int key){
		if (head != null){
			Node currentNode = head;
			while (head.key != key){
				if (currentNode.next == null){
					System.out.println("Link not found!");
					return;
				}
				currentNode = currentNode.next;
			}
			System.out.println("Link found : " + currentNode.toString());
			return;
		} else {
			System.out.println("Linked list is already empty.");
			return;
		}
	}
	
	public String toString(){
		ArrayList<String> list = new ArrayList<String>();
		StringBuilder output = new StringBuilder();
		System.out.println("Head = " + head);
		System.out.println("Tail = " + tail);
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
		DoublyList theLinkedList = new DoublyList();
		theLinkedList.addNode(5, "Data Structures");
		theLinkedList.addNode(9, "Algorithms");
		theLinkedList.addNode(8, "Operating Systems");
		theLinkedList.addNode(7, "Data Mining");
		System.out.println(theLinkedList.toString());
		theLinkedList.removeFirst();
		System.out.println(theLinkedList.toString());
		theLinkedList.findLink(8);
		theLinkedList.removeLast();
		System.out.println(theLinkedList.toString());
	}

}