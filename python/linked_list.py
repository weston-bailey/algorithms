from lib import linked_list

test_list = linked_list.single()

test_list.push(0)
test_list.push(3)
test_list.push(1)
test_list.push(2)
test_list.push(3)

test_list.log('before for_each()')

found = test_list.find(83)

print('found', found)