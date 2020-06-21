def validateBrackets(arrangement):
    specialChar = ['\'', '|']
    allChar = ['{', '[', '(', ')', '}', ']']
    merged = specialChar + allChar
    if len(arrangement) ==0:
        return True
    stack = []
    for i in arrangement:
        if i not in merged:
            continue
        if len(stack)>0:
            if i in specialChar:
                top = stack.pop()
                if top in allChar:
                    stack.append(top)
                    stack.append(i)
                    continue
                if i != top:
                    return False
                else:
                    continue
            if i in ['{', '[', '(']:
                stack.append(i)
            else:
                top = stack.pop()
                if top not in allChar:
                    stack.append(top)
                    continue
                if i == '}':
                    if top != '{':
                        return False
                elif i == ']':
                    if top!= '[':
                        return False
                elif i == ')':
                    if top!= '(':
                        return False
        else:
            stack.append(i)
    return True and len(stack)==0
                    
def doTest(x):
    print ("pattern = {pattern}, result = {result}").format(pattern = x, result = validateBrackets(x))
    
if __name__ == '__main__':
    doTest("{ [  ]  }")
    doTest("{ [ }")
    doTest("{ [ ] ( ) }")
    doTest("{ [ ( ] ) }")
    doTest("{ [ }")
    doTest("{ [a] (b) }")
    doTest("[")
    doTest("[]")
    doTest("code[]")
    doTest("''''");
    doTest("'''''");
    doTest("['']''");
    doTest("[']''");
