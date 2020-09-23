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

  // just for fun
  toString() {
    return `[object ${this.constructor.name}]`
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
      let currentNode = this.get(i);
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
    //  make a new node
    const newNode = new Node(value)

    // populate head and tail if list if empty
    if(this.isEmpty()){
      this.head = newNode;
      this.tail = newNode;
    // set the tail's next to the new node and place the new node at the tail
    } else {
      this.tail.next = newNode;
      this.tail = newNode;
    }
    this.size++
  }

  // add a node to the beginning of the list
  append(value) {
    // make a new node
    const newNode = new Node(value);

    // update head and tail if list if empty
    if(this.isEmpty()){
      this.head = newNode;
      this.tail = newNode;
    // asiign head to the next of the new node and place the new node at the head
    } else {
      newNode.next = this.head;
      this.head = newNode
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
    if(currentNode === null) return null;
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

  // replace a value at an index
  replace(index, value) {
    // if list is empty return with an error
    if(this.isEmpty()) return console.error('list is empty');
    // make a new node
    const newNode = new Node(value);

    // handle case if the index is the head 
    if(index === 0) {
     newNode.next = this.head.next;
     this.head = newNode;
     return
    }

    // find the node before the index
    let currentNode = this.get(index - 1);
    // return if no node at that index is found
    if(currentNode === null) return null;
    // if we are at the end of the list, update the tail
    if(this.size === index) {
      currentNode.next = newNode;
      this.tail = newNode;
    } else {
      newNode.next = currentNode.next.next;
      currentNode.next = newNode;
    }
    return
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

  // concatenate multiple lists and return a new list (doesn't have to include self)
  concat(...args) {
    let newList = new LinkedList();

    // make sure arguments are all lists and add up the total length
    for(let i = 0; i < args.length; i++){
      if(args[i].toString() != '[object LinkedList]') return console.error('arguments must be of type LinkedList');

      // iterate over current list and push it to new list
      let currentNode = args[i].head
      let j = 0;
      while(j < args[i].length()){
        newList.push(currentNode.value)
        currentNode = currentNode.next;
        j++;
      }
    }
    return newList
  }

  // returns the highest and lowest values found in the list...only for number values presently
  bounds() {
    if(this.isEmpty()) return null;
    // maximum boundaries possible
    let min = new Node(Number.POSITIVE_INFINITY);
    let max = new Node(Number.NEGATIVE_INFINITY);

    let currentNode = this.head;
    let iterator = 0;
    while(iterator < this.size) {
      if(currentNode.value < min.value) min.value = currentNode.value;
      console.log(currentNode.value, min.value)
      if(currentNode.value > max.value) max.value = currentNode.value;
      currentNode = currentNode.next;
      iterator++ 
    }
    let bounds = new LinkedList()
    bounds.push(min.value)
    bounds.push(max.value)
    return bounds
  }
}




