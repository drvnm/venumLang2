from typing import List
from intermediate.tokens import *
from .expressions import *


class Parser:
    def __init__(self, tokens: List[Token]):
        self.tokens = tokens
        self.current = 0
    

    def peek(self) -> Token:
        return self.tokens[self.current]

    def previous(self) -> Token:
        return self.tokens[self.current - 1]

    def is_at_end(self) -> bool:
        return self.peek().type == tokens.EOF

    def check(self, type: tokens) -> bool:
        if self.is_at_end():
            return False

        return self.peek().type == type

    def advance(self) -> Token:
        self.current += 1
        return self.previous()

    def match(self, *types: tokens) -> bool:
        for type in types:
            if self.check(type):
                self.advance()
                return True

        return False

    def error(self, token: Token, message: str) -> Exception:
        if token.type == tokens.EOF:
            raise Exception("Unexpected end of file.")

        return Exception(f"{token.line} at {token.lexeme}: {message}")

    def consume(self, token: tokens, message: str = "") -> Token:
        if self.check(token):
            return self.advance()

        raise self.error(token, message)

    def primary(self) -> Expr:
        if self.match(tokens.FALSE):
            return LiteralExpr(False)
        if self.match(tokens.TRUE):
            return LiteralExpr(True)
        if self.match(tokens.NIL):
            return LiteralExpr(None)
        if self.match(tokens.NUMBER, tokens.STRING):
            return LiteralExpr(self.previous().literal)
        if self.match(tokens.LEFT_PAREN):
            expr = self.expression()
            self.consume(tokens.RIGHT_PAREN, "Expect ')' after expression.")
            return GroupingExpr(expr)

        raise Exception("Expect expression.")

    def unary(self) -> Expr:
        if self.match(tokens.BANG, tokens.MINUS):
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

    def equality(self) -> Expr:
        expr = self.comparison()

        while self.match(tokens.BANG_EQUAL, tokens.EQUAL_EQUAL):
            operator = self.previous()
            right = self.comparison()
            expr = BinaryExpr(expr, operator, right)

        return expr

    def expression(self) -> Expr:
        return self.equality()

    def parse(self) -> Expr:
        return self.expression()
        