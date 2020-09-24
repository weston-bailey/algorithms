// check if a linked list is sorted
module.exports = function isSorted(list) {
  if(list.isEmpty()) return null;
  let currentNode = list.head;
  while(currentNode.next){
    if(currentNode.value > currentNode.next.value) return false;
    currentNode = currentNode.next;
  }
  return true
}