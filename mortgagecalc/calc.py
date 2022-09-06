

def pay_in_mon(price, first_pay, percent, credit_time):
    credict = int(price) - int(first_pay)
    first_pars = credict*(float(percent)/1200)
    second_pars = 1-(1+(float(percent)/1200))**-float(credit_time)
    return first_pars/second_pars


def overpay(pay_in_month, credit_time, price, first_pay):
    credict = int(price) - int(first_pay)
    return int(pay_in_month)*int(credit_time)-int(credict)