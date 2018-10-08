def save_file(boy, girl, count):
    file_name_boy = 'boy_'+str(count)+'.txt'
    file_name_girl = 'girl_'+str(count)+'.txt'

    boy_file = open(file_name_boy, 'w')
    girl_file = open(file_name_girl, 'w')

    boy_file.writelines(boy)
    girl_file.writelines(girl)
        
    boy_file.close()
    girl_file.close()


def split_file(file_name):
    f = open(file_name)
    
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
            save_file(boy, girl, count)

            boy = []
            girl = []
            count += 1

    save_file(boy, girl, count)

    f.close()

split_file('record.txt')
