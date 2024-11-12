import math

HEXADECIMAL_NUMS = {
    "A": 10,
    "B": 11,
    "C": 12,
    "D": 13,
    "E": 14,
    "F": 15,
    10: "A",
    11: "B",
    12: "C",
    13: "D",
    14: "E",
    15: "F"
}

def converter_3000():
    number = input("Enter your number (\"number\"x\"base\"): ")
    for let in number.split("x")[0]:
        temp_num = int(let) if (let.isdecimal() and int(let) < 10) else HEXADECIMAL_NUMS[let.upper()]
        if temp_num >= int(number.split("x")[1]):
            print("Wrong input")
            return False
    base = input("Enter translate base (1 - 16): ")
    if not base.isdecimal() or int(base) not in range(1, 17):
        print("Wrong input")
        return False
    if int(base) != 1:
        print(convert_to_dif_base(convert_to_dec(number), int(base)), end="\n\n")
    else:
        print("|"*convert_to_dec(number))

def convert_to_dec(string_num: str):
    inp, inp_base = string_num.split("x")
    inp = reversed(inp)
    result_num = 0
    count = 0
    for i in inp:
        temp = i if i.isdecimal() else HEXADECIMAL_NUMS[i.upper()]
        result_num += int(temp) * int(math.pow(int(inp_base), count))
        count += 1
    return result_num

def convert_to_dif_base(dec_num: int, inp_base: int):
    result_num = ""
    while dec_num:
        i = dec_num % inp_base
        temp_num = i if i < 10 else HEXADECIMAL_NUMS[i]
        result_num = str(temp_num) + result_num
        dec_num = dec_num // inp_base
    return result_num + f"x{inp_base}"

while True:
    converter_3000()
    if input("Do you want to try again?: ").lower() != "yes":
        break