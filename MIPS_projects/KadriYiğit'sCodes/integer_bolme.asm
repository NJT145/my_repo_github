.data


.text
	addi $t0, $zero, 30
	addi $t1, $zero, 4
		
	div $s0, $t0, $t1 # 30 / 5
	
	mflo $s0 #bolum
	mfhi $s1 #kalan
	
	li $v0, 1
	add $a0, $zero, $s0 
	
	
	syscall
	
