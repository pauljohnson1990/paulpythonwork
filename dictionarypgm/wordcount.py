#wordcount
text="hai hello hai hello"
#split method
word=text.split(" ")
print(len(word))
print(word)

word_count={}
# for i in range(0,len(word)):
#     print(len(word[i]))
#     word_count[word[i]]=len(word[i])
# print(word_count)

# for w in word:
#     if w in word_count:
#         word_count[w]+=1
#     else:
#         word_count[w]=1
# print(word_count)

for w in word:
    word_count[w]=word_count[w]+1 if w in word_count else 1
print(word_count)