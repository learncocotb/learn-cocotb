from cocotb.types import Bit,Logic, LogicArray
from cocotb.types.range import Range

print('Logic("X"): ' + str(Logic("X")))

print("Logic('X'): " + str(Logic('X')))

print("Logic(True): " + str(Logic(True)))

print("Logic('1'): " + str(Logic('1')))

print("Logic(1): " + str(Logic(1)))

print("Logic(Bit(0)): " + str(Logic(Bit(0))))

print("Logic('0'): " + str(Logic('0')))

print("Logic(): " + str(Logic()))

print('Logic("01XZ").binstr: ' + LogicArray("01XZ").binstr)

print("LogicArray('01XZ', Range(3, 'downto', 0)): " + LogicArray('01XZ', Range(3, 'downto', 0)).binstr)

print('LogicArray([0, True, "X"]): ' + LogicArray([0, True, "X"]).binstr)

print("LogicArray('01X', Range(2, 'downto', 0))" + LogicArray('01X', Range(2, 'downto', 0)).binstr)

print("LogicArray(0xA).integer: " +    str(LogicArray(0xA).integer))         

print("LogicArray('1010', Range(3, 'downto', 0)): " + LogicArray('1010', Range(3, 'downto', 0)).binstr)

print('LogicArray(-4, Range(0, "to", 3)).signed_integer : ' + str(LogicArray(-4, Range(0, "to", 3)).signed_integer)) # will sign-extend

print("LogicArray('1100', Range(0, 'to', 3)): " + str(LogicArray('1100', Range(0, 'to', 3)).integer))

# note ordering
la = LogicArray('1100', Range(0, 'to', 3))
print("la[0]: " + str(la[0]))

# note ordering
la = LogicArray('1100', Range(3, 'downto', 0))
print("la[0]: " + str(la[0]))

# others to know

str(Logic("Z"))
bool(Logic(0))
int(Logic(1))
Bit(Logic("1"))
Bit('1')