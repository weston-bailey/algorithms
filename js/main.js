const ll = require('./lib/LinkedList')

let newList0 = new ll.SingleLinkedList();
let newList1 = new ll.SingleLinkedList();
let newList2 = new ll.SingleLinkedList();

for(let i = 0; i < 5; i++) {
  newList0.push(i)
}
for(let i = 0; i < 10; i++) {
  newList1.push(i)
}
for(let i = 0; i < 5; i++) {
  newList0.replace(i, i * i + 12342134)
}

let concatList = newList0.concat(newList0)
console.log(newList0.pop())
console.log('~~~~~~~~~~~~~~~')
newList0.log()




