
# x=$t0; y=$t1; i=$t2 ; temp3=12=$t3 ; temp4=2=$t4 ; sum=$s0

addi $t0,$zero,12  # x=12
addi $t1,$zero,1  # y=1
addi $s0,$zero,0  # sum=0

WhileLoop1: 
slt $t9,$t1,$t0  # temp9=(y<x)
bne $t9,$zero,ForLoop1 # temp9==1 => jump ForLoop1
beq $t1,$t0,ForLoop1 # y==x => jump ForLoop1
j WhileLoop2

WhileLoop2: 
addi $t1,$t1,1  # y=y+1
slt $t9,$t1,$t0  # temp9=(y<x)
bne $t9,$zero,WhileLoop1 # temp9==0 => jump WhileLoop1
beq $t1,$t0,WhileLoop1 # y==x => jump WhileLoop1
j Exit

# In python, "for i in range(y,12,3)" starts from i=y and then do i=i+3 while i<12 .
ForLoop1: addi $t2,$t1,0  # i=y
          addi $t3,$zero,12  # temp3=12
          j Condition

Condition: addi $t4,$zero,2 # temp4=2	
           div $t6, $t2, $t4 # i / 2 = temp6
           mfhi $t7 #kalan
           beq $t7,$zero,IfCondition
           bne $t7,$zero,ElseCondition
           j ForLoop2

IfCondition: addi $s0,$s0,1  # sum=sum+1
             j ForLoop2
	
ElseCondition: addi $s0,$s0,2  # sum=sum+2
               j ForLoop2
               
ForLoop2: addi $t2,$t2,3  # i=i+3
          slt $t9,$t2,$t3  # temp9=(i<temp3=12)
          bne $t9,$zero,ForLoop1 # temp9==1 => jump ForLoop1
          j WhileLoop2
	
Exit: 
