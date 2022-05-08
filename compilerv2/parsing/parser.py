from typing import List
from scanning.error import error
from intermediate.tokens import *
from .expressions import *
from .statements import *


class Parser():
    def __init__(self, tokens: List[Token]):
        self.tokens = tokens
        self.current = 0

    # returns last - 1 token
    def previous(self) -> Token:
        return self.tokens[self.current - 1]

    # check if were at the end of the tokens
    def is_at_end(self) -> bool:
        return self.peek().type == tokens.EOF

    # returns current token
    def peek(self) -> Token:
        return self.tokens[self.current]

    # checks if current token is equal to given token
    def check(self, token: tokens) -> bool:
        if self.is_at_end():
            return False
        return self.peek().type == token

    # advances current token to next token
    def advance(self) -> None:
        self.current += 1

    def match(self, *tokens: tokens):
        for token in tokens:
            if self.check(token):
                self.advance()
                return True
        return False
    
    def consume(self, token: tokens, message: str) -> None:
        if self.check(token):
            self.advance()
        else:
            error(self.peek(), message)
    
    def primary(self) -> Expr:
        if self.match(tokens.FALSE):
            return LiteralExpr(False)
        if self.match(tokens.TRUE):
            return LiteralExpr(True)
        if self.match(tokens.NULL):
            return LiteralExpr(None)
        if self.match(tokens.NUMBER, tokens.STRING):
            return LiteralExpr(self.previous())
        if self.match(tokens.LEFT_PAREN):
            expr = self.expression()
            self.consume(tokens.RIGHT_PAREN, "Expected ')' after expression.")
            return GroupingExpr(expr)



    def unary(self) -> Expr:
        if self.match(tokens.MINUS, tokens.BANG):
            operator = self.previous()
            right = self.unary()
            return UnaryExpr(operator, right)
        return self.primary()

    def factor(self) -> Expr:
        expr = self.unary()

        while self.match(tokens.SLASH, tokens.STAR):
            operator = self.previous()
            right = self.unary()
            expr = BinaryExpr(expr, operator, right)
        
        return expr

    def term(self) -> Expr:
        expr = self.factor()
        
        while self.match(tokens.PLUS, tokens.MINUS):
            operator = self.previous()
            right = self.factor()
            expr = BinaryExpr(expr, operator, right)
        
        return expr

    def comparison(self) -> Expr:
        expr = self.term()

        while self.match(tokens.GREATER, tokens.GREATER_EQUAL, tokens.LESS, tokens.LESS_EQUAL):
            operator = self.previous()
            right = self.term()
            expr = BinaryExpr(expr, operator, right)
        
        return expr

    # parses equalities or anything above that
    def equality(self) -> Expr:
        expr = self.comparison()
        while self.match(tokens.EQUAL_EQUAL, tokens.BANG_EQUAL):
            operator = self.previous()
            right = self.expression()
            expr = BinaryExpr(expr, operator, right)
        return expr

    def expression(self) -> Expr:
        expr = self.equality()
        return expr

    def parse(self) -> Expr:
        expr = self.expression()
        return expr
