def count_character_frequency(input_string):
    uniqueChar={}

    for char in input_string:
        if char ==" ":
            continue
        count = input_string.count(char)
        if count > 0:
           #print(f" {char} is present {count} number of times" )
            uniqueChar[char]=count
            input_string=input_string.replace(char,'')

    return uniqueChar

x = count_character_frequency("hello world")
print(x)