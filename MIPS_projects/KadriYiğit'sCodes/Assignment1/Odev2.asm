#Lists are defined here
.data
list_A: .word 1, 3, 5, 6, 9, 13, 16, 18
list_B: .word 2, 4, 7, 8, 12, 15, 20
list_C: .word
.text
la $s0, list_A    # based address of list A loaded into $s0
addi $s1, $zero, 8  # $s1 is set to the size of the list A
la $s2, list_B      # based address of list B loaded into $s2
addi $s3, $zero, 7  # $s3 is set to the size of the list B
la $s4, list_C      # based address of list C loaded into $s4


# Continue to write your code here

addi $t9,$zero,0

# arr1=$s0 ; n1=$s1 ; arr2=$s2 ; n2=$s3 ; arr3=$s4

mergeArrays1:
addi $t0,$zero,0 # i=0
addi $t1,$zero,0 # j=0
addi $t2,$zero,0 # k=0
#j whileLoop_m1
j Exit

mergeArrays2:
j whileLoop_m2

mergeArrays3:


## while (i<n1 && j <n2) ...
whileLoop_m1:
#### check for condition (i<n1 && j <n2)
slt $t9,$t0,$s1  # temp9=(i<n1)
beq $t9,$zero,mergeArrays2 # temp9==0 => jump mergeArrays2
slt $t9,$t0,$s3  # temp9=(j<n2)
beq $t9,$zero,mergeArrays2 # temp9==0 => jump mergeArrays2
####!
#### load arr1[i] to $t5
sll $t9,$t0,2
add $t9,$t9,$s0
lw $t5,0($t9)
####!
#### load arr2[j] to $t6
sll $t9,$t1,2
add $t9,$t9,$s2
lw $t6,0($t9)
####!
#### check if (arr1[i] < arr2[j])
slt $t9,$t5,$t6  # temp9=(arr1[i]<arr2[j])
bne $t9,$zero,ifCondition # temp9==1 => jump ifCondition
beq $t9,$zero,elseCondition # temp9==0 => jump elseCondition
####!
ifCondition:
#### save arr1[i] to arr3[k]
sll $t9,$t2,2
add $t9,$t9,$s4
sw $t5,0($t9) # arr3[k] = arr1[i]
####!
addi $t0,$t0,1 # i++
addi $t2,$t2,1 # k++
j whileLoop_m1
elseCondition:
#### save arr2[j] to arr3[k]
sll $t9,$t2,2
add $t9,$t9,$s4
sw $t6,0($t9) # arr3[k] = arr2[j]
####!
addi $t1,$t1,1 # j++
addi $t2,$t2,1 # k++
j whileLoop_m1
##!

## while (i < n1) ...
whileLoop_m2:
slt $t9,$t0,$s1  # temp9=(i<n1)
beq $t9,$zero,mergeArrays3 # temp9==0 => jump mergeArrays3
#### load arr1[i] to $t5
sll $t9,$t0,2
add $t9,$t9,$s0
lw $t5,0($t9)
####!
#### save arr1[i] to arr3[k]
sll $t9,$t2,2
add $t9,$t9,$s4
sw $t5,0($t9) # arr3[k] = arr1[i]
####!
addi $t0,$t0,1 # i++
addi $t2,$t2,1 # k++
j whileLoop_m2
##!

## while (j < n2) ...
whileLoop_m3:
slt $t9,$t0,$s3  # temp9=(j<n2)
beq $t9,$zero,Exit # temp9==0 => jump Exit
#### save arr2[j] to arr3[k]
sll $t9,$t2,2
add $t9,$t9,$s4
sw $t6,0($t9) # arr3[k] = arr2[j]
####!
addi $t1,$t1,1 # j++
addi $t2,$t2,1 # k++
j whileLoop_m3

Exit: 