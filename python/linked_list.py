from lib import linked_list

test_list = linked_list.single()

test_list.push(0)
test_list.push(1)
test_list.push(2)
test_list.push(3)

# test_list.append(12354214356)

# test_list.log('before replace')

# print(test_list.replace(3, 5))
test_list.replace(4, 'replaced')


test_list.log('after replace')


# print(test_list.get(3))

# print('size', test_list.size)
