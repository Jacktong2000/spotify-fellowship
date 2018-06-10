#Question 1
def question1(s,t):
    o = list(s)
    q = list(t)

    pureindex = []
    answer = ''

    for i in range(len(o)):
        if o[i] in q:
            pureindex.append(int(q.index(o[i])))

    pureindex = sorted(pureindex, key=int)

    for q in pureindex:
        answer += t[q]
    print(answer)

#question1('good', 'odg')


def question2(teststring):
    a = teststring
    count = ''
    repeat = []
    open = []
    body = ''
    answer = ''

    for i in range(len(a)):
        if a[i].isdigit():
            count += a[i]
        elif a[i] == '[':
            repeat.append(int(count))
            count = ''
        elif (a[i] != '[') and (a[i].isdigit() == False) and (a[i] != ']'):
            body += a[i]
            if (a[i+1].isdigit() == True):
                open.append(body)
                body = ''
        elif a[i] == ']' and (body != ''):
            open.append(body)
            body = ''

    while len(repeat) > 1:
        for i in range(repeat[-1]):
            answer += open[-1]
        repeat.pop()
        open.pop()

    answer = '{}{}'.format(open[0],answer)
    hold = answer
    for _ in range((repeat[0] - 1 )):
        answer += hold

    print(answer)


#question2('4[br3[a]]')


#question3
def question3(n, coins):
    if n < 0:
        return []
    if n == 0:
         return [[]]
    all_changes = []

    for last_used_coin in coins:
        combos = question3(n - last_used_coin, coins)
        for combo in combos:
            combo.append(last_used_coin)
            combo.sort()
            all_changes.append(combo)
    all_changes.sort()
    return all_changes

def at_last(r):
    potter = r
    result = set(tuple(row) for row in potter)
    showoff = [list(k) for k in result]
    print(sorted(showoff))
at_last(question3(4,[1,2,3]))
