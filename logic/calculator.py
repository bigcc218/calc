class Calculator:
    def __init__(self):
        self.clear()
    def clear(self):
        self.expression = ''
    def evaluate(self, expr):
        self.expression = expr
        # 安全计算表达式
        try:
            # 只允许数字和运算符
            allowed = set('0123456789+-*/.() ')
            if not all(c in allowed for c in expr):
                raise ValueError('非法字符')
            result = str(eval(expr, {"__builtins__": None}, {}))
        except Exception:
            result = '错误'
        return result
