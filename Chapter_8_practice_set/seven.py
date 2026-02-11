def func(lst,word):
    index = lst.index(word)
    raw_word = lst.pop(index)
    return raw_word.strip()

l = int(input("enter the length of list"))
print("start entering the list items \n")
lst=[]
for i in range(l):
    ele = input("enter word")
    lst.append(ele)

print('list completed')
print('enter the word to be removed and striped')
word = input()
print(f" word has been removed and striped : {func(lst,word)} ")
print(f"final list : {lst}")
