def dailyTemp(temperatures):
    stack = []
    res = [0] * len(temperatures)

    for i, t in enumerate(temperatures):
        while stack and t > stack[-1][0]:
            stackT, stackInd = stack.pop()
            res[stackInd] = i - stackInd
        stack.append([t, i])

    return res