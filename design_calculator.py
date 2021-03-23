class Calculator(object):
    def calculate(self, expression):
            arr = []
            
            for char in expression:
                arr.append(char)
            return self.util(arr)

    def util(self, expression):    
        if len(expression) == 0 or expression[0] == " ":
            raise Exception("No expression provided")
        
        stack = []
        sign = '+'
        digit = 0
        
        while len(expression) > 0:        
            cur_char = expression.pop(0)   
            
            if cur_char.isdigit():
                digit = digit * 10 + int(cur_char)               
            
            if cur_char == '(':
                digit = self.util(expression)
            
            if len(expression) == 0 or (cur_char == '+' or cur_char == '-' or cur_char == '*' or cur_char == '/' or cur_char == ')'):
                if sign == '+':
                    stack.append(digit)
                elif sign == '-':
                    stack.append(-digit)
                elif sign == '*':
                    stack[-1] = stack[-1]*digit
                elif sign == '/':
                    stack[-1] = stack[-1]/float(digit)               
                sign = cur_char
                digit = 0
                if sign == ')':
                    break
        
        result = 0
        
        while len(stack):
            result = result + stack.pop()
        
        return result
