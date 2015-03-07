import java.util.ArrayList;

/*implementation for Singly Linked List*/

public class SinglyList {
	
	class Node{
		
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
	
	public SinglyList(){
		head = null;
		tail = null;
	}
	
	public void addNode(int key, String value){
		Node node = new Node(key, value);
		/*if list is empty make this node the first node in list*/
		if (head == null){
			head = node;
			tail = node;
		} else {
			/*place node we are inserting right next to tail of the list and slide the tail to the latest node inserted*/
			tail.next = node;
			tail = node;
		}
	}
	
	public void removeFirst(){
		/*make the next node to the head as head so automatically head will be removed as there will be no address to reference it*/
		if (head != null){
			head = head.next;
			System.out.println("First node removed!");
		} else {
			System.out.println("Linked list is already empty");
		}
	}
	
	public void findLink(int key){
		if (head != null){
			Node currentNode = head;
			while (currentNode.key != key){
				/*this means we have reached to the end of the list and still our desired not has not been found yet*/
				if (currentNode.next == null){
					System.out.println("Link not found!");
				}
				currentNode = currentNode.next;
			}
			System.out.println("Link found : " + currentNode.toString());
		} else {
			System.out.println("Linked list is already empty");
		}
	}
	
	public void removeLink(int key){
		if ( head != null){
			Node currentNode = head;
			Node previousNode = head;
			while (currentNode.key != key){
				if (currentNode.next == null){
					System.out.println("Link not found!");
				}
				previousNode = currentNode;
				currentNode = currentNode.next;
			}
			System.out.println("Link Deleted : " + currentNode.toString());
			/*this will delete the node which is in middle 
			i.e current node [previous node]-->[current node]-->[] to [previous node]-->[current node's next]*/
			previousNode.next = currentNode.next;
		} else {
			System.out.println("Linked list is already empty");
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
		SinglyList theLinkedList = new SinglyList();
		theLinkedList.addNode(5, "Data Structures");
		theLinkedList.addNode(9, "Algorithms");
		theLinkedList.addNode(8, "Operating Systems");
		theLinkedList.addNode(7, "Data Mining");
		System.out.println(theLinkedList.toString());
		theLinkedList.removeFirst();
		System.out.println(theLinkedList.toString());
		theLinkedList.findLink(8);
		theLinkedList.removeLink(8);
		System.out.println(theLinkedList.toString());
	}

}