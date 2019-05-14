clc
clear all
close all
disp('============================= ASSIGNMENT 1 =======================');
disp('Name: Nejat');
disp('Surname: Günaydýn');
disp('Student ID: 213861517');
disp('==================================================================');
disp(' ');

disp('Press any key to continue, or press to - and than to enter to break');
str=input('','s');
if(str=='-')
disp('END');
break
end

disp('============================= QUESTION 1 =========================');
disp(' PART 1.1');
disp(' ');

t=0:0.1:1;
sizeMATRIXt=size(t);
sizeOFt=sizeMATRIXt(1,2);
mt=zeros(1,sizeOFt);
for (i=1:sizeOFt)
    mt(1,i)=cos(2*pi*t(1,i));
end

disp('for t =');
disp(t);

disp('m(t) =');
disp(mt);

disp('Press any key to continue, or press to - and than to enter to break');
str=input('','s');
if(str=='-')
disp('END');
break
end

disp(' PART 1.2');
disp(' ');

levelsBetween=-1:(2.0/8):1;
disp('levelsBetween =');
disp(levelsBetween);
disp('levels :')
for(i=1:8)
   tempText=['between ',num2str(levelsBetween(1,i)),' and ',num2str(levelsBetween(1,i+1))];
   disp(tempText);
end
disp(' ');
disp('8 levels, so 3 bit will be enough.')
disp('lowes level is level between -1 and -0.75');
disp('    and its bit sequence will be 000 because the lowest level being represent by 0 bits (bits of zeros).');
disp('other levels: ');
disp('    between -0.75 and -0.5 : 001');
disp('    between -0.5 and -0.25 : 010');
disp('    between -0.25 and 0.00 : 011');
disp('    between 0.00 and 0.25  : 100');
disp('    between 0.25 and 0.50  : 101');
disp('    between 0.50 and 0.75  : 110');
disp('    between 0.75 and 1.00  : 111');
disp(' ');
disp('so, signal m(t) when t between 0 and 1 will be:');
output1='';
for (i=1:sizeOFt)
    if(levelsBetween(1,1)<mt(1,i) & mt(1,i)<levelsBetween(1,2))
        output1 = strcat(output1,'000_');
    elseif(levelsBetween(1,2)<mt(1,i) & mt(1,i)<levelsBetween(1,3))
        output1 = strcat(output1,'001_');
    elseif(levelsBetween(1,3)<mt(1,i) & mt(1,i)<levelsBetween(1,4))
        output1 = strcat(output1,'010_');
    elseif(levelsBetween(1,4)<mt(1,i) & mt(1,i)<levelsBetween(1,5))
        output1 = strcat(output1,'011_');
    elseif(levelsBetween(1,5)<mt(1,i) & mt(1,i)<levelsBetween(1,6))
        output1 = strcat(output1,'100_');
    elseif(levelsBetween(1,6)<mt(1,i) & mt(1,i)<levelsBetween(1,7))
        output1 = strcat(output1,'101_');
    elseif(levelsBetween(1,7)<mt(1,i) & mt(1,i)<levelsBetween(1,8))
        output1 = strcat(output1,'110_');
    elseif(levelsBetween(1,8)<mt(1,i) & mt(1,i)<levelsBetween(1,9))
        output1 = strcat(output1,'111_');
    end
end
disp(output1);
disp(' ');
disp('Press any key to continue, or press to - and than to enter to break');
str=input('','s');
if(str=='-')
disp('END');
break
end

disp(' PART 1.3');
disp(' ');
disp('signal m(t) when t between 0 and 1 will be:');
disp(output1);

disp('Press any key to continue, or press to - and than to enter to break');
str=input('','s');
if(str=='-')
disp('END');
break
end

disp(' PART 1.4');
disp(' ');
% ================== PUT YOUR CODE HERE ===================================


disp('Press any key to continue, or press to - and than to enter to break');
str=input('','s');
if(str=='-')
disp('END');
break
end

disp(' PART 1.5');
disp(' ');
% ================== PUT YOUR CODE HERE ===================================


disp('Press any key to continue, or press to - and than to enter to break');
str=input('','s');
if(str=='-')
disp('END');
break
end

disp('============================= QUESTION 2 =========================');
disp(' PART 2.1');
disp(' ');
digitsMAT=load('digits.mat');
f=whos('-file','digits.mat');
int=digitsMAT.AvgLength;
numel(num2str(abs(int)));

disp('Press any key to continue, or press to - and than to enter to break');
str=input('','s');
if(str=='-')
disp('END');
break
end

disp(' PART 2.2');
disp(' ');
% ================== PUT YOUR CODE HERE ===================================


disp('Press any key to continue, or press to - and than to enter to break');
str=input('','s');
if(str=='-')
disp('END');
break
end

disp(' PART 2.3');
disp(' ');
% ================== PUT YOUR CODE HERE ===================================


disp('Press any key to continue, or press to - and than to enter to break');
str=input('','s');
if(str=='-')
disp('END');
break
end

disp(' PART 2.4');
disp(' ');
% ================== PUT YOUR CODE HERE ===================================


disp('Press any key to continue, or press to - and than to enter to break');
str=input('','s');
if(str=='-')
disp('END');
break
end

disp(' PART 2.5');
disp(' ');
% ================== PUT YOUR CODE HERE ===================================


disp('Press any key to continue, or press to - and than to enter to break');
str=input('','s');
if(str=='-')
disp('END');
break
end

disp(' PART 2.6');
disp(' ');
% ================== PUT YOUR CODE HERE ===================================


disp('Press any key to continue, or press to - and than to enter to break');
str=input('','s');
if(str=='-')
disp('END');
break
end

disp('============================= QUESTION 3 =========================');
disp(' PART 3.1');
disp(' ');
% ================== PUT YOUR CODE HERE ===================================


disp('Press any key to continue, or press to - and than to enter to break');
str=input('','s');
if(str=='-')
disp('END');
break
end

disp(' PART 3.2');
disp(' ');
% ================== PUT YOUR CODE HERE ===================================


disp('Press any key to continue, or press to - and than to enter to break');
str=input('','s');
if(str=='-')
disp('END');
break
end

disp(' PART 3.3');
disp(' ');
% ================== PUT YOUR CODE HERE ===================================


disp(' ');
disp('END');