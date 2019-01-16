
# function to check if a bit-vector has only one of its elements as '1'
# Eg : 1000 ; ans is yes 
#      0100 ; ans is yes 
#      1010 ; ans is No
#      0000 ; ans is No 

# solution : sol is to perform subtraction of '1' from given number and perform and operation between orignal number and result. If result is 
# '0' then it has only one '1' else multiple '1''s  or all '0''s
