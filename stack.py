


class Stack:
    def __init__(self, string):
        self.string = string
        self.stack = []

    def isEmpty(self):
        return bool(self.stack)

    def peek(self):
        if self.size() > 0:
            return self.stack[-1]
        return self.stack

    def pop(self, bracket):
        list_bracket_sum = ['()', '[]', '{}']
        for bracket_sum in list_bracket_sum:
            if self.size() == 0:
                return self.stack
            current_bracket_sum = self.peek() + bracket == bracket_sum
            if current_bracket_sum:
                del self.stack[-1]

            

    def push(self):
        def check_bracket_close(bracket):
            last_size = self.size()
            list_bracket_close = [')', ']', '}']
            if bracket in list_bracket_close and self.size() > 0:
                self.pop(bracket)
                next_size = self.size()
                result_size = last_size == next_size
                return result_size
            return True

        for bracket in self.string:
            if check_bracket_close(bracket):
                self.stack.append(bracket)
            
    def size(self):
        return len(self.stack)

string_bracket = '{{[()]}}'

balance = Stack(string_bracket)
balance.push()
result = balance.isEmpty()

if result:
    print('Небаланс')
else:
    print('Баланс')