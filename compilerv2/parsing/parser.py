from re import I
from typing import List
from scanning.error import error
from intermediate.tokens import *
from intermediate.lookup_tables import *
from .expressions import *
from .statements import *

types = [tokens.BYTE, tokens.SHORT, tokens.INT,
         tokens.LONG, tokens.BOOL, tokens.STRING]
inc_dec_tokens = [tokens.EQUAL, tokens.PLUS_EQUAL,
                  tokens.MINUS_EQUAL, tokens.STAR_EQUAL, tokens.SLASH_EQUAL]


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
        return self.previous()

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
        if self.match(tokens.IDENTIFIER):
            return VarExpr(self.previous())
        if self.match(tokens.STAR):
            expr = self.expression()
            return DereferenceExpr(expr)
        if self.match(tokens.AMPERSAND):
            token = self.consume(tokens.IDENTIFIER, "Expected variable name.")
            return VarToPointerExpr(token)

        # if no valid token is found, throw error
        error(self.peek(), "Expected expression.")

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

        while self.match(tokens.PLUS, tokens.MINUS, tokens.PERCENT):
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

    def assignment(self) -> Expr:
        expr = self.equality()

        if self.match(*inc_dec_tokens):
            operator = self.previous()
            right = self.assignment()
            if isinstance(expr, VarExpr):
                return AssignmentExpr(expr.name, operator, right)

            error(operator, "Invalid assignment target.")

        return expr

    def expression(self) -> Expr:
        expr = self.assignment()
        return expr

    def print_stmt(self) -> Stmt:
        expr = self.expression()
        self.consume(tokens.SEMICOLON,
                     "Expected ';' after 'print' expression.")
        return PrintStmt(expr)

    def expression_stmt(self) -> Stmt:
        expr = self.expression()
        self.consume(tokens.SEMICOLON, "Expected ';' after expression.")
        return ExprStmt(expr)

    def block(self) -> Stmt:
        statements = []
        while not self.check(tokens.RIGHT_BRACE) and not self.is_at_end():
            statements.append(self.declaration())
        self.consume(tokens.RIGHT_BRACE, "Expected '}' after block.")
        return BlockStmt(statements)

    def if_stmt(self) -> Stmt:
        self.consume(tokens.LEFT_PAREN, "Expected '(' after 'if'.")
        condition = self.expression()
        self.consume(tokens.RIGHT_PAREN, "Expected ')' after if condition.")
        then_branch = self.statement()

        elif_statements = []
        while self.match(tokens.ELIF):
            elif_index = self.current - 1
            self.consume(tokens.LEFT_PAREN, "Expected '(' after 'elseif'.")
            econdition = self.expression()
            self.consume(tokens.RIGHT_PAREN,
                         "Expected ')' after elseif condition.")
            ethen_branch = self.statement()
            # self.current is used to generate a unique label for each elif statement
            elif_statements.append((econdition, ethen_branch, elif_index))

        else_branch = None
        else_id = None
        if self.match(tokens.ELSE):
            else_id = self.current - 1
            else_branch = self.statement()

        stmt = IfStmt(condition, then_branch, elif_statements, else_branch)
        stmt.end_id = self.current
        if else_branch:
            stmt.else_id = else_id
        return stmt
    
    def while_stmt(self) -> Stmt:
        while_index = self.current - 1
        self.consume(tokens.LEFT_PAREN, "Expected '(' after 'while'.")
        condition = self.expression()
        self.consume(tokens.RIGHT_PAREN, "Expected ')' after while condition.")
        body = self.statement()
        end_index = self.current

        stmt = WhileStmt(condition, body, while_index, end_index)
        return stmt

    def statement(self) -> Stmt:
        if self.match(tokens.PRINT):
            return self.print_stmt()
        if self.match(tokens.LEFT_BRACE):
            return self.block()
        if self.match(tokens.IF):
            return self.if_stmt()
        if self.match(tokens.WHILE):
            return self.while_stmt()
        return self.expression_stmt()

    def var_declaration(self) -> Stmt:
        type_ = self.previous()
        size = type_to_size[type_.type]
        name = self.consume(tokens.IDENTIFIER, "Expected variable name.")
        expr = None

        if self.match(tokens.EQUAL):
            expr = self.expression()

        self.consume(tokens.SEMICOLON,
                     "Expected ';' after variable declaration.")
        return VarStmt(type_, name, expr, size)

    def declaration(self) -> Stmt:
        if self.match(*types):
            return self.var_declaration()
        return self.statement()

    def parse(self) -> List[Stmt]:
        statements = []

        while not self.is_at_end():
            statements.append(self.declaration())

        return statements
