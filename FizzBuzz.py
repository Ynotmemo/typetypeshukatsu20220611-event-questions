for num in range(1, 101):
    string = ''

    #　15の倍数:''+'Fizz'+'Buzz'->'FizzBuzz'
    if num % 3 == 0:
        string += 'Fizz'

    if num % 5 == 0:
        string += 'Buzz'

    #　3の倍数でも5の倍数でもない時
    if len(string) == 0:
        string += str(num)

    print(string)
