// https://www.notion.so/Linked-List-White-boarding-Problems-137e8a2cddb94e33a3b1f5f08bbfdac5

// a list node
class Node {
  constructor(value) {
    this.value = value
    this.next = null
  }
}

// linked list datatype
export default class LinkedList {
  constructor() {
    this.head = null;
    this.tail = null;
    this.size = 0;
  }

  // can be checked to see if list is empty 
  isEmpty() {
    return this.size === 0;
  }

  // return how many nodes there are
  length() {
    return this.size;
  }

  // print list with optional start and stop nodes, no return
  log(beg, end) {
    let start = beg || 0;
    let stop = end || this.size;

    if(this.isEmpty()) console.log(null)

    for(let i = start; i < stop; i++ ){
      let currentNode = this.get(i)
      console.log(currentNode)
    }
  }

  //returns value at index
  get(index){
    // add check for empty list, if true, return null
    if(this.isEmpty()) return null;
    // if index is out of range
    if(index > this.size || index < 0) {
      console.error(`Index out of range.`)
      return null;
    }

    // if index 0, return node.head
    if(index === 0) {
      return this.head
    }

    // if index == lenght - 1, node.tail
    if(index === this.size - 1) {
      return this.tail
    }

    // we want a node anywhere in the list minus head or tail
    let currentNode = this.head
    let iterator = 0
    while (iterator < index) {
      iterator++
      currentNode = currentNode.next
    }
    
    // return node found at index
    return currentNode
  }

  // add value to end of list
  push(value) {
    const newNode = new Node(value)

    if(this.isEmpty()){
      this.head = newNode;
      this.tail = newNode;
    } else {
      this.tail.next = newNode;
      this.tail = newNode;
    }
    this.size++
  }

  // remove last node form list
  pop() {
    // bail if the list if empty
    if(this.isEmpty()) return null;
    // node removed from list for return
    let removed;
    // find the second to last node
    let currentNode = this.get(this.size - 1);
    // grab the next node to return it after removal
    removed = currentNode.next;
    // nullify last node and update tail
    currentNode.next = null;
    this.tail = currentNode;
    // decrement list size
    this.size--;
    // return the node that was removed 
    return removed;
  }

  // remove first node from the list
  shift() {
    // return immediately is list is empty
    if(this.isEmpty()) return null;
    // node removed from list for return
    let removed;
    // grab the node to be returned
    removed = this.head;
    // set head to next 
    this.head = this.head.next;
    // decrement size
    this.size--;
    if(this.isEmpty()) this.tail = null;
    return removed;
  }

  // removes node at index and returns it
  remove(index) {
    // return immediately is list is empty
    if(this.isEmpty()) return null;
    // node removed from list for return
    let removed;

    // in case we are removing the head
    if(index === 0) {
      // grab the node to be returned
      removed = this.head;
      // set head to next 
      this.head = this.head.next;
      // decrement size
      this.size--;
      if(this.isEmpty()) this.tail = null;
      return removed;
    }

    // find the node right before the one we want to remove
    let currentNode = this.get(index - 1);
    // return if no node was found (likely a bad index)
    if(currentNode.next === null) return null;
    // grab the next node to return it after removal
    removed = currentNode.next;
    // if we are at the end of the list, update the tail accordingly
    if(this.size === index) {
      currentNode.next = null;
      this.tail = currentNode;
      // otherwise move the next pointer 
    } else {
      currentNode.next = currentNode.next.next;
    }
    // decrement list size
    this.size--;
    // return the node that was removed 
    return removed;
  } 

  // returns middle value of list
  middle() {
    let index = this.size - 1 
    if(index % 2 === 0) {
      // size is even
      return this.get(Math.floor(index * .5))
    }
    // size is odd
    return this.get((index * .5) + 1) 
  }
}



