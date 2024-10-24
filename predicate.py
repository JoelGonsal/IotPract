def derive_predicate(statements):
    # Create a dictionary to hold relationships
    relationships = {}
    
    # Process each statement
    for statement in statements:
        subject, predicate = statement.split(" is ")
        relationships[subject.strip()] = predicate.strip()
    
    # Derive the final predicate
    derived_statements = []
    for subject, predicate in relationships.items():
        # Check if the predicate can be a subject for another relationship
        if predicate in relationships:
            final_subject = subject
            final_predicate = relationships[predicate]
            derived_statements.append(f"{final_subject} is {final_predicate}")
    
    return derived_statements

# Example usage
statements = [
    "Sachin is batsman",
    "batsman is cricketer"
]

derived = derive_predicate(statements)

# Print results
for result in derived:
    print(result)
