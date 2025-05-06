numbers = []

def input_num():
    total = int(input("How many numbers you wish to entered:\n Total Numbers:"))
    for i in range(total):
        num=int(input("Enter the number:"))
        numbers.append(num)
    print("Numbers that you have entered:",numbers)

def selection():
    for i in range(len(numbers)):
        min_index = i
        for j in range(i+1,len(numbers)):
            if numbers[j] < numbers[min_index]:
                min_index = j
            numbers[i] , numbers[min_index] = numbers[min_index] , numbers[i]
            
    print("Sorted numbers using selection sort:",numbers)

def option():
    while True:
        print("Choose the option\n1.Add numbers\n2.Selection Sort\n3.Exit")
        optn = input("select the option:")
        if optn == '1':
            input_num()
        elif optn == '2':
            selection()
        elif optn == '3':
            break
        else:
            print("Enter the valid option")
option()