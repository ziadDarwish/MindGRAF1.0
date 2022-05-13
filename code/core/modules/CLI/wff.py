
from distutils.log import debug
import sys
from lark import Lark, tree



propositionalLogic = """

        start: query | predicate | prop |quantifierpredicate | quantifierpredicate CONNECTIVES start| "(" start ")" 
        | predicate CONNECTIVES start | commands | remove | addcommands | showcommands
    
        predicate: WORD "(" term ")" | "(" predicate ")"

        addcommands: addtocontext

        showcommands: showhyp | showcontexts

        commands:  definecontext | definenode | addattribute | query | definepath | definerelation | setcontext | setattitudes 

        remove: removecontext
    
        term: VAR | VAR "," term

        argument: WORD | WORD "," argument

        prop: priorityexpr | VAR | expr

        expr:  VAR CONNECTIVES prop

        priorityexpr:  "(" prop ")"

        quantifierpredicate: QUANTIFIER "(" VAR "," predicate ")"
        
        query: WORD "(" WORD ")" "?"  

        definecontext: "defineContext("  "[" term "]" ","  start ")"

        definenode: "defineNode(" WORD ","  "[" term "]" "," start ")" -> molecular | "defineNode(" WORD "," start ")" -> variable

        definepath: "definePath(" WORD "," start ")"

        definerelation: "defineRelation(" WORD "," WORD ")" | "defineRelation(" WORD "," WORD "," WORD "," WORD ")"

        addattribute: "addAttr(" WORD "," "[" argument "]" "," "[" argument "]" ")"

        setcontext: "setContext(" WORD "," "[" "[" start "]" "," "[" start "]" "," "[" start "]"  "]"  ")"
        
        removecontext: "removeContext(" WORD ")"

        addtocontext: "addToContext(" prop "," WORD ")"

        showhyp: "showHypothesis"

        showcontexts: "showContexts"

        setattitudes: "setAttitudes(" "[" start "," start  "]" ")"
        QUANTIFIER: "forAll"
        CONNECTIVES: "^" | "|" | "->" | "="
        VAR: "a".."z" 
        


        %import common.WS
        %import common.WORD

    """

parserLark = Lark(propositionalLogic, start='start', ambiguity='explicit')

class wff():

    def __init__(self,grammar=propositionalLogic,parser=parserLark):
       self.grammar = grammar
       self.parser = parser

    def getGrammar(self):
       return self.grammar

    def getParser(self):
       return self.parser

    
    def precedenceQueue():
        propositionStack = []
        operatorStack = []
        return propositionStack, operatorStack
    
 

    def prettyParse(self,ex,fileName):
        print(self.getParser().parse(ex).pretty())
        #print(tree.Tree.iter_subtrees_topdown)
        #tree.pydot__tree_to_png(parserLark.parse(ex), fileName)

    
    
if __name__ == '__main__':

    p = wff()
    # print(p.getProposition())
    # print(p.getGrammar())
    # print(p.getParser())
    #p.prettyParse("(p^q)=t",sys.argv[1])
    t = "p^q"
    p.prettyParse(t,"")
 
