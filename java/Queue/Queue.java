/*implementation of Queue and Priority Queue using Arrays*/

/*
 	 Arrays, linked lists, trees, etc. are best for
     data that represents real objects.
 
     Stacks & Queues are instead used to complete a 
     task and are soon after discarded.
 
     Stacks & Queues
     1. Allow only a single item to be added or removed at a time
     2.  Queues allow access to the first item inserted (FIFO)
*/

public class Queue {
	
	private String[] queueArray;
	
	private int queueSize;
	
	//initializing queue as empty
	private int front, rear, numberOfItems = 0;
	
	public Queue(int size){
		queueSize = size;
		queueArray = new String[queueSize];
	}
	
	public void insert(String value){
		if (numberOfItems + 1 <= queueSize){
			queueArray[rear] = value;
			rear += 1;
			numberOfItems += 1;
			System.out.println(String.format("Insert : value %s was added to queue", value));
		} else{
			System.out.println("Sorry Queue is full.");
		}
	}
	
	public void insert_many(String[] values){
		for (String value : values){
			insert(value);
		}
	}
	
	public void remove(){
		if( numberOfItems >0 ){
			String value = queueArray[front];
			queueArray[front] = null;
			front += 1;
			numberOfItems -= 1;
			System.out.println(String.format("Remove : value %s was removed from queue", value));
		} else {
			System.out.println("Sorry Queue is already empty");
		}
	}
	
	public void peek(){
		if (numberOfItems > 0 ){
			System.out.println(String.format("Peek : value %s is in front of queue", queueArray[front]));
		} else {
			System.out.println("Sorry Queue is already empty");
		}
	}
	
//  This priority insert will add items in order from high to low
	public void priorityInsert(String input){
		int i;
		if(numberOfItems == 0){
			insert(input);
		} else {
			for(i = numberOfItems-1; i >= 0; i--){
				if(Integer.parseInt(input) > Integer.parseInt(queueArray[i])){
					queueArray[i+1] = queueArray[i];
				} else break; // Done shifting items in queue
			}
			queueArray[i+1] = input;
			rear += 1;
			numberOfItems += 1;
		}
	}
	
	public void priorityInsertMany(String[] values){
		for (String value : values){
			priorityInsert(value);
		}
	}

	public void displayQueue(){
		System.out.print("[ ");
		for( String value : queueArray){
			if (value != null){
				if (value == queueArray[front] && value == queueArray[rear]) {
					System.out.print(value + " [F] [R],");
				} else if ( value == queueArray[front]){
					System.out.print(value + " [F],");
				} else if (value == queueArray[rear - 1]){
					System.out.print(value + " [R],");
				} else {
					System.out.print(value + " ,");
				}
			} else{
				System.out.print(" ,");
			}
		}
		System.out.print(" ]\n");
	}
	
	public static void main(String [] args){		
		Queue theQueue = new Queue(10);
		theQueue.priorityInsert("16");
		theQueue.priorityInsert("25");
		theQueue.priorityInsert("10");
		theQueue.displayQueue();
		theQueue.remove();
		theQueue.peek();
		theQueue.displayQueue();		
	}
}