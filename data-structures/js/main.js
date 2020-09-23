import LinkedList from './lib/LinkedList.js';

let newList0 = new LinkedList();
let newList1 = new LinkedList();
let newList2 = new LinkedList();

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



// console.log(newList.get(12))