import earley_parser
import lex
import cpp_grammar

myParser = earley_parser.Parser(lex.CppLexAnalyzer(), cpp_grammar.set_cpp())


f = open('code_examples/main.cpp', 'r')
parsed = myParser.parse(f)
print(parsed)

f.close()
