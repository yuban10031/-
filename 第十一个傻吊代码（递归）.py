#def fab(n):
#    n1 = 1
 #   n2 = 1
  #  n3 = 1
#
 #   if n<1:
  #      print('输入有误')
   #while (n-2)> 0 :
    #    n3 = n1 + n2
     #   n1 = n2
      #  n2 = n3
       # n -= 1

    #return n3
#number = int(input('请输入刚开始有几只兔子：'))
#result = fab(number)
#if result !=-1:
 #   print('总共有%d只兔子诞生：' %(result))


def fab(n):
    if n<1:
        print('输入有误')
        return -1
    if n ==1 or n ==2:
        return 1
    else:
        return fab(n-1)+fab(n-2)

number = int(input('请输入刚开始有几只兔子：'))
result = fab(number)
if result !=-1:
    print('总共有%d只兔子诞生：' %result)    
    
