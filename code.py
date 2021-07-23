import random

triads = [str(x) + str(y) + str(z) for x in range(0, 2) for y in range(0, 2) for z in range(0, 2)]
target = 100
pattern = {}
original_data = new_data = ''
prediction = random.choice(triads)
balance = 1000


def gather_pattern():
    global original_data, balance
    print('Please give AI some data to learn...')
    while len(original_data) <= target:
        print(f'The current data length is {len(original_data)}, {target - len(original_data)} symbols left')
        string = input('Print a random string containing 0 or 1: \n\n')
        for symbol in string:
            if symbol == '0' or symbol == '1':
                original_data += symbol
        if len(original_data) >= target:
            break
    print(f'\nFinal data string:\n{original_data}\n')
    print(f'You have ${balance}. Every time the system successfully predicts your next press, you lose $1.')
    print('Otherwise, you earn $1. Print "enough" to leave the game. Let\'s go!')


def analyze_pattern():
    for triad in triads:
        triad_0 = count(triad + '0')
        triad_1 = count(triad + '1')
        pattern.update({triad: [triad_0, triad_1]})
    return pattern


def count(tetrad):
    result, index = 0, 0
    for index in range(len(original_data) - 3):
        if tetrad in original_data[index: index + 4]:
            result += 1
        index += 1
    return result


def play():
    global new_data
    new_data = input('\nPrint a random string containing 0 or 1: \n')
    if new_data == 'enough':
        print('Game Over!')
        quit()
    elif not new_data.isdigit():
        play()
    else:
        pass



def predict_pattern():
    global new_data, prediction
    print('prediction')
    index = 0
    while len(prediction) != len(new_data):
        triad = new_data[index:index + 3]
        next_digit = str(pattern[triad].index(max(pattern[triad])))
        prediction += next_digit
        index += 1
    print(prediction)
    print()


def display_results():
    global balance
    correct = len([1 for a, b in zip(new_data[3:], prediction[3:]) if a == b])
    wrong = len([1 for a, b in zip(new_data[3:], prediction[3:]) if a != b])
    predicted = len(new_data[3:])
    percentage = correct / predicted * 100
    balance = balance - correct + wrong
    print(f'Computer guessed right {correct} out of {predicted} symbols ({percentage:.2f} %)')
    print(f'Your capital is now ${balance}')


if __name__ == '__main__':
    gather_pattern()
    while True:
        play()
        analyze_pattern()
        predict_pattern()
        display_results()
