addi $s0,$zero,0

addi $t0,$zero,1
addi $t2,$zero,10
j LoopFor1

LoopFor1: addi $t1,$zero,0
          j loopWhile

loopWhile: add $s0,$s0,$t1
           addi $t1,$t1,1
           slt $t3,$t1,$t0
           bne $t3,$zero,loopWhile
           j loopCheck
           
loopCheck: bne $t1,$t0,LoopFor2
           j loopWhile

LoopFor2: addi $t0,$t0,2
          slt $t4,$t0,$t2
          bne $t4,$zero,LoopFor1
          j Exit

Exit:
