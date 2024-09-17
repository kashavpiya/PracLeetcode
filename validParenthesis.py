def validParenthesis(S):
    #O(n)
    closeToOpen = { ")": "(", "}":"{", "]":"["}
    stack = []

    for n in S:
        if n in closeToOpen:
            if stack and stack[-1] == closeToOpen[n]:
                stack.pop()
            else:
                return False
        else:
            stack.append(n)

    return (not stack)

def main():
    print(validParenthesis("{}[}{}"))

if __name__ == "__main__":
    main()