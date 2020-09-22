import LinkedList from './lib/LinkedList.js';

let newList = new LinkedList();

for(let i = 0; i < 35; i++) {
  newList.push(`my value is ${i}`)
}

// newList.log()

for(let i = 0; i < 45; i++) {
  console.log(newList.shift())
}

// newList.push(35)

// newList.log(33, 36)


// console.log('removed node', newList.remove(1));

console.log('~~~~~~~~~~~~~~~')



// newList.log()

// console.log(newList.get(12))