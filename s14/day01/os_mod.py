import os

# cmd_res = os.system("dir") # 执行命令，不保存结果
cmd_res = os.popen("dir").read()
print("-->", cmd_res)

# 在当前目录下，创建文件夹
os.mkdir("new_dir")
