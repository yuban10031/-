def discounts(price,rate):
    final_price = price * rate
    old_price = 88 #这里试图修改全局变量
    print('修改后old_price的值是:',old_price)#这个是局部变量
    return final_price
old_price = float(input('请输入原价：'))#这个是全局变量
rate = float(input('请输入折扣价：'))
new_price = discounts(old_price,rate)
print('修改后old_price的值是:',old_price)
print('打折后的价格是：',new_price)
