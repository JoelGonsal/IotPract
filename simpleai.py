from simpleai.search import CspProblem, backtrack, MOST_CONSTRAINED_VARIABLE, HIGHEST_DEGREE_VARIABLE, LEAST_CONSTRAINING_VALUE

variables = ('a','b','c','d')

domains = dict((v,['red','blue','green']) for v in variables)

def diff(variables,values):
    return values[0] != values[1]

constrants = {
    (('a','b'),diff),
    (('a','c'),diff),
    (('b','c'),diff),
    (('b','d'),diff)
    }

prob=CspProblem(variables,domains,constrants)

print(backtrack(prob))


print(backtrack(prob, variable_heuristic=MOST_CONSTRAINED_VARIABLE))


print(backtrack(prob, variable_heuristic=HIGHEST_DEGREE_VARIABLE))


print(backtrack(prob, value_heuristic=LEAST_CONSTRAINING_VALUE))




