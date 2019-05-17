def save_file(boy,girl,count):
    file_name_boy = 'boy_' + str(count) + '.txt'
    file_name_girl = 'girl_' + str(count) + '.txt'

    boy_file = open(file_name_boy,'w')
    girl_file = open(file_name_girl,'w')

    boy_file.writelines(boy)
    gilr_file.writelines(girl)

    boy_file.close()
    girl_file.close()
                       

def split_file(file_name):     
    f = open('C:\\KuGou\\明日方舟.txt',mode='r', encoding='UTF-8')

    boy = []
    girl = []
    count = 1

    for each_line in f:
        if each_line[:3] != '=====':
            (role, line_spoken) = each_line.split(':',1)
            if role == '位移':
                boy.append(line_spoken)
            if role == '召唤':
                girl.append(line_spoken)
                
            
        #我们这里进行字符串分割操作
        else:
            save_file(boy,girl,count)

            boy = []
            girl = []
            count +=1
            
    save_file(boy,girl,count)
    f.close()
        #文件的分别保存操作
        
