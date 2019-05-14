addi $s0,$zero,0  # sum=0

# In python, "for x in range(1,10,2)" starts from x=1 and then do x=x+2 while x<10 .
addi $t0,$zero,1  # x=1
addi $t2,$zero,10  # temp2=10
j forLoop1

forLoop1: addi $t1,$zero,0  # y=0
          jal whileLoop # jump and link to $ra

# In python, "while y<=x" checks if y<=x ; then continue if it is, else exit .
whileLoop: add $s0,$s0,$t1 # sum=sum+y
           addi $t1,$t1,1  # y=y+1
           slt $t3,$t1,$t0  # temp3=(y<x)
           bne $t3,$zero,whileLoop
           bne $t1,$t0,forLoop2 # if y!=x jump forLoop2
           jr $ra

forLoop2: addi $t0,$t0,2  # x=x+2
          slt $t4,$t0,$t2  # temp4=(x<temp2) ; temp2=10
          bne $t4,$zero,forLoop1
          j Exit

Exit:
