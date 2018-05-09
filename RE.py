import re
# . 单个字符
# [] 字符集　[abc]表示a、b、c,[a-z]表示a到z单个字符
# [^] 非字符集 [^abc]表示非a或b或c的单个字符
# * 前一个字符0次或无限次扩展 abc*表示ab、abc、abcc、abccc等
# + 前一个字符１次或无限次扩展 abc+表示abc、abcc、abccc等
# ?　前一个字符０次或１次扩展 abc？表示ab、abc
# |　左右表达式任意一个 abc|def 表示abc、def
# {m} 扩展前一个字符m次 ab{2}c表示abbc
# {m,n} 扩展前一个字符m至n次(包含n) ab{1,2}c表示abc、abbc
# ^ 匹配字符串开头 ^abc表示abc切在一个字符串的开头
# $ 匹配字符串结尾 abc$表示abc且在一个字符串的结尾
# () 分组标记，内部只能使用|操作符
# \d 数字，等价于[0-9]
# \w 单词字符，等价于[A-Za-z0-9]

# ^[A-Za-z]+$ 由26个字母组成的字符串
# ^[A-Za-z0-9]+$ 由26个字母和数字组成的字符串
# ^-?\d+$ 整数形式的字符串
# ^[0-9]*[1-9][0-9]*$ 正整数形式的字符串
# [0-9]\d{5}　中国境内邮政编码　６位
# [\u4ee00-\u9fa5] 匹配中文字符
# \d{3}-\d{8}|\d{4}-\d{7} 国内电话号码　
# (([1-9]?\d|1\d{2}|2[0-4]\d|25[0-5]).){3}([1-9]?\d|1\d{2}|2[0-4]\d|25[0-5]) ip地址

# re.search(pattern,string,flags=0) #　搜索匹配正则表达式的第一个位置,返回match对象
# flags:re.I 忽略大小写
# flags:re.M ^操作符能够给定字符串的每行当做匹配开始
# flags:re.S 操作符"."能匹配所有字符,默认匹配除换行外的所有字符

match = re.search(r'[1-9]\d{5}','BIT 100081')
if match:
    print(match.group(0))

# re.match() # 从开始位置起匹配正则表达式
match = re.match(r'[1-9]\d{5}','100081 BIT')
if match:
    match.group(0)

# re.findall() # 搜索字符串,以列表类型返回全部能匹配的子串
ls = re.findall(r'[1-9]\d{5}]','BIT100081 TSU100084')
print(ls)

# re.split(pattern, string, maxsplit=0, flags=0) # 将一个字符串按照正则表达式匹配结果进行分割,返回列表类型
ls = re.split(r'[1-9]\d{5}','BIT100081 TSU100084', maxsplit=1)
print(ls)

# re.finditer(pattern,string,flags) # 搜索字符串,返回一个匹配结果的迭代类型，每个迭代元素是match对象
for m in re.finditer(r'[1-9]\d{5}','BIT100081 TSU100084'):
   if m:
       print(m.group(0))

# re.sub(pattern,repl替换的字符串,string,count=0最大替换次数,flags=0) # 在一个字符串中替换所有匹配正则表达式的子串,返回替代后的字符串
print(re.sub(r'[1-9]\d{5}',':zipcode','BIT100081 TSU100084'))

# 正则表达式面向对象用法
# regex = re.compile(pattern,flags)
pat = re.compile(r'[1-9]\d{5}')
rst = pat.search('BIT 100081')

# match
# string 待匹配的文本
# re 匹配使用的pattern对象(re)
# pos 正则表达式的开始位置
# endpos 结束位置

# group(0) 获得匹配后的字符串
# start() 匹配字符串在原始字符串的开始位置
# end() 结束位置m.stirng,
# span() 返回()(start(),end())
m = re.match(r'[1-9]\d{5}]','BIT100081 TSU100084')
print(type(m))
# print(m.stirng,m.re,m.pos,m.endpos,m.group(0),m.start(),m.end(),m.span())

# 默认最长匹配
match = re.search(r'PY.*N','PYANDNCNDN')
# *? 前一个字符0次或者无限次扩展,最小匹配
# +? 前一个字符1次或者无限次扩展,最小匹配
# ?? 前一个字符0次或者1次扩展,最小匹配
# {m,n}? 扩展一个字符m次至n(含n),最小匹配

print(match.group(0))



