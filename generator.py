from data import korean
import random

animal = korean.animal
adjective = korean.adjective

def generate(max_length, number_length, seperator=None):
    if max_length < number_length or max_length < 5 or number_length < 0 or max_length - number_length < 2:
        raise ValueError
    count = 0
    while True:
        animal_rand = random.randint(0, len(animal)-1)
        adjective_rand = random.randint(0, len(adjective)-1)
        if number_length == 0:
            number = ''
        else:
            number = random.randint(pow(10, number_length-1), pow(10, number_length)-1)
        
        if seperator:
            name = seperator.join((adjective[adjective_rand], animal[animal_rand], str(number)))
        else:
            name = f"{adjective[adjective_rand]}{animal[animal_rand]}{number}"
        
        if len(name) <= max_length:
            return name

        count = count + 1
        if count > 10000:
            raise ValueError('아이디를 생성하지 못하였습니다')

def easy_generate():
    return generate(max_length=15, number_length=0)

if __name__ == "__main__":
    print(easy_generate())
