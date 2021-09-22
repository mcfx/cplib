import os, string, random

path = os.path.dirname(__file__)


def get_lara_code():
    s = open(os.path.join(path, 'comments.lara')).read()
    return [(s[:s.find('aspectdef main')], 'removeComments', 0, 1000)]


spaces = ' \t'
tokenchars = string.digits + string.ascii_letters + '_'
strp = '"\''

operators = {
    '::', '++', '--', '(', ')', '[', ']', '{', '}', '.', '->',
    '+', '-', '!', '~', '*', '&', '/', '%', '>>', '<<', '<', '>', '<=', '>=', '==', '!=', '^', '|',
    '&&', '||', '?', ':', '=', '+=', '-=', '*=', '/=', '%=', '<<=', '>>=', '&=', '^=', '|=', ',',
    ';',
}


def split_operators(s):
    i = 0
    res = []
    while i < len(s):
        j = i
        while j < len(s) and s[i:j + 1] in operators:
            j += 1
        res.append(s[i:j])
        i = j
    return res


def tokenize(code):
    lines = code.split('\n')
    sharps = []
    res = []
    for line in lines:
        if len(line) != 0 and line[0] == '#':
            sharps.append(line)
            continue
        pos = 0
        lst = ''
        lstp = True
        while pos < len(line):
            if line[pos] in spaces:
                if lst != '':
                    res.append(lst)
                    lst = ''
                pos += 1
                continue
            if line[pos] in strp:
                if lst != '':
                    res.append(lst)
                    lst = ''
                t = pos + 1
                while True:
                    if line[t] == '\\':
                        t += 2
                        continue
                    if line[t] == line[pos]:
                        break
                    t += 1
                res.append(line[pos:t + 1])
                pos = t + 1
                continue
            if pos + 1 < len(line) and line[pos] == '/' and line[pos + 1] == '/':
                break
            if (line[pos] in tokenchars) != lstp and lst != '':
                res.append(lst)
                lst = ''
            lstp = line[pos] in tokenchars
            lst += line[pos]
            pos += 1
        if lst != '':
            res.append(lst)
    res2 = []
    for token in res:
        if token[0] not in strp and token[0] not in tokenchars:
            res2 += split_operators(token)
        else:
            res2.append(token)
    return sharps, res2


def need_space(lst, x):
    if x[0] in strp:
        if lst[-1] in strp:
            return True
    elif x[0] in tokenchars:
        if lst[-1] in tokenchars:
            return True
    elif x[0] == '*':
        if lst[-1] == '/':
            return True


def gen_code(tokens):
    lst = ' '
    res = []
    for x in tokens:
        if need_space(lst, x):
            res.append(' ')
        res.append(x)
        lst = x
    return ''.join(res)


def macro_replace(sharps, tokens):
    token_names = {'y1', 'y2'}
    for token in tokens:
        if token[0] in tokenchars:
            token_names.add(token)

    def randname(curlen=1):
        curtm = 0
        while True:
            s = random.choice(string.ascii_letters)
            for _ in range(1, curlen):
                s += random.choice(string.ascii_letters + string.digits + '_')
            if s not in token_names:
                token_names.add(s)
                return s
            curtm += 1
            if curtm == 10:
                curtm = 0
                curlen += 1

    tn = []
    td = {}
    for t in tokens:
        if not t.startswith('_CPLTMP_'):
            tn.append(t)
            continue
        if t in td:
            tn.append(td[t])
            continue
        u = randname(2)
        td[t] = u
        tn.append(u)
        token_names.add(u)
        token_names.remove(t)
    tokens = tn

    while True:
        posd = {}
        for i, t in enumerate(tokens):
            if t not in posd:
                posd[t] = []
            posd[t].append(i)
        best = 0
        blen = 1000
        bcur = None
        for i, t in enumerate(tokens):
            cur = posd[t][:]
            lst = t
            totl = len(t)
            j = i
            while len(cur) > 1:
                reward = (len(cur) - 1) * (totl - 3) - 13  # len('#define xxx ')==12
                if reward > best:
                # if reward > 10 and (j - i + 1 <= blen or (j - i + 1 == blen and reward > best)):
                    best = reward
                    blen = j - i + 1
                    bcur = cur
                j += 1
                if j == len(tokens):
                    break
                if need_space(lst, tokens[j]):
                    totl += 1
                lst = tokens[j]
                totl += len(lst)
                curn = []
                for pos in cur:
                    if pos + j - i < len(tokens) and tokens[pos + j - i] == tokens[j]:
                        curn.append(pos)
                cur = curn
        if bcur is None:
            break
        print('macro_replace:', best, len(bcur), gen_code(tokens[bcur[0]:bcur[0] + blen]))
        name = randname()
        sharps.append('#define %s %s' % (name, gen_code(tokens[bcur[0]:bcur[0] + blen])))
        tn = []
        i = 0
        j = 0
        while i < len(tokens):
            if j < len(bcur) and bcur[j] == i:
                tn.append(name)
                i += blen
                j += 1
                continue
            tn.append(tokens[i])
            i += 1
        tokens = tn
    return sharps, tokens


def post_process_priority():
    return 1000


def post_process(code, _):
    sharps, tokens = tokenize(code)
    sharps, tokens = macro_replace(sharps, tokens)
    code = '\n'.join(sharps) + '\n' + gen_code(tokens) + '\n'
    return code


if __name__ == '__main__':
    code = open('../../../include/test_out.cpp').read().replace('\r', '\n')
    code = post_process(code, 0)
    code = open('../../../include/test_out2.cpp', 'w').write(code)
