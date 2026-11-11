print("=======欢迎使用房贷计算器======")
while True:
    #选择房贷类型
    loan_type= input("请输入房贷类型(1:商业贷款  2:公积金贷款  exit:退出):")
    if loan_type == "exit" :
        print("已经退出！")
        break       #遇到break关键字强行跳出循环

    if loan_type == "1":
        type_name = "商业贷款"
    elif loan_type == "2":
        type_name = "公积金贷款"
    else:
        print("输入的贷款类型有误，请重新个输入！\n")
        continue

#贷款的金额和期限
    type_money = float(input("请输入贷款金额："))
    type_year = float(input("请输入贷款年限( 年): "))

#根据贷款的类型，
    if loan_type == "1":
        if type_year <=5:
            year_rate =0.0475
        else :
            year_rate =0.049
    elif loan_type == "2":
        if type_year <=5:
            year_rate =0.026
        else :
            year_rate =0.031

    #按等额本息公式计算
    month_rate = year_rate/12 #月利率 =利率 / 12
    months = type_year * 12     #还款月数=期限*12
    pow_value = (1+month_rate)**months  #
    month_pay = type_money * month_rate * pow_value/(pow_value -1)
    total_pay = month_pay *months
    total_interest=total_pay - type_money

    #输出最终结果
    print("---------计算结果---------")
    print(f"贷款类型：{type_name}(年利率：{year_rate*100:.2f}%)")
    print(f"每月月供：{month_pay:.2f}元")
    print(f"还款总额：{total_pay:.2f}元")
    print(f"支付利息：{total_interest:.2f}元")
    print()


