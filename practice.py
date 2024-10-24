from simpleai.search import SearchProblem,astar

GOAL="JOEL"

class problem(SearchProblem):
    def action(self,state):
        if len(state) < len(goal):
            return list('abcd')
        else:
            return []

    def action(self,state,action):
        return state+action

    def goal(self,state):
        return state==GOAL

    def heur(self,state):
        wrong=sum([1 if state[i]!= GOAL[i] else 0 for i in range(len(state))])
        missing = len(GOAL)-len(state)
        return wrong + missing

prob= problem(initial_state="")
result=astar(prob)
print(result.state)
print(result.path)
