import comp as c

def mov(x, y):
    c.register.select(x)
    c.register.reg_to_buff()
    c.register.select(y)
    c.register.buff_to_reg()

class alu():
    def set_from_reg(x, y):
        c.register.select(x)
        c.write_alu("A") #Sets x to alu A
        c.register.select(y)
        c.write_alu("B") #Sets y to alu B, this assums that we want to set the values sequentialy
print(c.code)