sourcestring = "There are 7 days in a week - Sunday, Monday, Tuesday, Wednesday, Thursday, Friday and Saturday"
wordtofindone = "week"
wordToFindTwo = "day"
wordToFindThree = "weekend"

if wordtofindone in sourcestring:
    print(f"'{wordtofindone}' is present in the text.")
else:
    print(f"'{wordtofindone}' is NOT present in the text.")

def countOne(sourcestring,wordtofindone):
    for wordtofindone in sourcestring:
        count= sourcestring.lower().count(wordtofindone.lower())
        if count > 0:
            print(f'The word "{wordtofindone}" appears {count} time(s) in the string.')
        else:
            print(f'The word "{wordtofindone}" was not found in the string.')