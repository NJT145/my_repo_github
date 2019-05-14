.data
	no1: .word 6
	no2: .word 5
.text
	lw $s0, no1
	lw $s1, no2
	
	sub $t0, $s0, $s1  # t2 = t1 - t0
	
	li $v0, 1
	move $a0, $t0
	syscall
	
