def notas(*n, sit = False): 
    r = dict()
    r['total'] = len(n)
    r['maior'] = max(n)
    r['menor'] = min(n)
    r['media'] = sum(n)/ len(n)
    if sit:
        if r['media'] >= 5:
            r['situação'] = 'RAZOÁVEL'
        elif r['media']  >= 7:
            r['situação'] = 'BOA'
        else:
            r['situação'] = 'RUIM'
    return r


resp = notas(5.5, 5.6, 10, sit = True)
print(resp)
