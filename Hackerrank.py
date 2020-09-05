from itertools import permutations


def getTotalX(a, b):
    # Write your code here
    list_of_nums = []
    init_num = max(a)
    max_num = min(b)
    while init_num <= max_num:
        a_has_factors = 0
        num_is_factor = 0
        for element in a:
            if init_num % element == 0:
                a_has_factors += 1
        for element in b:
            if element % init_num == 0:
                num_is_factor += 1
        if a_has_factors == len(a) and num_is_factor == len(b):
            list_of_nums.append(init_num)

        init_num += 1
    return len(list_of_nums)


a = [2, 4]
b = [16, 32, 96]
# print(getTotalX(a, b))


def birthday(s, d, m):
    # s -> array
    # d-> birthday date
    # m -> birthday month -> number of consecutive pieces she wants to give him

    pos = 0
    if d in s:
         pos += 1
    for i in range(len(s) - m):
        temp = 0
        for j in range(m):
            temp += s[j]
        if temp == s[i]:
            pos += 1
    return pos


# print(birthday([4], 4, 1))




def migratoryBirds(arr):
    count_dict ={}
    for num in arr:
        if num in count_dict.keys():
            count_dict[num] += 1
        else:
            count_dict[num] = 1
    max_bird = 0
    max_freq = 0
    for key in count_dict.keys():
        if count_dict[key] >= max_freq and key<max_bird:
            max_bird = key
            max_freq = count_dict[key]
        elif count_dict[key] > max_freq:
            max_bird = key
            max_freq= count_dict[key]
    return max_bird

print(migratoryBirds([1,2,3,4,5,4,3,2,1,3,4]))


def dayOfProgrammer(year):
        isleapyear = False
        if year < 1918:
            if (year % 4 == 0):
                isleapyear = True
            if isleapyear == False:
                return '13.09.' + str(year)
            else:
                return '12.09.' + str(year)
        elif year > 1918:
            if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
                isleapyear = True
            if isleapyear == False:
                return '13.09.' + str(year)
            else:
                return '12.09.' + str(year)
        else:
            return '12.09.1984'
print(dayOfProgrammer(1800))



#magic square cost reduction calculation
X = []
X.extend(list(map(int, '4 9 2'.split())))
X.extend(list(map(int, '3 5 7'.split())))
X.extend(list(map(int, '8 1 5'.split())))
print(X)
Ans = 81
for P in permutations(range(1, 10)):
    if sum(P[0:3]) == 15 and sum(P[3:6]) == 15 and sum(P[0::3]) == 15 and sum(P[1::3]) == 15 and P[0] + P[4] + P[8] == 15 and (P[2] + P[4] + P[6] == 15):
        print(P)
        Ans = min(Ans, sum(abs(P[i] - X[i]) for i in range(0, 9)))
print(Ans)


def reverseWords(s):
    # temp_lst = []
    # temp_str = ""
    # for letter in s:
    #     if s != '\s':
    #         temp_str += letter
    #         print(temp_str)
    #     elif s== " ":
    #         print(temp_lst)
    #         temp_lst.append(temp_str)
    #         temp_lst.append(" ")
    #         temp_str = ""
    # temp_lst = temp_lst[::-1]
    # new_str = "".join(temp_lst)
    # print(new_str.split())
    s = "".join(s)
    s = s.split(" ")
    s = s[::-1]
    s = " ".join(s)
    s = [letter for letter in s]
    print(s)


s= ["t","h","e"," ","s","k","y"," ","i","s"," ","b","l","u","e"]

reverseWords(s)