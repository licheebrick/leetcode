# Array
## Grammar in Python
### Sequence types: str, unicode, list, tuple, xrange...
* in, not in
* +, *
* s[i]
* s[i:j], s[i, k, j]
* len(), max(), min()
* s.index(x), s.count(x)

### string
#### Change:
* str.capitalize(), str.lower(), str.upper(), str.swapcase()
* str.expandtabs(tabsize)
* str.join()
* str.lstrip([chars]), str.strip([chars])
* str.partition()
* str.replace()
* str.split(), str.splitlines()

#### Find:
* str.count(substring)
* str.find() -1 if not found, str.index() ValueError if not found;


#### Judgement:
* str.endwith(), str.startwith()
* str.isalnum(), str.isalpha(), str.isdigit(), str.islower(), str.isupper(),  str.isspace(),

### Mutable Sequence Types: List & bytearray
* del s[i:k:j], s.remove(x)
* s \*= n
* s.pop([i])
* s.sort()

## Data Structure and Algorithms related to Array

## Summary of the leetcode category
### 414:找数列中第三大的数：（不重复）
1. set化，去除最大数；N时间，N空间
2. 存下三个数，逐个比较位移；N时间，1空间

### 找数列中第k大的数：不重复/重复

### 11： 最大水杯问题；【未解决】
从外往里推导。

### N-sum 问题；
1. 需要注意的问题：去重复，且N>2时去重复每一重循环都要考虑；
2. 可以直接用递归的方法做。
3. N=4时，可以分为2+2再用hash做；
4. 边界问题考虑了没？数不够多；数不够大；
