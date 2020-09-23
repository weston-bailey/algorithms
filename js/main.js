const ll = require('./lib/LinkedList')

let newList0 = new ll.SingleLinkedList();
let newList1 = new ll.SingleLinkedList();
let newList2 = new ll.SingleLinkedList();

for(let i = 0; i < 10; i++) {
  newList0.push(i)
}
for(let i = 0; i < 10; i++) {
  newList1.push(i)
}
for(let i = 10; i > 0; i--) {
  newList2.push(i)
}

let concatList = newList0.concat(newList0, newList1, newList2)
concatList.log()
console.log('~~~~~~~~~~~~~~~')

console.log(concatList.bounds())