import sys
def input(): return sys.stdin.readline().rstrip()
stack_ = []
for _ in range(int(input())):
    command = input()
    if 'push' in command:
        command, number = command.split()
        stack_.append(number)
    elif command == 'pop' and len(stack_):
        print(stack_.pop())
    elif command == 'pop':
        print(-1)
    elif command == 'size':
        print(len(stack_))
    elif command == 'empty':
        if len(stack_):
            print(0)
        else:
            print(1)
    elif command == 'top':
        if len(stack_):
            print(stack_[-1])
        else:
            print(-1)