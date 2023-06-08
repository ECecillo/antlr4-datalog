from time import sleep
from itertools import groupby
from datalog_types import Predicate, Fact, AggregateFunction, Rule
from typing import List, Union, Dict


def match_and_bind(predicate: Predicate, EDB: List[Fact]):
    for fact in EDB:
        if fact.predicate == predicate.name and len(fact.values) == len(predicate.terms):
            yield {term: value for term, value in zip(predicate.terms, fact.values)}

def apply_aggregate(aggregate: AggregateFunction, variable_bindings: List[Dict[str, Union[str, int]]]) -> Union[str, int, float]:
    variable_to_aggr = aggregate.input_variable
    values_sum = 0
    values_count = 0

    for binding in variable_bindings:
        value = binding.get(variable_to_aggr)
        if value is not None:
            try:
                values_sum += int(value)
                values_count += 1
            except ValueError:
                return "Erreur: Tous les éléments de la liste doivent être des nombres"

    if values_count == 0:
        return None

    if aggregate.function == 'COUNT':
        return values_count
    elif aggregate.function == 'SUM':
        return values_sum
    elif aggregate.function == 'AVG':
        return values_sum / values_count

def construct_fact(head: Predicate, variable_bindings: Dict[str, Union[str, int]]) -> Fact:
    fact_values = [variable_bindings[var] for var in head.terms]
    return Fact(head.name, fact_values)

def datalog_engine_evaluation(datalog_program: List[Rule], EDB: List[Fact]) -> List[Fact]:
    derived_facts = []
    new_facts = True

    while new_facts:
        new_facts = False

        for rule in datalog_program:
            head, body = rule.head, rule.body
            # Initialize a list of all variable bindings for this rule
            all_variable_bindings = [{}]

            for predicate in body:
                if isinstance(predicate, Predicate):
                    # Get all matching bindings for this predicate
                    predicate_bindings = list(match_and_bind(predicate, EDB))
                    print(
                        f'All matching binding at begining for {predicate}: {all_variable_bindings} and predicate_binding return is : {predicate_bindings}')

                    if all_variable_bindings.count({}) == 1 and len(predicate_bindings) > 1:
                        print("Is empty because starting evaluation")
                        all_variable_bindings = predicate_bindings
                        continue
                    
                    index = {}
                    # Create a new list to hold the updated variable bindings
                    new_variable_bindings = []

                    # For each combination of existing and new bindings...
                    for existing_bindings in all_variable_bindings:
                        for new_bindings in predicate_bindings:
                            for variable, value in new_bindings.items():
                                if variable in existing_bindings and existing_bindings[variable] == value:
                                    new_binding = new_bindings.copy()
                                    print(
                                        f'Matching binding new variable {variable} with {new_binding} and old binding is {existing_bindings}')
                                    new_variable_bindings.append(new_binding)
                    
                    # Replace the list of all variable bindings with the updated list
                    all_variable_bindings = new_variable_bindings
                    print(
                        f'All matching binding at end of loop for {predicate}: {all_variable_bindings}')
                elif isinstance(predicate, AggregateFunction):
                    result = apply_aggregate(predicate, all_variable_bindings)
                    # Add the result to each individual binding
                    for binding in all_variable_bindings:
                        binding[predicate.output_variable] = result

            # Construct derived facts for each set of variable bindings
            for variable_bindings in all_variable_bindings:
                derived_fact = construct_fact(head, variable_bindings)

                if not any(fact.same_as(derived_fact) for fact in derived_facts):
                    derived_facts.append(derived_fact)

    return derived_facts
