// Arrays, linked lists, trees, etc. are best for
// data that represents real objects.

// Stacks & Queues are instead used to complete a 
// task and are soon after discarded.

// Stacks
// 1. Allow only a single item to be added or removed at a time
// 2. Stacks allow access to the last item inserted (LIFO)

public class Stack {

	private String[] stackArray;

	private int stackSize;

	// Sets stack as empty
	private int topOfStack = -1;

	public Stack(int size) {
		stackSize = size;
		stackArray = new String[stackSize];
		System.out.println("Stack of size " + stackSize + " initialized.");
	}
	
	public void push(String value){
		if( topOfStack + 1 < stackSize){
			topOfStack += 1;
			stackArray[topOfStack] = value;
		} else{
			System.out.println("Sorry but stack is full");
		}
		System.out.println(String.format("Push : value %s was added to stack", value));
	}
	
	public void pushMany(String[] values){
		for (String value : values){
			push(value);
		}
	}
	
	public void pop(){
		if ( topOfStack >= 0){
			String value = stackArray[topOfStack];
			stackArray[topOfStack] = null;
			topOfStack -= 1;
			System.out.println(String.format("Pop : value %s was removed to stack", value));
		} else{
			System.out.println("Sorry but stack is already empty");
		}
	}
	
	public void popAll(){
		while( topOfStack != -1){
			pop();
		}
	}
	
	public void peek(){
		if ( topOfStack >= 0){
			System.out.println(String.format("Peek : value %s is on top of stack", stackArray[topOfStack]));
		} else{
			System.out.println("Sorry but stack is already empty.");
		}
	}

	public void displayStack() {
		System.out.print("[ ");
		for (String value : stackArray) {
			if (value != null) {
				System.out.print(value + " ,");
			} else {
				System.out.print(" ,");
			}
		}
		System.out.print(" ] \n");
	}

	public static void main(String[] args) {
		Stack theStack = new Stack(10);
		
		theStack.push("10");
		theStack.push("17");
		theStack.push("13");
		
		// Look at the top value on the stack
		
		theStack.peek();
		
		// Remove values from the stack (LIFO)
		
		theStack.pop();
		theStack.pop();
		
		theStack.displayStack();

		// Add many to the stack
		
		theStack.pushMany(new String[]{"1", "2", "3", "4"});
		theStack.displayStack();
	}
}