n = int(input())
books = {}
for i in range(n):
    book = input()
    books[book] = books.get(book, 0) + 1
max_ = 0
for i in books:
    if max_ < books[i]:
        max_ = books[i]
max_list = []
for i in books:
    if books[i] == max_:
        max_list.append(i)
print(sorted(max_list)[0])