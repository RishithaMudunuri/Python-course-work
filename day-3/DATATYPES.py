Python 3.11.9 (tags/v3.11.9:de54cf5, Apr  2 2024, 10:12:12) [MSC v.1938 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
a=10
type(a)
<class 'int'>
l=[]
l=list()
type(l)
<class 'list'>
t=()
t=(1,2,3,4,5)
type(t)
<class 'tuple'>
str=madhu
Traceback (most recent call last):
  File "<pyshell#8>", line 1, in <module>
    str=madhu
NameError: name 'madhu' is not defined
str='madhu'
str='''madhu'''
status=True
type(status)
<class 'bool'>
a=none
Traceback (most recent call last):
  File "<pyshell#13>", line 1, in <module>
    a=none
NameError: name 'none' is not defined. Did you mean: 'None'?
a=None

==================================================================================== RESTART: Shell ====================================================================================
a=10
a=10
int(a)
10
bool(a)
True
str(a)
'10'
complex(a)
(10+0j)
float(a)
10.0
set(a)
Traceback (most recent call last):
  File "<pyshell#22>", line 1, in <module>
    set(a)
TypeError: 'int' object is not iterable
list(a)
Traceback (most recent call last):
  File "<pyshell#23>", line 1, in <module>
    list(a)
TypeError: 'int' object is not iterable
tuple(a)
Traceback (most recent call last):
  File "<pyshell#24>", line 1, in <module>
    tuple(a)
TypeError: 'int' object is not iterable
a=10.2
int(a)
10
complex(a)
(10.2+0j)
str(a)
'10.2'
bool(a)
True
set(a)
Traceback (most recent call last):
  File "<pyshell#30>", line 1, in <module>
    set(a)
TypeError: 'float' object is not iterable
tuple(a)
Traceback (most recent call last):
  File "<pyshell#31>", line 1, in <module>
    tuple(a)
TypeError: 'float' object is not iterable
list(a)
Traceback (most recent call last):
  File "<pyshell#32>", line 1, in <module>
    list(a)
TypeError: 'float' object is not iterable
a=i+2j
Traceback (most recent call last):
  File "<pyshell#33>", line 1, in <module>
    a=i+2j
NameError: name 'i' is not defined. Did you mean: 'id'?
a=1+4
int(a)
5
float(a)
5.0
str(a)
'5'
bool(a)
True
set(a)
Traceback (most recent call last):
  File "<pyshell#39>", line 1, in <module>
    set(a)
TypeError: 'int' object is not iterable
list(a)
Traceback (most recent call last):
  File "<pyshell#40>", line 1, in <module>
    list(a)
TypeError: 'int' object is not iterable
tuple(a)
Traceback (most recent call last):
  File "<pyshell#41>", line 1, in <module>
    tuple(a)
TypeError: 'int' object is not iterable
none(a)
Traceback (most recent call last):
  File "<pyshell#42>", line 1, in <module>
    none(a)
NameError: name 'none' is not defined. Did you mean: 'None'?
>>> a='rishi'
>>> int(a)
Traceback (most recent call last):
  File "<pyshell#44>", line 1, in <module>
    int(a)
ValueError: invalid literal for int() with base 10: 'rishi'
>>> float(a)
Traceback (most recent call last):
  File "<pyshell#45>", line 1, in <module>
    float(a)
ValueError: could not convert string to float: 'rishi'
>>> complex(a)
Traceback (most recent call last):
  File "<pyshell#46>", line 1, in <module>
    complex(a)
ValueError: complex() arg is a malformed string
>>> set(a)
{'s', 'r', 'h', 'i'}
>>> tuple(a)
('r', 'i', 's', 'h', 'i')
>>> list(a)
['r', 'i', 's', 'h', 'i']
>>> bool(a)
True
>>> a=[1,2,3,4]
>>> int(a)
Traceback (most recent call last):
  File "<pyshell#52>", line 1, in <module>
    int(a)
TypeError: int() argument must be a string, a bytes-like object or a real number, not 'list'
>>> float(a)
Traceback (most recent call last):
  File "<pyshell#53>", line 1, in <module>
    float(a)
TypeError: float() argument must be a string or a real number, not 'list'
>>> complex(a)
Traceback (most recent call last):
  File "<pyshell#54>", line 1, in <module>
    complex(a)
TypeError: complex() first argument must be a string or a number, not 'list'
>>> str(a)
'[1, 2, 3, 4]'
>>> tuple(a)
(1, 2, 3, 4)
