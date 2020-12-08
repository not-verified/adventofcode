from parse import *
import copy

program = []

with open("input.txt", "r") as f:
    for line in f:
        op, sign, arg = parse("{} {}{:d}", line)
        program.append((op, int(arg) if sign == "+" else -int(arg)))

def execute(program, ip, acc, history):
    if ip in history:
        return None, acc, history
    if ip >= len(program):
        return -1, acc, history
    history.append(ip)
    op, delta = program[ip]
    if op == "nop":
        return ip + 1, acc, history
    if op == "acc":
        return ip + 1, acc + delta, history
    if op == "jmp":
        return ip + delta, acc, history

programs = [program]
for idx, instruction in enumerate(program):
    op, delta = instruction
    program_copy = copy.deepcopy(program)
    if op == "nop":
        program_copy[idx] = ("jmp", delta)
        programs.append(program_copy)
    if op == "jmp":
        program_copy[idx] = ("nop", delta)
        programs.append(program_copy)

for program in programs:
    ip, acc, history = 0, 0, []
    while ip != -1:
        ip, acc, history = execute(program, ip, acc, history)
        if ip == None:
            break
    print(acc) if ip == -1 else None