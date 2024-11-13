def get_negative_numbers_descending():
    numbers = list(map(int, input().split()))
    negative_numbers = [num for num in numbers if num < 0]

    negative_numbers.sort(reverse=True)
    
    if negative_numbers:
        for num in negative_numbers:
            print(num, end=" ")
    else:
        print("列表中没有负整数", end="")

get_negative_numbers_descending()
