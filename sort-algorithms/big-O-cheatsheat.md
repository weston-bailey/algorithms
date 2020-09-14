# Big O Notation Cheatsheet

Big O notation is used to describe the run time and space requirements of an algorithm, and how those requirements change based on input data

## O(1)

constant time f(1)

describes and algorithm that executes in the same time and space regardless of the input data

```python
# return a boolean after checking if a value is of None type
def is_none(value):
  return value is None
```

```javascript
// return a boolean after checking if a value is undefined 
const isUndefined = value => value === undefined ? true : false
```

## O(n)

linear time f(n)

describes and algorithm whose performance will grow linearly with the size of the dataset

```python
def find_in_list(value, li):
  for element in li:
    if value == element:
      return True
  return False
```

```javascript
// check and array for value and return with a boolean
const findInArray = (value, arr) => {
  for(i = 0; i < arr.length; i++) {
    if(arr[i] === value) return true;
  }
  return false;
}
```

## 0()




## References

[blog about big 0](https://justin.abrah.ms/computer-science/big-o-notation-explained.html)

[blog about big 0](https://rob-bell.net/2009/06/a-beginners-guide-to-big-o-notation/)






