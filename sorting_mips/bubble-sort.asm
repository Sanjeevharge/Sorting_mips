addi $s1,$t1,0
addi $t5,$t2,0
addi $t7,$t3,0
addi $t0,$0,0
copy:
	slt $t9,$t0,$s1
	beq $t9,$0,initial
	lw $t9,0($t5)
	sw $t9,0($t7)
	addi $t5,$t5,4
	addi $t7,$t7,4
	addi $t0,$t0,1
	j copy
	
initial:
	addi $at,$0,1
    	sub $s1,$s1,$at
	addi $t0,$0,0
	addi $t4,$0,0
	addi $t7,$t3,0
	j loop3

loop3:
	slt $t9,$t0,$s1
	beq $t9,$0,exit
	sub $t8,$s1,$t0
	slt $t9,$t4,$t8
	bne $t9,$0,loop2
	addi $t4,$0,0
	addi $t0,$t0,1
	addi $t7,$t3,0
	j loop3
	
loop2:
	lw $t9,0($t7)
	lw $t5,4($t7)
	slt $s2,$t9,$t5
	beq $s2,$0,swap
	addi $t4,$t4,1
	addi $t7,$t7,4
	j loop3
	
swap:
	sw $t5,0($t7)
	sw $t9,4($t7)
	addi $t4,$t4,1
	addi $t7,$t7,4
	j loop3

exit: