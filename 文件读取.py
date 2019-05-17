if __name__ == '__main__':
    fileHandler = open('C:\\KuGou\\明日方舟.txt', mode='r', encoding='UTF-8')
    report_lines = fileHandler.readlines()
    for line in report_lines:
        print(line.rstrip())
