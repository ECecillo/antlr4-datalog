from time import sleep
from itertools import groupby
from datalog_types import Predicate, Fact, AggregateFunction, Rule
from typing import List, Union, Dict


def match_and_bind(predicate: Predicate, EDB: List[Fact]) -> List[Dict[str, Union[str, int]]]:
    # relation = next((r for r in EDB if r.predicate == predicate.name), None)
    relation = [r for r in EDB if r.predicate == predicate.name]
    all_bindings = []

    if relation:
        for fact in relation:
            variable_bindings = {}
            if len(fact.values) == len(predicate.terms):
                for term, value in zip(predicate.terms, fact.values):
                    variable_bindings[term] = value
                all_bindings.append(variable_bindings)
    return all_bindings


def apply_aggregate(
        aggregate: AggregateFunction,
        variable_bindings: List[Dict[str, Union[str, int]]]
    ) -> Union[str, int, float]:
    # Extract the variable to which the aggregate function applies
    variable_to_aggr = aggregate.input_variable

    # Extract the relevant values from the variable bindings
    values = [binding[variable_to_aggr]
              for binding in variable_bindings 
              if variable_to_aggr in binding and binding[variable_to_aggr] is not None]

    # If there are no values left, return NULL
    if not values:
        return None

    # Apply the aggregate function
    if aggregate.function == 'COUNT':
        return len(values)
    elif aggregate.function == 'SUM':
        try :
            sumResult = sum(int(element) for element in values)  
            return sumResult
        except ValueError:
            return "Erreur: Tous les éléments de la liste doivent être des nombres"
    elif aggregate.function == 'AVG':
        try:
            average = sum(int(element) for element in values)
            return average / len(values)
        except ValueError:
            return "Erreur: Tous les éléments de la liste doivent être des nombres"

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
                    predicate_bindings = match_and_bind(predicate, EDB)
                    print(
                        f'All matching binding at begining for {predicate}: {all_variable_bindings} and predicate_binding return is : {predicate_bindings}')
                    # sleep(5)
                    if all_variable_bindings.count({}) == 1 and len(predicate_bindings) > 1:
                        print("Is empty because starting evaluation")
                        all_variable_bindings = predicate_bindings
                        continue

                    # Create a new list to hold the updated variable bindings
                    # new_variable_bindings = []
                    new_var_binding_test = []

                    # For each combination of existing and new bindings...
                    for existing_bindings in all_variable_bindings:
                        for new_bindings in predicate_bindings:
                            for variable, value in new_bindings.items():
                                if variable in existing_bindings and existing_bindings[variable] == value:
                                    new_binding = new_bindings.copy()
                                    print(
                                        f'Matching binding new variable {variable} with {new_binding} and old binding is {existing_bindings}')
                                    new_var_binding_test.append(new_binding)
                            # # Merge the bindings together, making sure there are no conflicts
                            # merged_bindings = {
                            #     **existing_bindings, **new_bindings}
                            # print(
                            #     f'Merging {existing_bindings} and {new_bindings} to get {merged_bindings}')
                            # # Only add the merged bindings if they include all the bindings from both sets
                            # # This is a way of ensuring that the bindings are consistent (i.e., we don't have a binding of X to both 's1' and 's2')
                            # if all(value == merged_bindings.get(key) for key, value in {**existing_bindings, **new_bindings}.items()):
                            #     new_variable_bindings.append(
                            #         merged_bindings)

                    # Replace the list of all variable bindings with the updated list
                    # all_variable_bindings = new_variable_bindings
                    all_variable_bindings = new_var_binding_test
                    # print(
                    #     f'All matching binding at end of loop for {predicate}: {all_variable_bindings}')
                    print(
                        f'All matching binding at end of loop for {predicate}: {all_variable_bindings}')
                    # sleep(5)
                elif isinstance(predicate, AggregateFunction):
                    # Group bindings by the value of 'I'
                    #groups = groupby(all_variable_bindings, 'I')
                    # Apply the aggregate function to each set of bindings
                    # Apply the aggregate function to the set of variable bindings
                    result = apply_aggregate(predicate, all_variable_bindings)

                    # Add the result to each individual binding
                    for binding in all_variable_bindings:
                        binding[predicate.output_variable] = result
                    # For each group...
                    new_variable_bindings = []

                    #for group in groups:
                    #    # Apply the aggregate function to the group
                    #    result = apply_aggregate(predicate, group)

                    #    # Add the result to each binding in the group
                    #    for binding in group:
                    #        new_binding = binding.copy()
                    #        new_binding[predicate.output_variable] = result
                    #        new_variable_bindings.append(new_binding)

                    ## Replace the list of all variable bindings with the updated list
                    #all_variable_bindings = new_variable_bindings

            # Construct derived facts for each set of variable bindings
            for variable_bindings in all_variable_bindings:
                derived_fact = construct_fact(head, variable_bindings)

                if not any(fact.same_as(derived_fact) for fact in derived_facts):
                    derived_facts.append(derived_fact)
                    # new_facts = True

    return derived_facts
