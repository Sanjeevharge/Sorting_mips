addi $s1,$t1,0#s1 is assigned n
addi $t5,$t2,0#t5 is assigned in input address
addi $t7,$t3,0#t7 is given the output address
addi $t0,$0,0#t0=i is assigned 0
copy:
	slt $t9,$t0,$s1#if0<n t9=1 else t9=0
	beq $t9,$0,initial#when t9=0 initial
	lw $t9,0($t5)#storing the 1st element into t9
	sw $t9,0($t7)#giving that element to 0th address of t7
	addi $t5,$t5,4#incrementing input address
	addi $t7,$t7,4#incrementing the output address
	addi $t0,$t0,1#i++
	j copy
	
initial:
	addi $at,$0,1#at=1
    	sub $s1,$s1,$at#n=n-1
	addi $t0,$0,0#i=0
	addi $t4,$0,0#t4=0=j
	addi $t7,$t3,0#t7=t3
	j loop3

loop3:
	slt $t9,$t0,$s1#if i<n-1 t9=1 else t9=0
	beq $t9,$0,exit#if t9=0 directly stop
	sub $t8,$s1,$t0#t8=n-1-i
	slt $t9,$t4,$t8#if j<n-i-1 the t9=1 else t9=0
	bne $t9,$0,loop2#if t9!=0 go to loop2
	addi $t4,$0,0#when the above conditon satisfy make jback to 0
	addi $t0,$t0,1#i++
	addi $t7,$t3,0
	j loop3
	
loop2:
	lw $t9,0($t7)#t9=A[j]
	lw $t5,4($t7)#t5=A[j+1]
	slt $s2,$t9,$t5#if A[j]<A[j+1] s2=1 else s2=0
	beq $s2,$0,swap #if s2=0 the do swap
	addi $t4,$t4,1#j++
	addi $t7,$t7,4#go to next output address
	j loop3
	
swap:
	sw $t5,0($t7)#t5 has A[j] and it is shifted to 1st address of the output address
	sw $t9,4($t7)#t9 has A[j+1] and that is shifted to 2nd address of the outpput address
	addi $t4,$t4,1#j++
	addi $t7,$t7,4#increment output address
	j loop3

exit:
