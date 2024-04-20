import re
from abc import ABC, abstractmethod


class Node(ABC):
    
    @abstractmethod
    def __call__(self, values: dict) -> bool:
        pass


class Not(Node):
    
    def __init__(self, children) -> None:
        assert(len(children) == 1)
        self.child = children[0]

    def __call__(self, values: dict) -> bool:
        return not self.child(values)


class And(Node):

    def __init__(self, children) -> None:
        self.children = children

    def __call__(self, values: dict) -> bool:
        for child in self.children:
            if not child(values):
                return False
        return True


class Or(Node):

    def __init__(self, children) -> None:
        self.children = children

    def __call__(self, values: dict) -> bool:
        for child in self.children:
            if child(values):
                return True
        return False


class Implies(Node):
    
    def __init__(self, children) -> None:
        assert(len(children) == 2)
        self.p = children[0]
        self.q = children[1]

    def __call__(self, values: dict) -> bool:
        return not self.p(values) or self.q(values)


class Equals(Node):

    def __init__(self, children) -> None:
        assert(len(children) == 2)
        self.p = children[0]
        self.q = children[1]

    def __call__(self, values: dict) -> bool:
        return self.p(values) == self.q(values)


class Literal(Node):

    def __init__(self, args) -> None:
        assert(len(args) == 1)
        self.literal = args[0]

    def __call__(self, values: dict) -> bool:
        if self.literal == 'true':
            return True
        if self.literal == 'false':
            return False
        return bool(values[self.literal])


def validate_parentheses(expression):
    level = 0
    for c in expression:
        if c == '(': level += 1
        if c == ')': level -= 1
        if level < 0: return False
    return level == 0


def split_args(args_str: str) -> list[str]:
    start = 0
    level = 0
    args = []
    for i, c in enumerate(args_str):
        if c == ',' and level == 0:
            args.append(args_str[start:i])
            start = i + 1
        if c == '(': level += 1
        if c == ')': level -= 1
    args.append(args_str[start:])
    return args


def parse_expression(expression: str) -> Node:
    assert(validate_parentheses(expression))
    
    expression = expression.lower().replace(' ', '')
    tmp = re.sub(r'^.*?\(', '', expression)
    args_str = re.sub(r'\)$', '', tmp)
    args = split_args(args_str)

    children = None
    if '(' in expression:
        # TODO find a better way to determine if it's not a literal
        # not a literal
        children = [parse_expression(a) for a in args]

    if expression.startswith('not'):
        return Not(children)
    elif expression.startswith('and'):
        return And(children)
    elif expression.startswith('or'):
        return Or(children)
    elif expression.startswith('imp'):
        return Implies(children)
    elif expression.startswith('eq'):
        return Equals(children)
    else:
        # literal node
        return Literal(args)



def main():
    pass


if __name__ == '__main__':
    main()