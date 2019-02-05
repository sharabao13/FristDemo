#数据类型 set 结合
s1 = {1,2,3,4,'a'}
s2 = {2,3,8,9,'a','b'}
#print (s1,s2)     打印常规集合
#print ('c' in s1)  #判断c元素是否在集合内  用in 内置函数
#print ('f' not in s1)  #判断元素f是否不再集合内 用not in
#集合的 交集 & 并集 |  差集 - 反差集 ^ 
#print (s1 & s2)
#print (s1 | s2)
#print (s1 - s2)  #s1 - s2 找s1 与s2 不同的元素
#print (s2 - s1)   #s2 - s1 找s2 与s1 不同的元素
#print (s1 ^ s2) 
# set内置函数  建立一个无序不重复的元素值
s3 = set("hello python")
#print (s3)
#字典 dictionary 数据类型
dic = {"name":"tom","age":26,"sex":"man"}  
#print (dic) '
#print (dic ["name"])  # 字典索引
#print ("tom" in dic)  #只能查找key 不能查找value
dic ["sex"] = "girl"
#print (dic)
del dic ["age"]  #删除某个key 相等的value也会一起删掉
#print (dic)
#列表跟字典的复合使用
dic = {i:i * 2 for i in [2,4,56,7,8]}
print (dic) 