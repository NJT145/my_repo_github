#A list is defined here
.data
my_array: .word 10, 9, 2, 3, 1, 4, 6, 7, 32
.text
la $s0, my_array    # based address of list loaded into $s0
addi $s1, $zero, 9  # $s1 is set to the size of the list 

# Now you have the size and the base address of the list
# You should be able to find the mean of the list and the diffence between maximum and minimum elements in the list.
# Continue to write your code here

################################################
# $s0=my_array
# $s1=size
# $s2=mean=0
# $s3=farthest_pair_diff=max-min
# $s4=sum
# $t0=i
# $t1=min
# $t2=max
# $t3=temp3=my_array[i]
# $t4=temp4=x*4
# $t5=temp5=(x<size)
# $t6=temp6
# $t7=temp7=max>my_array[x]
################################################
# my python code plan:
## sum=0
## min=my_array[0]
## max=0
## for i in range(size):
##     sum+=my_array[i]
## for i in range(size):
##     if my_array[i]<min:
##         min=my_array[i]
## for i in range(size):
##     if my_array[i]>max:
##         max=my_array[i]
## mean=sum/size
## farthest_pair_diff=max-min
################################################

addi $s2,$zero,0  # mean=0
addi $s3,$zero,0  # farthest_pair_diff=0
addi $s4,$zero,0  # sum=0
addi $t0,$zero,0  # i=0
lw $t1,0($s0) # min=my_array[0]
addi $t2,$zero,0  # max=0

j forLoop


forLoop: sll $t4,$t0,2
          add $t4,$t4,$s0
          lw $t3,0($t4) 
          add $s4,$s4,$t3 
          addi $t0,$t0,1  # x=x+1
          slt $t5,$t0,$s1  # temp5=(x<size)
          bne $t5,$zero,forLoop
          j nextStep


nextStep: div $s4,$s1 # sum/size
          mflo $s2 # mean=sum/size
          
          addi $t0,$zero,0  # x=0
          addi $t5,$zero,0  # temp5=0
          j forLoop2

# check if min<my_array[x]
forLoop2: sll $t4,$t0,2
          add $t4,$t4,$s0
          lw $t3,0($t4) # $t3 = my_array[x]
          slt $t6,$t3,$t1 # temp6=(my_array[x]<min)
          bne $t6,$zero,changeMin
          addi $t0,$t0,1  # x=x+1
          slt $t5,$t0,$s1  # temp5=(x<size)
          bne $t5,$zero,forLoop2
          j nextStep2

changeMin: add $t1,$zero,$t3 # min=my_array[x]
           addi $t0,$t0,1  # x=x+1
           slt $t5,$t0,$s1  # temp5=(x<size)
           bne $t5,$zero,forLoop2
           j nextStep2

nextStep2:addi $t0,$zero,0  # x=0
          addi $t5,$zero,0  # temp5=0
          addi $t6,$zero,0  # temp6=0
          addi $t2,$zero,0  # max=0
          j forLoop3

forLoop3: sll $t4,$t0,2
          add $t4,$t4,$s0
          lw $t3,0($t4) # $t3 = my_array[x]
          slt $t6,$t3,$t1 # temp6=(my_array[x]<max)
          beq $t6,$zero,checkMaxEqualOrBigger # if temp6=0 then max>=my_array[x]
          addi $t0,$t0,1  # x=x+1
          slt $t5,$t0,$s1  # temp5=(x<size)
          bne $t5,$zero,forLoop3
          j Exit

# check if max>my_array[x]
checkMaxEqualOrBigger: bne $t3,$t2,changeMax
                       j Exit

changeMax: add $t2,$zero,$t3 # max=my_array[x]
           addi $t0,$t0,1  # x=x+1
           slt $t5,$t0,$s1  # temp5=(x<size)
           bne $t5,$zero,forLoop3
           j Exit

Exit: sub $s3,$t2,$t1


# sum=74 ; mean=8.222 ; max-min=31