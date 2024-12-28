import comp as c
import op


for i in range(1,10):
    op.mov("A", "B") 
    op.mov("B", "C")
    op.mov("C", "A")


print(c.code)