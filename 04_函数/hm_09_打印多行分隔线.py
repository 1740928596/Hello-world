def print_line(char,times):
    """
打印任意字符任意次数的字符串
    :param char:
    :param times:
    """
    print(char*times)


def print_lines(char,times):
    """
打印5行分隔线
    :param char:字符串
    :param times:次数
    """
    i = 0
    while i < 5:
        print_line(char,times)
        i+=1
print_lines("任意字符",9)