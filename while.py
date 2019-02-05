# 1- 100 的偶数
# for x in range(1,101) :
#     print (x)
#     # x = x + 1    
# x = 0
# count = 0
# while x < 100 :
#     x += 1
#     if x % 2 > 0 :
#         count = count + x
#         print (x)
# print (count)

count = 0
while count < 3 :
    user_n = input ("请输入用户名: ")
    pass_wd = input ("请输入密码 :")
    if user_n == "admin" and pass_wd == "123456" :
        print ("欢迎登录")
        break
    else :
        print ("用户名或密码错误")
        count = count + 1
else :
    print ("请稍后再试")


