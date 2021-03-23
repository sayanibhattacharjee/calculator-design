from flask import Flask
app = Flask(__name__)

class Calculator(object):
    def calculate(self, expression):

            arr = []
            for char in str(expression):
                arr.append(char)
            return self.util(arr)

    def util(self, expression):     
        if len(expression) == 0 or expression[0] == " ":
            raise Exception("No expression provided")
        stack = []
        sign = '+'
        num = 0
        while len(expression) > 0:
            cur_char = expression.pop(0)           
            if cur_char.isdigit():
                num = num * 10 + int(cur_char)               
            if cur_char == '(':
                num = self.util(expression)
            if (cur_char == '+' or cur_char == '-' or cur_char == '*' or cur_char == '/' or cur_char == ')'):
                if sign == '+':
                    stack.append(num)
                elif sign == '-':
                    stack.append(-num)
                elif sign == '*':
                    stack[-1] = stack[-1]*num
                elif sign == '/':
                    stack[-1] = stack[-1]/float(num)               
                sign = cur_char
                num = 0
                if sign == ')':
                    break
        result = 0
        while len(stack):
            result = result + stack.pop()
        return result

if __name__ == '__main__':
    app.run()

s = "5/2-3*2+5"
d = ""
cal = Calculator()
print(cal.calculate(s))