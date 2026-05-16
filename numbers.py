sum = 0
count_numbers3 = 0
count_odd_numbers = 0
numbers = [2, 3, 4, 8, 9, 10, 3, 2, 1, 3, 5, 6, 7, 9]
min = numbers[0]
new_arr = []
for number in numbers:
    print(number)
    sum += number
    if number == 3:
        count_numbers3 += 1
    if numbers[number] < numbers[0]:
        min == numbers[number]
    if number % 2 == 1:
        count_odd_numbers += 1
    if number not in new_arr:
        new_arr.append(number)
fist_index_number3 = 0
isFound = False
for i in range(len(numbers)):
     if numbers[i] == 3 and not isFound:
          fist_index_number3 = i
          isFound = True
          
          
print(new_arr)        
print("The total sum numbers in the list:",sum)
print("Count Numbers 3:",count_numbers3)
print("Minimum number is:",min)
print("Count Odd Numbers:",count_odd_numbers)

for number in new_arr:
            print(number)

print("First Index Number 3:",fist_index_number3)