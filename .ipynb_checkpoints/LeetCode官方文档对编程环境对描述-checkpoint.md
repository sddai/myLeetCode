# LeetCode 官方文档对代码提交环境的描述
|Language|Version|Notes|
|:----  |:----  |:----  |
| Python3 | Python 3.10 | Most libraries are already imported automatically for your convenience, such as array, bisect, collections. If you need more libraries, you can import it yourself. <br/>For Map/TreeMap data structure, you may use sortedcontainers library. |

# 上述库函数的介绍
Python is a popular and versatile programming language that supports multiple paradigms such as object-oriented, functional, and procedural. Python also has a rich set of built-in data structures and libraries that can help with various tasks and problems. In this response, I will give a detailed illustration about Python's array, bisect, collections and sortedcontainers library with examples.

## **Array**

它将相同类型的元素序列存储在连续的内存块中。 数组对于有效存储和操作大量数据非常有用。 Python 没有原生数组类型，但它提供了定义`array.array`类的`array`模块，该类是 C 数组类型的一个薄包装器。 `array.array` 类支持基本操作，例如索引、切片、追加、扩展、插入、删除和排序。 它还具有在数组和字节对象、文件和列表之间进行转换的方法。

要创建数组对象，我们需要指定元素的类型代码和可选的初始值设定项。 类型代码指示元素的大小和种类，例如“b”表示有符号字节、“f”表示浮点数或“u”表示 Unicode 字符。 初始值设定项可以是提供数组初始值的可迭代对象，也可以是指定数组初始大小的整数。

An array is a data structure that stores a sequence of elements of the same type in a contiguous block of memory. Arrays are useful for storing and manipulating large amounts of data efficiently. Python does not have a native array type, but it provides the `array` module that defines the `array.array` class, which is a thin wrapper around the C array type¹. The `array.array` class supports basic operations such as indexing, slicing, appending, extending, inserting, removing, and sorting. It also has methods for converting between arrays and bytes objects, files, and lists.

To create an array object, we need to specify the type code of the elements and an optional initializer. The type code indicates the size and kind of the elements, such as `'b'` for signed bytes, `'f'` for floating point numbers, or `'u'` for Unicode characters. The initializer can be an iterable object that provides the initial values for the array, or an integer that specifies the initial size of the array. For example:

```python
# Import the array module
import array

# 构造一个空的int类型数组
arr = array.array('i')
# 指定内容
arr = array.array('i', [0, 1, 2, 3, 4, 6, 7, 8, 9, 100])

arr = array.array('f',[random.randrange(-10,10) for  _ in range(5)])
# array('f', [-10.0, -3.0, 8.0, -1.0, 7.0])

# Create an array of signed bytes with values 1, 2, 3 有符号字节数组
a = array.array('b', [1, 2, 3])

# Create an array of floating point numbers with size 5  大小为 5 的浮点数数组
b = array.array('f', 5)

# Print the arrays
print(a) # array('b', [1, 2, 3])
print(b) # array('f', [0.0, 0.0, 0.0, 0.0, 0.0])
```

## **Bisect**

`bisect`模块支持按排序顺序维护列表，而无需在每次插入后对列表进行排序。 对于具有昂贵比较操作的长项目列表，这可以是对线性搜索或频繁排序的改进²。 该模块称为 bisect，因为它使用基本的二分算法来完成其工作。 与搜索特定值的其他二分工具不同，该模块中的函数旨在定位插入点。 因此，这些函数从不调用“__eq__()”方法来确定是否已找到某个值。 相反，这些函数仅调用“__lt__()”方法，并将返回列表中值之间的插入点。

该模块提供四个函数：`bisect.bisect_left()`、`bisect.bisect_right()`、`bisect.insort_left()`和`bisect.insort_right()`。 前两个函数返回应插入值以维持排序顺序的索引，而后两个函数实际上将值插入到适当的位置。 左变体和右变体之间的区别在于，左变体返回值的任何现有条目之前的插入点，而右变体返回值的任何现有条目之后的插入点。

The `bisect` module provides support for maintaining a list in sorted order without having to sort the list after each insertion. For long lists of items with expensive comparison operations, this can be an improvement over linear searches or frequent resorting². The module is called bisect because it uses a basic bisection algorithm to do its work. Unlike other bisection tools that search for a specific value, the functions in this module are designed to locate an insertion point. Accordingly, the functions never call an `__eq__()` method to determine whether a value has been found. Instead, the functions only call the `__lt__()` method and will return an insertion point between values in a list.

The module provides four functions: `bisect.bisect_left()`, `bisect.bisect_right()`, `bisect.insort_left()`, and `bisect.insort_right()`. The first two functions return the index where a value should be inserted to maintain sorted order, while the last two functions actually insert the value at the appropriate position. The difference between left and right variants is that left variants return an insertion point before any existing entries of the value, while right variants return an insertion point after any existing entries of the value. For example:

```python
# Import the bisect module
import bisect

# Create a sorted list of numbers
l = [10, 20, 30, 40]

# Find the insertion point for 25 using left and right variants
i = bisect.bisect_left(l, 25)
j = bisect.bisect_right(l, 25)

# Print the indices
print(i) # 2
print(j) # 2

# Insert 25 using left and right variants
bisect.insort_left(l, 25)
bisect.insort_right(l, 25)

# Print the list
print(l) # [10, 20, 25, 25, 30, 40]
```

## **Collections**

[官方文档](https://docs.python.org/zh-cn/3.10/library/collections.html#)

`collections`模块提供了专门的容器类型，可以扩展内置容器的功能，例如列表、元组、字典和集合。 一些容器类型是：

- `collections.Counter`：一个 dict 子类，用于计算可哈希对象的数量。 它支持算术运算来组合和操作计数。
- `collections.deque`：一个类似列表的容器，支持从两端快速追加和弹出。 它还可以用作循环缓冲区。
- `collections.defaultdict`：一个 dict 子类，调用工厂函数为缺失的键提供默认值。
- `collections.namedtuple`：创建带有命名字段的元组子类的函数。
- `collections.OrderedDict`：一个 dict 子类，它记住键的插入顺序。
- `collections.ChainMap`：一个类似字典的类，它将多个映射组合在一起作为一个单元。
- `collections.UserDict`、`collections.UserList` 和 `collections.UserString`：提供更轻松的 dict、list 和 str 子类自定义的包装类。

The `collections` module provides specialized container types that extend the functionality of the built-in containers such as list, tuple, dict, and set³. Some of the container types are:

- `collections.Counter`: A dict subclass that counts hashable objects. It supports arithmetic operations to combine and manipulate counts.
- `collections.deque`: A list-like container that supports fast appends and pops from both ends. It can also be used as a circular buffer.
- `collections.defaultdict`: A dict subclass that calls a factory function to provide a default value for missing keys.
- `collections.namedtuple`: A function that creates a tuple subclass with named fields.
- `collections.OrderedDict`: A dict subclass that remembers the order of insertion of keys.
- `collections.ChainMap`: A dict-like class that groups multiple mappings together as a single unit.
- `collections.UserDict`, `collections.UserList`, and `collections.UserString`: Wrapper classes that provide easier customization of dict, list, and str subclasses.

To use these container types, we need to import the `collections` module and create instances of the desired classes. For example:

```python
# Import the collections module
import collections

# 从单词列表创建一个计数器对象 Create a counter object from a list of words
c = collections.Counter(['red', 'blue', 'green', 'red', 'yellow', 'blue'])

# Print the counter
print(c) # Counter({'red': 2, 'blue': 2, 'green': 1, 'yellow': 1})

# 从数字列表创建一个双端队列对象 Create a deque object from a list of numbers
d = collections.deque([1, 2, 3, 4])

# Append and pop values from both ends
d.append(5)
d.appendleft(0)
d.pop()
d.popleft()

# Print the deque
print(d) # deque([1, 2, 3, 4])

# 创建一个带有 lambda 函数的 defaultdict 对象作为默认工厂 Create a defaultdict object with a lambda function as the default factory
dd = collections.defaultdict(lambda: 'N/A')

# Assign some values to existing and non-existing keys
dd['a'] = 1
dd['b'] = 2
dd['c']

# Print the defaultdict
print(dd) # defaultdict(<function <lambda> at 0x7f9c8c6f6f70>, {'a': 1, 'b': 2, 'c': 'N/A'})

# 创建一个名为 Point 的命名元组类型，其中包含字段 x 和 y Create a namedtuple type called Point with fields x and y
Point = collections.namedtuple('Point', ['x', 'y'])

# Create a point object from two coordinates
p = Point(3, 4)

# Access the fields by name or index
print(p.x) # 3
print(p[1]) # 4

# 从键值对列表创建 有序字典 对象  Create an OrderedDict object from a list of key-value pairs
od = collections.OrderedDict([('a', 1), ('b', 2), ('c', 3)])   #可以用于 LRU cache

# Print the OrderedDict
print(od) # OrderedDict([('a', 1), ('b', 2), ('c', 3)])

# OrderedDict的两个方法：
# popitem(last=True)
# The popitem() method for ordered dictionaries returns and removes a (key, value) pair. The pairs are returned in LIFO order if last is true or FIFO order if false.

# move_to_end(key, last=True)
# Move an existing key to either end of an ordered dictionary. The item is moved to the right end if last is true (the default) or to the beginning if last is false. Raises KeyError if the key does not exist:

d = OrderedDict.fromkeys('abcde')
d.move_to_end('b')
''.join(d)

d.move_to_end('b', last=False)
''.join(d)

# 从两个字典创建一个 ChainMap 对象 Create a ChainMap object from two dictionaries
cm = collections.ChainMap({'a': 1, 'b': 2}, {'c': 3, 'd': 4})

# Print the ChainMap
print(cm) # ChainMap({'a': 1, 'b': 2}, {'c': 3, 'd': 4})

# ChainMap:
import builtins  # 这是内置函数
from collections import ChainMap

local_vars = {"x": 1, "y": 2}
global_vars = {"z": 3, "w": 4}
builtin_vars = vars(builtins)  # vars列出了builtins的属性及其属性值，如果不带参数vars()直接返回当前位置的属性和属性值，类似于locals()

chain = ChainMap(local_vars, global_vars, builtin_vars)
print(chain["x"]) # 1
print(chain["z"]) # 3
print(chain["len"]) # <built-in function len>
```

## **SortedContainers**

SortedContainers 是一个外部库，提供列表、字典和集合的排序变体。 它是用纯 Python 编写的，速度与 C 扩展⁴ 一样快。 该库包含三种容器类型：“sortedcontainers.SortedList”、“sortedcontainers.SortedDict”和“sortedcontainers.SortedSet”。 这些容器类型与其内置对应容器类型类似，但它们按排序顺序维护其元素。 它们还支持快速索引、切片、搜索和插入操作。 它们是使用二叉搜索树和跳跃列表来实现的。

SortedContainers is an external library that provides sorted variants of list, dict, and set. It is written in pure Python and is fast as C-extensions⁴. The library contains three container types: `sortedcontainers.SortedList`, `sortedcontainers.SortedDict`, and `sortedcontainers.SortedSet`. These container types are similar to their built-in counterparts, but they maintain their elements in sorted order. They also support fast indexing, slicing, searching, and insertion operations. They are implemented using binary search trees and skip lists.

To use these container types, we need to install the `sortedcontainers` library using `pip` or `conda` and import the `sortedcontainers` module. For example:

```python
# Install the sortedcontainers library using pip
pip install sortedcontainers

# Import the sortedcontainers module
import sortedcontainers

# Create a SortedList object from a list of numbers
sl = sortedcontainers.SortedList([3, 1, 2, 5, 4])

# Print the SortedList
print(sl) # SortedList([1, 2, 3, 4, 5], load=1000)

# Create a SortedDict object from a dict of words and frequencies
sd = sortedcontainers.SortedDict({'red': 2, 'blue': 2, 'green': 1, 'yellow': 1})

# Print the SortedDict
print(sd) # SortedDict({'blue': 2, 'green': 1, 'red': 2, 'yellow': 1})

# Create a SortedSet object from a set of letters
ss = sortedcontainers.SortedSet('abracadabra')

# Print the SortedSet
print(ss) # SortedSet(['a', 'b', 'c', 'd', 'r'], key=None, load=1000)
```

😊

Source: 
 - (1) bisect — Array bisection algorithm — Python 3.12.0 documentation. https://docs.python.org/3/library/bisect.html.
 - (2) Sorted List — Sorted Containers 2.4.0 documentation - Grant Jenks. https://grantjenks.com/docs/sortedcontainers/sortedlist.html.
 - (3) Python Sorted Containers | Napath's Blog. https://blog.napath.com/index.php/2020/09/30/python-sorted-containers/.
 - (4) Python - bisect — Array bisection algorithm Source code: Lib/bisect.py .... https://runebook.dev/en/docs/python/library/bisect.