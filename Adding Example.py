import comp as c
import op
#we are assuming that the 2 values we want to add are in registers c, and d

op.alu.set_from_reg("C", "D")
c.register.select("A") #this gets ready to store added value to register A
c.alu_math_op("+")



print(c.code) #prints the output of the binary compilation of instructions 
