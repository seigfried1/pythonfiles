# card_no = 378282246310005
def credit_card_no_checker(card_no):
    card_no_list = [int(i) for i in str(card_no)]
    
    step_one_list = []
    for i in range(len(card_no_list)-1):
        if i%2 != 0:
            step_one_list.append(card_no_list[i] * 2)
    
    step_one_list_string = []
    for i in step_one_list:
        step_one_list_string.append(str(i))
    
    
    a = ''.join(step_one_list_string)
    
    step_one_addition = 0
    for i in a:
        step_one_addition += int(i)
    
    
    step_two_list = []
    for i in range(len(card_no_list)):
        if i%2 == 0:
            step_two_list.append(card_no_list[i])
    
    
    final_ans = step_one_addition
    for i in step_two_list:
        final_ans += i
    
    if final_ans % 10 == 0:
        print("card seems legit")
