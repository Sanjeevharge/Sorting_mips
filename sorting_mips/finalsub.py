import re

regis_numb = {
    "$s6": "10110",
    "$t2": "01010",
    "$t5": "01101",
    "$s4": "10100",                                         #defined dictionaries for registers
    "$a1": "00101",
    "$v1": "00011",
    "$v0": "00010",
    "$t4": "01100",
    "$t0": "01000",
    "$a3": "00111",
    "$t6": "01110",
    "$k1": "11011",
    "$t3": "01011",
    "$sp": "11101",
    "$s2": "10010",
    "$t9": "11001",
    "$s5": "10101",
    "$s3": "10011",
    "$0": "00000",
    "$s7": "10111",
    "$t8": "11000",   
    "$a0": "00100",
    "$ra": "11111",
    "$s1": "10001",
    "$at": "00001",
    "$t1": "01001",
    "$s0": "10000",   
    "loop3": "00000100000000000000010010",
    "$t7": "01111",
    "back": "100000000000000110101",
    "loop2": "0000000000000100",
    "exit": "0000000000010011",
    "swap": "00000100000000000000010010",
    "initial": "0000000000000110",
    "copy": "00000100000000000000000100",
    "swapbeq" : "0000000000000011"

}


J_ins = {'jal': '000011', 'j': '000010'}
I_ins = {'addi': '001000', 'lw': '100011', 'sw': '101011', 'beq': '000100','subi':'000000', 'bne':'000101'}
R_ins = {'sll': '000000', 'slt': '000000', 'sub': '000000', 'add': '000000'}





with open('bubble-sort.asm','r') as file_read:

    for line in file_read.readlines():
        if line.strip():          #for splitting of lines
        
            line = line.strip()   
        # leading tab and trailing newline are removed
        

        segments = re.split(r'[,\s()]+', line) 
                              # Splitting by commas,spaces and parentheses
        instruction = segments[0]
        if(segments[0]=="addi"):
            print(I_ins[segments[0]] + regis_numb[segments[2]] + regis_numb[segments[1]] + str(bin(int(segments[3]))[2:].zfill(16))) 
        if(segments[0]=="bne"):
            print(I_ins[segments[0]] + regis_numb[segments[1]] + regis_numb[segments[2]] + regis_numb[segments[3]])
        if(segments[0]=="beq"):
            if(segments[3]!="swap"):
                print(I_ins[segments[0]] + regis_numb[segments[1]] + regis_numb[segments[2]] + regis_numb[segments[3]])
            else :
                print(I_ins[segments[0]] + regis_numb[segments[1]] + regis_numb[segments[2]] + regis_numb[segments[3]+"beq"])
        if(segments[0]=="lw"):
            print(I_ins[segments[0]] + regis_numb[segments[3]] + regis_numb[segments[1]] + str(bin(int(segments[2]))[2:].zfill(16)))
        if(segments[0]=="sw"):
            print(I_ins[segments[0]] + regis_numb[segments[3]] + regis_numb[segments[1]] + str(bin(int(segments[2]))[2:].zfill(16)))
        if(segments[0]=="subi"):    
            print(I_ins[segments[0]] + regis_numb[segments[2]] + regis_numb[segments[1]] + str(bin(int(segments[3]))[2:].zfill(16)))
        if(segments[0]=="add"):
            print(R_ins[segments[0]] + regis_numb[segments[2]] + regis_numb[segments[3]] + regis_numb[segments[1]] + '00000' + '100010')
        if(segments[0]=="sub"):
            print(R_ins[segments[0]] + regis_numb[segments[2]] + regis_numb[segments[3]] + regis_numb[segments[1]] + '00000' + '100010')
        if(segments[0]=="j"):
            print(J_ins[segments[0]] + regis_numb[segments[1]])
        if(segments[0]=="slt"):
            print('000000' + '00000' + regis_numb[segments[2]] + regis_numb[segments[1]] + "00000" + '101010')
        if(segments[0]=="jal"):
            print(J_ins[segments[0]] + regis_numb[segments[1]])

	           


        


                 
