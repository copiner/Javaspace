f = open("record.txt")
boy = []
girl = []
count = 1
for line in f:
    if line[:6] != '======':
        (role, chat) = line.split(':', 1)
        if role == 'calvin':
            boy.append(chat)
        if role == 'rose':
            girl.append(chat)
    else:
        file_name_boy = 'boy_'+str(count)+'.txt'
        file_name_girl = 'girl_'+str(count)+'.txt'

        boy_file = open(file_name_boy, 'w')
        girl_file = open(file_name_girl, 'w')

        boy_file.writelines(boy)
        girl_file.writelines(girl)
        
        boy_file.close()
        girl_file.close()

        boy = []
        girl = []
        count += 1

file_name_boy = 'boy_'+str(count)+'.txt'
file_name_girl = 'girl_'+str(count)+'.txt'

boy_file = open(file_name_boy, 'w')
girl_file = open(file_name_girl, 'w')

boy_file.writelines(boy)
girl_file.writelines(girl)
        
boy_file.close()
girl_file.close()
f.close()
