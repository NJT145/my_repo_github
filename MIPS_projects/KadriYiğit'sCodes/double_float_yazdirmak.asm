.data
	double_integer: .double 5.4566
	double_integer2: .double 0.0
.text
	ldc1, $f2, double_integer
	ldc1, $f0, double_integer2
	li $v0, 3
	add.d $f12, $f2, $f4
	syscall
	