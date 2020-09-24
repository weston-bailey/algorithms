import { LinkedList } from 'lib' 

let newList0 = new LinkedList.Single()
let newList1 = new LinkedList.Single()

for(let i = 0; i < 30; i++) {
  newList0.push(i % 10)
}

for(let i = 0; i < 10; i++) {
  newList1.push(i)
}

console.log(LinkedList.insertionSort(newList0))

newList0.log()



