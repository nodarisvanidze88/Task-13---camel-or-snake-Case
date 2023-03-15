# camle to snake or snake to camel converter
user = input("Add the text: ").strip()

def snakeCheck(txt):
    counter = 0
    if "_" in txt:
        counter += 1
    return counter

def camelCheck(txt):
    text = list(txt)
    text[0]=text[0].lower()
    text = str("".join(text))
    counter1 = 0
    for i in text:
        if i.isupper():
            result = text.replace(i,"_"+i.lower())
            counter1 += 1


    return [result, counter1]

def snakeToCamleCase(txt):
    if snakeCheck(txt) > 0:
        text = txt.split("_")
        for i in range(1,len(text)):
            text[i] = text[i].title()
        text[0] = text[0].lower()
        result = "".join(text)
        return "Your input is snake_case\ncamelCase: "+ result
    elif camelCheck(txt)[1]>0:
        return "Your input is camelCase\nsnakeCase: "+ camelCheck(txt)[0]



def main():
    print(snakeToCamleCase(user))

main()

