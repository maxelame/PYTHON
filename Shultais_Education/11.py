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
