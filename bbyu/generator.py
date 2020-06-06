from .data import korean
import random

animal = korean.animal
adjective = korean.adjective
color = korean.color

def generate(max_length, number_length=2, items=['adjective', 'animal', 'number'], seperator=''):
    if max_length < number_length or max_length < 5 or number_length < 0 or max_length - number_length < 2:
        raise ValueError
    count = 0
    while True:
        animal_rand = random.randint(0, len(animal)-1)
        adjective_rand = random.randint(0, len(adjective)-1)
        color_rand = random.randint(0, len(color)-1)
        item_value = []
        for item in items:
            seq = []
            if item == 'number':
                number = random.randint(pow(10, number_length-1), pow(10, number_length)-1)
                item_value.append(str(number))
            else:
                if item == 'adjective':
                    seq = adjective
                elif item == 'animal':
                    seq = animal
                elif item == 'color':
                    seq = color
                else:
                    item_value.append(str(item))
                    continue
                random_index = random.randint(0, len(seq)-1)
                item_value.append(seq[random_index])
        name = seperator.join(item_value)        
        if len(name) <= max_length:
            return name
        count = count + 1
        if count > 10000:
            raise ValueError('아이디를 생성하지 못하였습니다')

def easy_generate():
    return generate(max_length=15, number_length=0, items=['adjective', 'animal'])

if __name__ == "__main__":
    print(easy_generate())
