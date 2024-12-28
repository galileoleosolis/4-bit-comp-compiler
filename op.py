import comp as c

def mov(x, y):
    c.register.select(x)
    c.register.reg_to_buff()
    c.register.select(y)
    c.register.buff_to_reg()

mov("A", "B")

print(c.code)