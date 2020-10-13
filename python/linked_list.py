from lib import linked_list

test_list = linked_list.single()

test_list.push(0)
test_list.push(1)
test_list.push(2)
test_list.push(3)

test_list.log()

list_get = test_list.get(3)

print('size', test_list.size)
print(list_get.value)