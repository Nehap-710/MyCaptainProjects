def word_count(word):
    count={}
    for i in word:
        count[i] = word.count(i)
    return count
a = input('enter word:')
b = word_count(a)
c=list(b.keys())
c.sort()
for j in c:
    print(j, b[j])
