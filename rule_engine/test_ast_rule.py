import unittest
from rule_engine import create_rule, evaluate_rule, combine_rules, Node

class TestASTRuleEngine(unittest.TestCase):

    def test_create_rule(self):
        rule_string = "(age > 30 AND department == 'Sales')"
        ast = create_rule(rule_string)
        self.assertIsInstance(ast, Node)
        self.assertEqual(ast.type, "operator")

    def test_evaluate_rule(self):
        rule_string = "(age > 30 AND department == 'Sales')"
        ast = create_rule(rule_string)
        data = {"age": 35, "department": "Sales"}
        result = evaluate_rule(ast, data)
        self.assertTrue(result)

    def test_evaluate_rule_with_invalid_data(self):
        rule_string = "(age > 30 AND department == 'Sales')"
        ast = create_rule(rule_string)
        data = {"age": 25, "department": "Sales"}
        result = evaluate_rule(ast, data)
        self.assertFalse(result)

    def test_combine_rules(self):
        rule1 = "(age > 30 AND department == 'Sales')"
        rule2 = "(salary > 50000)"
        combined_ast = combine_rules([rule1, rule2])
        data = {"age": 35, "department": "Sales", "salary": 60000}
        result = evaluate_rule(combined_ast, data)
        self.assertTrue(result)

        data = {"age": 35, "department": "Sales", "salary": 40000}
        result = evaluate_rule(combined_ast, data)
        self.assertFalse(result)

    def test_invalid_rule(self):
        with self.assertRaises(ValueError):
            create_rule("(age >> 30 AND department == 'Sales')")

    def test_string_value_comparison(self):
        rule_string = "(department == 'Sales')"
        ast = create_rule(rule_string)
        data = {"department": "Sales"}
        result = evaluate_rule(ast, data)
        self.assertTrue(result)

        data = {"department": "Marketing"}
        result = evaluate_rule(ast, data)
        self.assertFalse(result)

if __name__ == "__main__":
    unittest.main()
