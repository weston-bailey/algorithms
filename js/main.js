import { LinkedList } from 'lib' 

console.log(LinkedList)

let newList0 = new LinkedList.Single()
let newList1 = new LinkedList.Single()


for(let i = 0; i < 1000; i++) {
  newList0.push(i % 10)
}

for(let i = 0; i < 10; i++) {
  newList1.push(i)
}

console.log(newList0.bounds());
console.log(newList0.findLast(2345))
console.log(LinkedList.isSorted(newList1))
console.log('~~~~~~~~~~~~~~~')
console.log(newList0.clear())
newList0.log()



