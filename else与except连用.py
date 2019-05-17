try:
    with open('data.txt','w') as f:
        for each_line in f:
            print(eaach_line.readline())
        
except OSError as reason:
    print('出错了：'+ str(reason))
finally:
    f.close()
