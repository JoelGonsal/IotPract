

def is_batsman(person):
    return person == "Sachin"

def is_cricketer(role):
    return role == "Batsman"

# Derive the conclusion
def derive_conclusion(person):
    if is_batsman(person) and is_cricketer("Batsman"):
        print(f"{person} is a Cricketer.")
    else:
        print(f"{person} is not a Cricketer.")

# Test with the given example
person = "Sachin"
derive_conclusion(person)

def bat(person1):
    return person1 == "Sachin"

def cri(role1):
    return role1 == "Batsmen"

def con(person1):
    if bat(person1) and cri("Batsmen"):
        print(f"{person1} is a Cricketer ")
    else:
        print(f"{person1} is not a Crickter")

person1 = "Sachin"
con(person1)
