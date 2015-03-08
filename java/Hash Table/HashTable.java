	// If we think of a Hash Table as an array
	// then a hash function is used to generate
	// a unique key for every item in the array.
	// The position the item goes in is known
	// as the slot. Hashing doesn't work very well
	// in situations in which duplicate data
	// is stored. Also it isn't good for searching
	// for anything except a specific key. 
	// However a Hash Table is a data structure that 
	// offers fast insertion and searching capabilities.

public class HashTable {
		Integer[] theArray;
		int arraySize;
		int itemsInArray = 0;

		public HashTable(int size) {
			arraySize = size;
			theArray = new Integer[size];
		}

		// Simple Hash Function that puts values in the same
		// index that matches their value
		public void hashFunction1(Integer[] array) {
			for (int n = 0; n < array.length; n++) {
				Integer newElementVal = array[n];
				theArray[newElementVal.intValue()] = newElementVal;
			}
		}

		// Now let's say we have to hold values between 0 & 999
		// but we never plan to have more than 15 values in all.
		// It wouldn't make sense to make a 1000 item array, so
		// what can we do?

		// One way to fit these numbers into a 30 item array is
		// to use the mod function. All you do is take the modulus
		// of the value versus the array size

		// The goal is to make the array big enough to avoid
		// collisions, but not so big that we waste memory

		public void hashFunction2(Integer[] array) {
			for (int n = 0; n < array.length; n++) {
				Integer newElementVal = array[n];
				// Create an index to store the value in by taking
				// the modulus
				int arrayIndex = newElementVal.intValue() % 29;
				System.out.println("Modulus Index= " + arrayIndex + " for value "+ newElementVal);
				// Cycle through the array until we find an empty space
				while (theArray[arrayIndex] != null) {
					++arrayIndex;
					System.out.println("Collision Try " + arrayIndex + " Instead");
					// If we get to the end of the array go back to index 0
					arrayIndex %= arraySize;
				}
				theArray[arrayIndex] = newElementVal;
			}
		}

		// Returns the value stored in the Hash Table
		public int findKey(int key) {
			// Find the keys original hash key
			int arrayIndexHash = key % 29;
			while (theArray[arrayIndexHash] != null) {
				if (theArray[arrayIndexHash] == key) {
					// Found the key so return it
					System.out.println(key + " was found in index "+ arrayIndexHash);
					return theArray[arrayIndexHash];
				}
				// Look in the next index
				++arrayIndexHash;
				// If we get to the end of the array go back to index 0
				arrayIndexHash %= arraySize;
			}
			// Couldn't locate the key
			System.out.println("Sorry but key was not found in table.");
			return -1;
		}

		public String toString(){
			StringBuilder s = new StringBuilder();
			s.append("[ ");
			int i = 0;
			for (Integer element : theArray){
				if (element != null){
					s.append("index : " + i + " - value : "+element + ", ");
				} else {
					s.append("index : " + i + " - value : "+" , ");
				}
				i += 1;
			}
			s.append(" ]");
			return s.toString();
		}

		public static void main(String[] args) {

			HashTable hashTable = new HashTable(30);

			// Simplest Hash Function

			// Integer[] elementsToAdd = { 1, 5, 17, 21, 26 };

			// hashTable.hashFunction1(elementsToAdd);

			// Mod Hash Function
			// This contains exactly 30 items to show how collisions
			// will work

			Integer[] elementsToAdd2 = { 100, 510, 170, 214, 268, 398,
					235, 802, 900, 723, 699, 1, 16, 999, 890,
					725, 998, 978, 988, 990, 989, 984, 320, 321,
					400, 415, 450, 50, 660, 624 };
			
			hashTable.hashFunction2(elementsToAdd2);

			// Locate the value 660 in the Hash Table
			hashTable.findKey(660);
			System.out.println(hashTable.toString());

		}
	}