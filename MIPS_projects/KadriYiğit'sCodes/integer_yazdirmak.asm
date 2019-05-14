.data
	x: .word 12
	y: .word 1
	sum: .word 0
.text
	
	lw $t0, x
	lw $t1, y
	lw $s0, sum
	
	syscall	
