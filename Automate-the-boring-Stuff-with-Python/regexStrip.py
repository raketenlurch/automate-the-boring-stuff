import re

def removeWhitespace(text):
    print(text)
    stripSpace = re.compile(r'\s')
    mo = stripSpace.sub(' ', text)
    print(mo)

def removeSecondArgument(text):
    print(text)
    stripSecondArgumentAndSpace = re.compile(r'((\w+)\s(\w+)?)')
    for groups in stripSecondArgumentAndSpace.findall(text):
        newText = groups[1]
    print(newText)

text = '"  hjjkhk  "'

if len(text.split()) > 1:
    removeSecondArgument(text)
else:
    removeWhitespace(text)