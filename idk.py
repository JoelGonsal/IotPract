from simpleai.search import SearchProblem, astar

GOAL = 'JOEL'

class HelloProblem(SearchProblem):
    def actions(self, state):
        # Return possible characters to add if the current state length is less than the goal
        return list(' ABCDEFGHIJKLMNOPQRSTUVWXYZ') if len(state) < len(GOAL) else []

    def result(self, state, action):
        # Append the action character to the current state
        return state + action

    def is_goal(self, state):
        # Check if the current state matches the goal
        return state == GOAL

    def heuristic(self, state):
        
        wrong = sum(1 for i in range(min(len(state), len(GOAL)))
                    if state[i] != GOAL[i])
        return wrong + (len(GOAL) - len(state))

# Initialize and solve the problem
problem = HelloProblem(initial_state='')
result = astar(problem)

# Print the result state and the path taken to reach it
print("Resulting state:", result.state)
print("Path taken:")
for step in result.path():
    print(step)
print("Joel Gonsalves 112")


from simpleai.search import SearchProblem, astar

GOAL = 'HELLO WORLD'                  

class HelloProblem(SearchProblem):
    def actions(self, state):
        if len(state) < len(GOAL):
            return list('ABCDEFGHIJKLMNOPQRSTUVWXYZ ')
        else:
            return []

    def result(self, state, action):
        return state + action

    def is_goal(self, state):
        return state == GOAL

    def heuristic(self, state):
        # Calculate how far we are from the goal
        wrong = sum([1 if state[i] != GOAL[i] else 0 for i in range(len(state))])
        missing = len(GOAL) - len(state)
        return wrong + missing

problem = HelloProblem(initial_state='')
result = astar(problem)
print(result.state)
print(result.path())
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


