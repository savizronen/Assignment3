"""
assignment 3 - Intro to Computation with Python
functions:
function parameters - positional, default, *args
scope - global, local
function evocation & subroutines
by Hadas Lapid
all rights reserved
"""
# Q1.a
chrs = []


def creat_let_list():
    for i in range(97, 123):
        chrs.append(chr(i))


# Q1.b
def mod_chrs(I, n=0):  # ADD INPUT
    for i in range(len(chrs)):
        if I == chrs[i]:
            if (ord(chrs[i]) + n) > 122:
                distance_to_z = 122 - ord(chrs[i])
                n = n - distance_to_z
                return chr(97 + n - 1)
            return chr(ord(chrs[i]) + n)


# Q1.c
def mod_word(s, n):  # ADD INPUT
    str = ""
    for ch in s:
        str += mod_chrs(ch, n)
    return str


# Q2
def filter_files(*args, ext='.csv'):  # ADD INPUT
    lst = []
    for file_name in args:
        if len(file_name) >= 4:
            file_name_ext = file_name[len(file_name) - 4:len(file_name)]
            if file_name_ext == ext:
                lst.append(file_name)
    return lst


# Q3.a
def break_digits(num):  # ADD INPUT
    lst_reverse = []
    while num != 0:
        number = num % 10
        lst_reverse.append(number)
        num = int(num / 10)
    return lst_reverse


# Q3.b
def list2num(lst):  # ADD INPUT
    num = 0
    if len(lst) != 0:
        for digit in lst[::-1]:
            num += int(digit)
            num = num * 10
    else:
        return []
    return num // 10


# Q3.c
def min_nums(x, y):  # ADD INPUT
    res_lst = []
    x_lst = break_digits(x)
    y_lst = break_digits(y)
    if len(x_lst) != len(y_lst):
        print("digits are not of the same size")
    counter_arry = [0] * 10
    for i in x_lst:
        counter_arry[i] += 1
    for i in y_lst:
        counter_arry[i] += 1
    counter_digit = len(x_lst)
    for i in range(len(counter_arry)):
        if counter_arry[i] > 0:
            res_lst.append(i)
            counter_digit -= 1
            counter_arry[i] -= 1
        if counter_digit == 0:
            res_lst = res_lst[::-1]
            return list2num(res_lst)

    return None


def main():
    # global chrs
    # Q1.a
    creat_let_list()
    print(chrs)
    # Q1.b
    print(f"'a' was shifted to '{mod_chrs('a', 5)}' with n=5")
    print(f"'z' was shifted to '{mod_chrs('z', 4)}' with n=4")
    # Q1.c
    word = "story"
    print(f"'{word}' is modified to '{mod_word(word, 2)}' with n=2")

    # Q2
    csv_files = filter_files("file.csv", "file2.txt", "file3.doc", "file4.csv")
    print(f"csv files: {csv_files}")
    doc_files = filter_files("file.csv", "file2.txt", "file3.doc", "file4.csv", ext='.doc')
    print(f"doc files: {doc_files}")
    txt_files = filter_files("file.csv", "file2.txt", "file3.doc", "file4.csv", ext='.txt')
    print(f"text files: {txt_files}")

    # Q3.a
    num = 1357
    print(f"{num} is broken into {break_digits(num)}")
    # Q3.b
    l = [1, 4, 5, 6]
    print(f"{l} is assembled into {list2num(l)}")
    # Q3.c
    n1 = 185
    n2 = 437
    print(f"from {n1} and {n2} you get the minimal valued digits: {min_nums(n1, n2)}")
    # unequal size test
    min_nums(1, 123)
    return


if __name__ == "__main__":
    main()
