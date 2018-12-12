s="My name is Michele"
list_words=s.split()  #split() returns a list
list_words_reversed=list_words[::-1]  #this will give us a reversed list
s2=" ".join(list_words_reversed)
print(s2)