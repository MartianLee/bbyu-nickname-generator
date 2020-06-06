from bbyu.generator import generate, easy_generate

# Usage
print('- easy_generate')
print(easy_generate())
print('\n- generate(max_length=10, number_length=2, items=[\'color\', \'animal\']) * 3')
for i in range(3):
  print(generate(max_length=10, number_length=2, items=['number', '번째', 'color', 'animal']))

print('\n- generate(max_length=10, number_length=2, items=[\'adjective\', \'color\', \'animal\', \'number\']) * 3')
for i in range(3):
  print(generate(max_length=10, number_length=2, items=['adjective', 'color', 'animal', 'number']))

print('\ngenerate(max_length=12, number_length=3, seperator=\'-\'')
print(generate(max_length=12, number_length=3, seperator='-'))
# print(generate(max_length=10, number_length=2))
