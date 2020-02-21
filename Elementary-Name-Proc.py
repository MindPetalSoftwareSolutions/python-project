namevar = str(input("Enter Name to Check: "))
eval_string ='6'
write_instances = int(input("How Many Times Shall I Write It: "))
eval_chars = int(input("Which Character Would You Like to Know?: "))
index_account = -1
count = 0

while (count < write_instances):
    eval_string = eval_string + namevar
    count = count + 1
    # Print (count)

print (eval_string [eval_chars + index_account])
# Print (eval_chars)