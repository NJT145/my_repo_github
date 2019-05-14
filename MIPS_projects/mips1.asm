addi $s0,$zero,10  # x=10
addi $s1,$zero,2  # y=2


mult $s0,$s1
mfhi $t0 # remainder
mflo $t1 # result