from lib import linked_list

test_list = linked_list.single()

test_list.push(0)
test_list.push(1)
test_list.push(2)
test_list.push(3)

test_list.append(12354214356)

test_list.log()

test_list.pop()
test_list.log()

test_list.pop()
test_list.log()

test_list.pop()
test_list.log()

test_list.pop()
test_list.log()

test_list.pop()
test_list.log()

test_list.pop()
test_list.log()

test_list.pop()
test_list.log()

test_list.pop()
test_list.log()

print(test_list.get(0))

print('size', test_list.size)
