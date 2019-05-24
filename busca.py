f = open("pyflakes-make_test.docx")

text = ""

for s in f.readlines():
    x = s.find('PASSED')
    y = s.find('sudo')
    if x == -1 and y == -1:
        text += s

with open("pyflakes-IsLiteral.docx", "w") as temp:
    error_file = temp.write(text)
