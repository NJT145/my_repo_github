.data
	karakterim: .byte "k"
.text
	li $v0, 4
	la $a0, karakterim
	syscall	
