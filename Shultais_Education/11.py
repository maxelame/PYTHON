languages = ['Chinese', 'Spanish', 'English', 'Hindi', 'Arabic', 'Bengali', 'Portuguese', 'Russian', 'Japanese', 'Lahnda']
print(languages[::-1])

#################
languages = ['Chinese', 'Spanish', 'English', 'Hindi', 'Arabic', 'Bengali', 'Portuguese', 'Russian', 'Japanese', 'Lahnda']

for i in range(0, len(languages) // 2):
    languages[i], languages[-(i + 1)] = languages[-(i + 1)], languages[i]

print(languages)


numbers1 = [1, 2, 3]
numbers2 = [6]
numbers3 = [7, 8, 9, 10, 11, 12, 13]

print(numbers1 * 2 + numbers2 * 9 + numbers3)



numbers = [2, 6, 3, 14, 10, 4, 11, 16, 12, 5, 4, 16, 1, 0, 8, 16, 10, 10, 8, 5, 1, 11, 10, 10, 12, 0, 0, 6, 14, 8, 2, 12, 14, 5, 6, 12, 1, 2, 10, 14, 9, 1, 15, 1, 2, 14, 16, 6, 7, 5]
print(len(numbers)) # Вывел длину списка;
print(numbers[-1]) #Вывел последний элемент списка;
print(numbers[::-1]) #Вывел список в обратном порядке (вспоминаем срезы);
if 15 in numbers and 17 in numbers:
    print("YES")
else:
    print("NO") #Вывел YES если список содержит числа 5 и 17, и NO в противном случае;
del numbers[0]
del numbers[-1]
print(numbers)#Вывел список с удаленным первым и последним элементами.
