def widrawls(balance, withlst):
    msg = ""
    msg_lst = []
    for item in withlst:
        if item <= balance:
            balance -= item
            msg = f"Withdrawn: {balance}"
            msg_lst.append(msg)
        else:
            msg = f"Insufficient funds for requested amount: {balance}"
            msg_lst.append(msg)
        
    msg = f"Remaining Balance: {balance}"
    msg_lst.append(msg)
    return msg_lst
            
            

res = widrawls(1000, [34,50,15,8])
print(res)