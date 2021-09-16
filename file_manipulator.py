#basic helper functions 

def read_file(file_name):
    try:
        file=open(file_name, "r")
        lines=file.readlines()
        file.close()
        return lines
    except:
        print('ERR: File read failed!')
        return None

def write_file(file_name,lines,method):
    try:
        file=open(file_name,method)
        file.writelines(lines)
        file.close()
    except:
        print('ERR: File write failed!')
        return None

def store_streak(top_streak):
    try:
        file=open('data/top_streak.txt','w')
        file.write(str(top_streak))
        file.close()
    except:
        print('ERR: File streak save failed!')
    return None