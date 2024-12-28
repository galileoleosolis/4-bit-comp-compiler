code = list()


class register():

    def select(reg):
        if reg == "A":
            code.append("0000")
        elif reg == "B":
            code.append("0001")
        elif reg == "C":
            code.append("0010")
        elif reg == "D":
            code.append("0011")
        else:
            raise Exception("invalid register")

    def reg_to_buff():
        code.append("0100")

    def buff_to_reg():
        code.append("0101")

    def update():
        code.append("0110")

def write_alu(reg):
    if reg == "A":
        code.append("0111")
    elif reg == "B":
        code.append("1000")

def alu_math_op(op):
    if op == "+":
        code.append("1001")
    elif op == "-":
        code.append("1010")
        

def fetch_bin():
    
    return(code)