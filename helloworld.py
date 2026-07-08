def main():
    print("Hello, World!")
    name = input("你叫什么名字？")
    print(f"你好，{name}！欢迎学习 Git！")

def print_time():
    print("当前时间是：", time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()),"该休息了")
if __name__ == "__main__":
    main()
    print_time()
    
