class Node:
    def __init__(self, node_type, left=None, right=None, value=None):
        self.type = node_type
        self.left = left
        self.right = right
        self.value = value

    def __repr__(self):
        return f"Node(type={self.type}, value={self.value})"

    def evaluate(self, data):
        if self.type == "operand":
            attribute, operator, comparison_value = self.value
            actual_value = data.get(attribute)
            if actual_value is None:
                raise ValueError(f"Missing attribute: {attribute}")

            # Ensuring both values are of the same type for comparison
            if isinstance(actual_value, int):
                comparison_value = int(comparison_value)
            elif isinstance(actual_value, str):
                comparison_value = str(comparison_value)
            else:
                raise ValueError(f"Unsupported attribute type: {type(actual_value)}")

            if operator == ">":
                return actual_value > comparison_value
            elif operator == "<":
                return actual_value < comparison_value
            elif operator == "==":
                return actual_value == comparison_value
            elif operator == "!=":
                return actual_value != comparison_value
            elif operator == ">=":
                return actual_value >= comparison_value
            elif operator == "<=":
                return actual_value <= comparison_value
            else:
                raise ValueError(f"Unsupported operator: {operator}")

        elif self.type == "operator":
            if self.value == "AND":
                return self.left.evaluate(data) and self.right.evaluate(data)
            elif self.value == "OR":
                return self.left.evaluate(data) or self.right.evaluate(data)
            else:
                raise ValueError(f"Unsupported operator: {self.value}")

        else:
            raise ValueError(f"Unsupported node type: {self.type}")

def create_rule(rule_string):
    tokens = rule_string.replace('(', ' ( ').replace(')', ' ) ').split()
    # Validate tokens
    for token in tokens:
        if token not in {'(', ')', 'AND', 'OR', '>', '<', '==', '!=', '>=', '<='} and not token.isalnum() and not token.isdigit() and not token.startswith("'"):
            raise ValueError(f"Invalid token: {token}")
    print(f"Tokens: {tokens}")  # Debug statement
    return parse_tokens(tokens)

def parse_tokens(tokens):
    stack = []
    current_token = []
    for token in tokens:
        if token in {'AND', 'OR'}:
            if current_token:
                stack.append(tuple(current_token))
                current_token = []
            stack.append(token)
        elif token == '(':
            stack.append(token)
        elif token == ')':
            if current_token:
                stack.append(tuple(current_token))
                current_token = []
            sub_expr = []
            while stack and stack[-1] != '(':
                sub_expr.append(stack.pop())
            if not stack:
                raise ValueError("Mismatched parentheses in the expression")
            stack.pop()
            sub_expr.reverse()
            stack.append(sub_expr)
        else:
            current_token.append(token)
    if current_token:
        stack.append(tuple(current_token))
    if '(' in stack or ')' in stack:
        raise ValueError("Mismatched parentheses in the final stack")
    print(f"Final stack: {stack}")  # Debug statement
    return build_ast(stack)

def find_operator_index(tokens):
    precedence = {'AND': 1, 'OR': 0}
    max_precedence = -1
    operator_index = -1
    for index, token in enumerate(tokens):
        if token in precedence:
            if precedence[token] > max_precedence:
                max_precedence = precedence[token]
                operator_index = index
    return operator_index

def build_ast(expr):
    print(f"Building AST for: {expr}")  # Debug statement
    if isinstance(expr, list) and len(expr) == 1:
        expr = expr[0]
    
    if isinstance(expr, list) and len(expr) > 1:
        operator_index = find_operator_index(expr)
        if operator_index == -1:
            raise ValueError("No operator found in the expression")
        left_expr = build_ast(expr[:operator_index])
        right_expr = build_ast(expr[operator_index + 1:])
        return Node("operator", left=left_expr, right=right_expr, value=expr[operator_index])
    
    elif isinstance(expr, list) and len(expr) == 1:
        return build_ast(expr[0])
    
    elif isinstance(expr, tuple) and len(expr) == 3:
        attribute, operator, value = expr
        if isinstance(value, str):
            value = value.strip("'\"")
        return Node("operand", value=(attribute, operator, value))
    
    raise ValueError("Invalid expression")

def combine_rules(rules):
    root = None
    for rule_string in rules:
        rule_ast = create_rule(rule_string)
        if root is None:
            root = rule_ast
        else:
            root = Node("operator", value="AND", left=root, right=rule_ast)
    return root

def evaluate_rule(ast, data):
    return ast.evaluate(data)
