strng = "123+435-(34090)*346+(12-45*(56-6)))"


def brac(s):
    """this function returns inner most braketed index and value"""
    x = ""
    index_r = -1
    for i in s:
        index_r += 1
        if i == ")":
            break
    index_l = index_r
    while True:
        index_l -= 1
        x += s[index_l]
        if s[index_l - 1] != "(":
            continue
        else:
            break
    value = s[index_l:index_r]
    return index_l, value


def prev(s, index):
    """ this function returns the index and value of the of the previous number"""
    x = ""

    while True:
        index -= 1
        x += s[index]

        if s[index - 1] not in "*/+-" and index != 0:
            continue
        elif s[index - 1] in "+-":
            index -= 1
            x += s[index]
            break
        else:
            break
    # these reverses the string because to back it to original sequence
    value = x[::-1]

    return value, index


def nex(s, index):
    """this function returns the index and value of the next number"""
    x = ""
    while True:
        index += 1
        x += s[index]
        if index == len(s)-1:
            break
        elif s[index + 1] not in "+-*/":
            continue
        else:
            break

    return x, index


def replace(s, index_l, index_r, value):
    """this function will replace part of the string s with given left and right
    index and the value to be replaced with
    s = given string
    value = to be replaced with"""
    x = ""
    count = -1
    while count < len(s)-1:
        count += 1
        if count < index_l or count > index_r:
            x += s[count]

            # this ensures that value is inserted only once
        elif count == index_l + 1:
            x += value

    return x

def linear_cal(value):
    """It returns result of the simple arithmatic operation """

    i = 0
    # it simply puts a zero if the first numaric value of the given string is an operator
    if value[0] in '+-':
        value = '0' + value


    while True:
        if i == len(value)-1:
            i = 0
            break
        elif value[i] == '/':
            p = prev(value, i)
            n = nex(value, i)
            result = float(p[0])/float(n[0])
            if result >= 0:
                result = '+' + str(result)
            value = replace(value, p[1], n[1], str(result))
            # print(value)
            i = 0
            # continue
        i += 1
    while True:

        if i == len(value)-1:
            i = 0
            break
        elif value[i] == '*':
            p = prev(value, i)
            n = nex(value, i)
            result = float(p[0])*float(n[0])
            if result >= 0:
                result = '+' + str(result)
            value = replace(value, p[1], n[1], str(result))
            # print(value)
            i = 0
            # continue
        i += 1
    while True:

        if i == len(value) - 1:
            i = 0
            break
        elif value[i] == '+':
            p = prev(value, i)
            n = nex(value, i)
            result = float(p[0]) + float(n[0])
            if result >= 0:
                result = '+' + str(result)
            value = replace(value, p[1], n[1], str(result))
            i = 0
            # print(value)
            # continue
        i += 1
    while True:
        if i == len(value) - 1:
            i = 0
            break
        elif value[i] == '-':
            p = prev(value, i)
            n = nex(value, i)
            result = float(p[0]) - float(n[0])
            if result >= 0:
                result = '+' + str(result)
            value = replace(value, p[1], n[1], str(result))
            # print(value)
            i = 0
            # continue
        i += 1


    return value

# replace(8, 14, 'xxx')
# print(s)
print(linear_cal('-565-64/654+-4455-54-654*654+68+684'))
print(eval('-565-64/654+-4455-54-654*654+68+684'))
# print(prev('54*420/456*654', 10))

# print(prev("-65*4-89*54", 8))