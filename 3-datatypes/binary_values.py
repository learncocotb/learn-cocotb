# Simple tests for an counter module
from cocotb.binary import BinaryRepresentation, BinaryValue

bv = BinaryValue(10, 8, True, BinaryRepresentation.TWOS_COMPLEMENT)
print("===============================================================")
print("BinaryValue(10, 8, True, BinaryRepresentation.TWOS_COMPLEMENT)")
print("bv.get_value(): " + str(bv.get_value()))
print("bv.integer: " + str(bv.integer))
print("===============================================================")

print()

bv =  BinaryValue('XzZx0100', 8, True, BinaryRepresentation.TWOS_COMPLEMENT)
print("===============================================================")
print("BinaryValue('XzZx0100', 8, True, BinaryRepresentation.TWOS_COMPLEMENT)")
print("bv.is_resolvable: "+ str(bv.is_resolvable))
print("bv.binstr: "+ str(bv.binstr))
print("===============================================================")

print()


bv = BinaryValue('10000000', 8, True, BinaryRepresentation.TWOS_COMPLEMENT); 
print("===============================================================")
print("BinaryValue('10000000', 8, True, BinaryRepresentation.TWOS_COMPLEMENT)")
print("bv.get_value_signed(): " + str(bv.get_value_signed()))
print("bv.signed_integer: " + str(bv.signed_integer))
print("===============================================================")

print()

bv = BinaryValue(n_bits=10, bigEndian=False, binaryRepresentation=BinaryRepresentation.TWOS_COMPLEMENT)
bv.integer = -128
print("===============================================================")
print("bv = BinaryValue(n_bits=10, bigEndian=False, binaryRepresentation=BinaryRepresentation.TWOS_COMPLEMENT)")
print("bv.integer = -128")
print("bv.get_value_signed: " + str(bv.signed_integer))
print("bv.get_value_signed: " + str(bv.n_bits))
print("===============================================================")


