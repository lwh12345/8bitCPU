# 0-7bit 立即数
IMM1 = [i for i in range(256)]

# 8-10bit 寄存器地址或立即数
R0_2 = 0b000 << 8
R1_2 = 0b001 << 8
R2_2 = 0b010 << 8
R3_2 = 0b011 << 8
R4_2 = 0b100 << 8
R5_2 = 0b101 << 8
R6_2 = 0b110 << 8
R7_2 = 0b111 << 8

# 11-13bit 寄存器地址或立即数
R0_1 = 0b000 << 11
R1_1 = 0b001 << 11
R2_1 = 0b010 << 11
R3_1 = 0b011 << 11
R4_1 = 0b100 << 11
R5_1 = 0b101 << 11
R7_1 = 0b111 << 11
R6_1 = 0b110 << 11

# 14-16bit 目标寄存器地址
RD_0 = 0b000 << 14
RD_1 = 0b001 << 14
RD_2 = 0b010 << 14
RD_3 = 0b011 << 14
RD_4 = 0b100 << 14
RD_5 = 0b101 << 14
RD_6 = 0b110 << 14
RD_7 = 0b111 << 14

# 25-17bit op操作位
# 两个寄存器间运算
ADD_R = 0b00000000 << 17
SUB_R = 0b00000001 << 17
AND_R = 0b00000010 << 17
OR_R  = 0b00000011 << 17
XOR_R = 0b00000100 << 17
NOT_R = 0b00000101 << 17

# 立即数运算
ADD_I = 0b10000000 << 17
SUB_I = 0b10000001 << 17
AND_I = 0b10000010 << 17
OR_I  = 0b10000011 << 17
XOR_I = 0b10000100 << 17
NOT_I = 0b10000101 << 17

# 内存读写操作
LOAD  = 0b10010000 << 17 # 读出
STORE = 0b10100000 << 17 # 写入

# 条件跳转操作
BEQ_R = 0b00001000 << 17 # 等于
BNE_R = 0b00001001 << 17 # 不等于
BLT_R = 0b00001010 << 17 # 小于
BGE_R = 0b00001101 << 17 # 大于等于
JMP   = 0b00001000 << 17 # 无条件跳转

# 压栈出栈
PUSH  = STORE | R7_1 # 压栈
POP   = LOAD  | R7_1 # 出栈

# 空指令
NOP   = JMP   | 12

# 汇编指令 [操作 地址1或数据1 地址2或数据2 地址]
data = [
    ADD_I | RD_1 | 100,
    ADD_I | RD_2 | 120,
    ADD_R | RD_3 | R1_1 | R2_2,
    ADD_I | RD_7 | 255,
    
    PUSH  | R1_2,
    SUB_I | RD_7 | R7_1 | 1,
    PUSH  | R2_2,
    SUB_I | RD_7 | R7_1 | 1,

    ADD_I | RD_7 | R7_1 | 1,
    POP   | RD_4,
    ADD_I | RD_7 | R7_1 | 1,
    POP   | RD_5,
    NOP
]

# 写入二进制文件
with open('asm.bin', 'wb') as f:
    for num in data:
        # 将16位整数转为大端序的2字节
        f.write(num.to_bytes(4, byteorder="little", signed=False))