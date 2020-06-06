# bbyu-nickname-generator

Generate nickname with various options(animal, color etc.)

Currently supports only korean. but have plans to add all of the language in the world

### Objects

* adjective
* animal
* color

## Install
```shell
pip install bbyu-nickname-generator
```

## Usage
```python
>> from bbyu import generator
>> print(generator.easy_generate())
>> '수다스러운도마뱀'
>> print(generator.generate(max_length=12, number_length=3, seperator='-'))
>> '뒤늦은-물개-234'
>> print(generator.generate(max_length=10, number_length=2)) # default seperator = None
>> '외로운원숭이28'
>> generate(max_length=10, number_length=2, items=['number', '번째', 'color', 'animal'])
>> '72번째분홍색문어'
```

* Find out test.py for basic use case.

## Setting

### easy_generate()
```
generator.easy_generate()
```
* = ``generate(max_length=15, number_length=0))``

### generate()
```python
generator.generate(max_length=12, number_length=3, items=['color', 'animal', 'number'], seperator='-')
```
* ``max_length`` : The maximum length of nickname. It's easy to limit length of field.
* ``number_length`` : The length of number which locates end of the nickname.
* ``item`` : List of item type. item is the object which you can put in nickname. If you don't set any sequence, default is ``['adjective', 'number']``.
  
  * item list : ``'color', 'animal', 'number'``
  
  * else : except above item name, generator understand it's plain text. So they just put it to all nicknames. ex) '73``th``_red_mouse', '42``th``_green_horse'

* ``seperator`` : The seperator which shows up in between two item(adj, color, animal etc).


## Sources
* korean

  * adjective : https://ko.wiktionary.org/wiki/%EB%B6%84%EB%A5%98:%ED%95%9C%EA%B5%AD%EC%96%B4_%ED%98%95%EC%9A%A9%EC%82%AC
  * color : https://ko.wikipedia.org/wiki/%EC%83%89_%EB%AA%A9%EB%A1%9D
