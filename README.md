# bbyu-nickname-generator
Generate nickname with various options(animal, color etc.)
Currently supports only korean. but have plans to add all of the language in the world
### Objects
  * adjective
  * animal
  <!-- * color -->

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
```

## Setting

### easy_generate()
```
generator.easy_generate()
```
* = ``generate(max_length=15, number_length=0))``

### generate()
```python
generator.generate(max_length=12, number_length=3, seperator='-')
```
* ``max_length`` : The maximum length of nickname. It's easy to limit length of field.
* ``number_length`` : The length of number which locates end of the nickname.
* ``seperator`` : The seperator which shows up in between two object(adj, color, animal etc).
