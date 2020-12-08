from parse import *

program = []

with open("input.txt", "r") as f:
    for line in f:
        op, sign, arg = parse("{} {}{:d}", line)
        program.append((op, int(arg) if sign == "+" else -int(arg)))

def execute(program, ip, acc, history):
    if ip in history or ip >= len(program):
        return None, acc, history
    history.append(ip)
    op, delta = program[ip]
    if op == "nop":
        return ip + 1, acc, history
    if op == "acc":
        return ip + 1, acc + delta, history
    if op == "jmp":
        return ip + delta, acc, history
    
ip, acc, history = 0, 0, []
while ip != None:
    ip, acc, history = execute(program, ip, acc, history)

print(acc)