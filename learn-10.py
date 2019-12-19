# 10 - 字典与集合
# 类似Java或C++中Map对象

dictionary = {
    'a': 123,
    'b': 'hello'
}
print(dictionary)

""" 10.1.1 - 字典的创建和删除 """
# 10.1.1 - 1 创建空字典
dictionary = {}
dictionary = dict()
print(dictionary)

# 10.1.1 - 2 - 通过映射函数创建字典
# dictinary = dict(zip(list1, list2))
name = ['a', 'b', 'c']
value = ['hello', 'world', 'python']
dictionary = dict(zip(name, value))
print(dictionary)

# 10.1.1 - 3 - 通过给定的键值对创建字典
# dictinary = dict(key1 = value1, key2 = value2, ..., keyn = valuen)
dictionary = dict(a = 'hello', b = 'world', c = 'python')
print(dictionary)

# 10.1.1 - 4 - 使用dict对象的fromkeys()创建值为空的字典
# dictionary = dict.fromkeys(list1) list1：字典的键列表
name_list = ['a', 'b', 'c']
dictionary = dict.fromkeys(name_list)
print(dictionary)

# 10.1.1 - 5 - 通过元组和列表创建字典
# dictionary = { tuple: list }
tuple = ('a', 'b', 'c')
list = ['hello', 'world',  'python']
dictionary = { tuple: list }
print(dictionary)

# 10.1.1 - 6 删除字典
# del dictinary 或 dictionary.clear()
del dictionary
# print(dictionary)

""" 10.1.2 - 通过“键值对”访问字典 """
# dictionary[key]
# dictionary(key, [default])
dictionary = { 'a': 'hello'}
print(dictionary['a'])
print('你喜欢的水果是：', dictionary['fruit'] if '' in dictionary else '苹果')
print('爱好：', dictionary.get('hobby', '没有'))

""" 10.1.3 - 遍历字典 """
# dictionary.items()
dictionary = { 'a': 'hello', 'b': 'world' }
for item in dictionary.items():
    print(item)
for key,value in dictionary.items():
    print(key, value)
print(dictionary.keys())
print(dictionary.values())

""" 10.1.4 - 添加/修改/删除字典元素 """
# dictionary[key] = value
# del dictionary[key]
dictionary = dict()
dictionary['a'] = 'hello'
print(dictionary)
dictionary = dict((('a', 'hello'), ('b', 'world'), ('c', 'python')))
print(dictionary)
del dictionary['c']
print(dictionary)

if 'c' in dictionary:
    del dictionary['c']
print(dictionary)

""" 10.1.5 - 字典推导式 """
import random
random_dict = { i: random.randint(10, 100) for i in range(1, 5) }
print(random_dict)

""" 10.2 - 集合 """
# set:可变集合 frozenset: 不可变集合

""" 10.2.1 - 集合的创建 """
# 10.2.1 - 1 使用"{}"创建
# setname = { element1, element2, element3, ..., elementn }
set1 = { 'hello', 'world' }
set2 = { 1, 2, 3, 4, 5, 6 }
print(set1, set2)

# 10.2.1 - 2 使用set()创建集合
# setname = set(iteration)
set1 = set('hello world')
set2 = set([1, 2, 3, 4, 5])
set3 = set(('hello', 'world'))
set4 = set()
print(set1, set2, set3, set4)

# 10.2.2 - 集合的添加和删除
# 10.2.2 - 1 添加
# setname.add(element)
set1 = set(['hello', 'world'])
set1.add('python')
print(set1)

# 10.2.2 - 2 删除
# del pop() remove() clear()
set1 = set(['hello', 'world', 'python'])
print(set1)
set1.remove('hello')
print(set1)
set1.pop()
print(set1)
set1.clear()
print(set1)

# 10.2.3 - 集合的交集、并集、差集运算
# 交集：& 并集：| 差集：-
set1 = set(['php', 'python', 'javascript'])
set2 = set(['c', 'c++', 'java', 'python'])
print(set1, set2)
print(set1 & set2)
print(set1 | set2)
print(set1 - set2)