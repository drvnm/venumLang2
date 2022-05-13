from typing import List
from scanning.error import error
from intermediate.tokens import *
from .expressions import *
from .statements import *



class Parser():
    def __init__(self, tokens: List[Token]):
        self.tokens = tokens
        self.current = 0
    
    def previous(self) -> Token:
        return self.tokens[self.current - 1]    
        
    def is_at_end(self) -> bool:
        return self.peek().type == tokens.EOF
    
    def peek(self) -> Token:
        return self.tokens[self.current]
        
    def check(self, token: tokens) -> bool:
        if self.is_at_end():
            return False
        return self.peek().type == token

    def advance(self) -> None:
        self.current += 1
        return self.previous()
        
    def match(self, *types: tokens) -> bool:
        for type in types:
            if self.check(type):
                self.advance()
                return True
        return False

    def consume(self, token: tokens, message: str) -> None:
        if self.check(token):
           return self.advance()
        else:
            error(self.peek().line, message)
    
    def primary(self) -> Expr:
        if self.match(tokens.FALSE, tokens.TRUE):
            tok = self.previous()
            tok.literal = True if tok.lexeme == "true" else False
            return LiteralExpr(tok)
        if self.match(tokens.NULL):
            return LiteralExpr(None)
        if self.match(tokens.NUMBER, tokens.STRING):
            return LiteralExpr(self.previous())
        if self.match(tokens.IDENTIFIER):
            return VarExpr(self.previous())
        if self.match(tokens.LEFT_PAREN):
            expr = self.expression()
            self.consume(tokens.RIGHT_PAREN, "Expect ')' after expression.")
            return GroupingExpr(expr)
        raise Exception(f"Expect expression but got {self.peek()}")
    
    def unary(self) -> Expr:
        if self.match(tokens.MINUS, tokens.BANG):
            operator = self.previous()
            right = self.unary()
            return UnaryExpr(operator, right)
        return self.primary()
    
    def factor(self) -> Expr:
        expr = self.unary()
        
        while self.match(tokens.STAR, tokens.SLASH):
            operator = self.previous()
            right = self.unary()
            expr = BinaryExpr(expr, operator, right)
        return expr
    
    
    def term(self) -> Expr:
        expr = self.factor()

        while self.match(tokens.MINUS, tokens.PLUS):
            operator = self.previous()
            right = self.factor()
            expr = BinaryExpr(expr, operator, right)

        return expr

    def comparison(self) -> Expr:
        expr = self.term()

        while self.match(tokens.GREATER, tokens.LESS, tokens.GREATER_EQUAL, tokens.LESS_EQUAL):
            operator = self.previous()
            right = self.term()
            expr = BinaryExpr(expr, operator, right)

        return expr
        
    def equality(self) -> Expr:
        expr = self.comparison()

        while self.match(tokens.EQUAL_EQUAL, tokens.BANG):
            operator = self.previous()
            right = self.comparison()
            expr = BinaryExpr(expr, operator, right)

        return expr   
    
    def and_(self):
        expr = self.equality()
        
        while self.match(tokens.AND):
            operator = self.previous()
            right = self.equality()
            expr = LogicalExpr(expr, operator, right)
        
        return expr 
    
    def or_(self) -> Expr:
        expr = self.and_()
        
        while self.match(tokens.OR):
            operator = self.previous()
            right = self.and_()
            expr = LogicalExpr(expr, operator, right)

        return expr

    def assigment(self) -> Expr:
        expr = self.or_()

        if self.match(tokens.EQUAL):
           equals = self.previous()
           value = self.assigment()
           if isinstance(expr, VarExpr):
               name = expr.name
               return AssignExpr(name, value)
           
           error(equals.line, "Invalid assignment target.")
        return expr
    
    def expression(self) -> Expr:
        return self.assigment()
    
    def print_statement(self) -> Statement:
        expr = self.expression()
        self.consume(tokens.SEMICOLON, "Exptected ';' after expression.")
        return PrintStatement(expr)
    
    def expression_statement(self) -> Statement:
        expr = self.expression()
        self.consume(tokens.SEMICOLON, "Exptected ';' after expression.")
        return ExpressionStatement(expr)
    
    def block(self) -> List[Statement]:
        statements = []
        while not self.check(tokens.RIGHT_BRACE) and not self.is_at_end():
            statements.append(self.declaration())
        self.consume(tokens.RIGHT_BRACE, "Expected '}' after block.")
        return statements
    
    def if_statement(self) -> Statement:
        self.consume(tokens.LEFT_PAREN, "Expected '(' after 'if'.")
        condition = self.expression()
        self.consume(tokens.RIGHT_PAREN, "Expected ')' after expression")
        
        then_branch = self.statement()
        else_branch = None
        if self.match(tokens.ELSE):
            else_branch = self.statement()
        
        return IfStatement(condition, then_branch, else_branch)
    
    def statement(self) -> Statement:
        if self.match(tokens.PRINT):
            return self.print_statement()
        elif self.match(tokens.LEFT_BRACE):
            return BlockStatement(self.block())
        elif self.match(tokens.IF):
            return self.if_statement()
        return self.expression_statement()
    
    def let_declration(self) -> Statement:
        name = self.consume(tokens.IDENTIFIER, "Expected identifier after 'let'.")
        
        expr = None
        if self.match(tokens.EQUAL):
            expr = self.expression()
            
        self.consume(tokens.SEMICOLON, "Expected ';' after variable declaration.")
        return LetStatement(name, expr)

    def declaration(self) -> Statement:
        if self.match(tokens.LET):
            return self.let_declration()
        return self.statement()
    
    def parse(self) -> List[Statement]: 
        statements = []
        while not self.is_at_end():
            statements.append(self.declaration())
        
        return statements