def backwards(word):
    s=word.split()
    s.reverse()
    x=" ".join(s)
    return x

word="My name is Michele"
print(backwards(word))
