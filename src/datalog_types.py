from typing import *


class Variable():
    # Also called term
    name: str

    def __init__(self, name: str):
        self.name = name

    def __repr__(self):
        return self.name

# man("Enzo") is a fact.
# student(1123231, "Enzo", 20) is also fact.


class Fact:
    def __init__(self, predicate: str, values: List[Union[str, int]]):
        self.predicate = predicate
        self.values = values

    def __str__(self):
        return f'predicate name: {self.predicate}, values: {self.values}'

    def __repr__(self):
        term_str = ", ".join([str(t) for t in self.values])
        return f"{self.predicate}({term_str})"

    def same_as(self, other_fact):
        return self.predicate == other_fact.predicate and self.values == other_fact.values



class Predicate:
    name: str
    terms: List[str]

    def __init__(self, name: str, terms: List[str]):
        self.name = name
        self.terms = terms

    def __str__(self):
        return f'Relation name: {self.name}, terms: {self.terms}'

    def __repr__(self):
        term_str = ", ".join([str(t) for t in self.terms])
        return f"{self.name}({term_str})"

    pass

    def variables(self) -> Sequence[Variable]:
        return [v for v in self.terms if isinstance(v, Variable)]


class AggregateFunction:
    def __init__(self, function: str, variable_to_aggr: str, output_variable: str):
        self.function = function # COUNT, SUM, AVG
        self.input_variable = variable_to_aggr # [V]
        self.output_variable = output_variable # Count
    def __str__(self):
        return f'Aggregate function : {self.function}, inputVar: {self.input_variable}, output: {self.output_variable}'
    def __repr__(self):
        return f'{self.function}({self.input_variable}, {self.output_variable})'

class Rule:
    """
    A Datalog rule r is a logic program rule of the form:
    R0 <- R1, R2, ... Rn. where n >= 0
    Ri are relations where no function symbols appears
    R0 is called the head
    R1, R2.. Rn is called the body

    The meaning of the above rule is if R1,R2...Rn is true, then R0 is true.

    """

    head: Predicate
    body: List[Union[Predicate, 'AggregateFunction']]

    def __init__(self, head: Predicate, body: List[Union[Predicate, 'AggregateFunction']]):
        self.head = head
        self.body = body

    def __repr__(self):
        #body = ",".join([str(predicate.name) for predicate in self.body])
        res = []
        for predicate in self.body:
            if isinstance(predicate, AggregateFunction):
                res.append(predicate.function)
            else:
                res.append(predicate.name)
        body = ",".join(res) 
        return f"{self.head} <= {body}"
