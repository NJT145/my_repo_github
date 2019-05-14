.data
	float_integer: .float 12.323
.text
	li 	$v0, 1
	lwc1	$f1, float_integer
	syscall	
