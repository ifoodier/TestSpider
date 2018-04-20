# -*- coding: utf-8 -*-
import re
"""
.   任意单个字符
[]  字符集，对单个字符给出取值范围，    [abc]表示a、b、c，[a-z]表示a到z单个字符
[^] 非字符集，对单个字符给出排除范围，  [^abc]表示非a或b或c的单个字符
*   前一个字符0次或多次 ，             abc* 表示ab、abc、abccc等
+   前一个字符1次或多次
?   前一个字符0次或1次，               abc? 表示ab、abc
|   左右表达式任意一个，               abc|def表示abc、def
{m} 前一个字符m次，ab{2}c表示abbc
{m,n}前一个字符m至n次（含n），         ab{1,2}c 表示abc、abbc
^   匹配字符串开头，                   ^abc表示abc且在一个字符串的开头
$   匹配字符串结尾，                   abs$表示abc且在一个字符串的结尾
()  分组标记，内部只能使用|操作符，     (abc)表示abc，(abc|def)表示abc、def
\d  数字，等价于[0-9]
\w  单词字符，等价于[A-Za-z0-9]

^[A-Za-z]+$     由26个字母组成的字符串
^-?\d+$         整数形式字符串
^[0-9]*[1-9][0-9]*[0-9] 正整数
[1-9]\d{5}      中国境内邮政编码，6位
[\u4e00-\u9fa5] 中文字符
\d{3}-\d{8}|\d{4}-\d{7} 国内电话号码
(([1-9]?\d | 1\d{2} | 2[0-4]\d | 25[0-5]).){3}([1-9]?\d | 1\d{2} | 2[0-4]\d | 25[0-5]) IP地址字符串形式
"""

"""
raw string 原生字符串类型，是不包含转义符的字符串
如：  r'\d{3}-\d{8}'
string 
如：  r'\\d{3}-\\d{8}'
"""

"""
Re库主要功能函数
re.search(pattern, string, flags=0) 在一个字符串中搜索匹配正则表达式的第一个位置，返回match对象
    * pattern：正则表达式的字符串或原生字符串表示
    * string：待匹配字符串
    * flags：正则表达式使用时的控制标记
        + re.I re.IGNORECASE 忽略正则表达式的大小写
        + re.M re.MULTILINE ^ 操作符能够将给定字符串的每行当作匹配开始
        + re.S re.DOTALL . 操作符能够匹配所有字符（包括换行符）
re.match(pattern, string, flags=0)  从一个字符串的开始位置起匹配正则表达式，返回match对象，即只有在0位置匹配成功才有返回
    * pattern：正则表达式的字符串或原生字符串表示
    * string：待匹配字符串
    * flags：正则表达式使用时的控制标记
re.findall(pattern, string, flags=0)搜索字符串，以列表类型返回全部能匹配的子串
    * pattern：正则表达式的字符串或原生字符串表示
    * string：待匹配字符串
    * flags：正则表达式使用时的控制标记
re.split(pattern, string, maxsplit=0, flags=0)  将一个字符串按照正则表达式匹配结果进行分割，返回列表类型
    * pattern：正则表达式的字符串或原生字符串表示
    * string：待匹配字符串
    * maxsplit: 最大分割数，剩余部分作为最后一个元素（整体）输出
    * flags：正则表达式使用时的控制标记
re.finditer(pattern, string, flags=0)搜索字符串，返回一个匹配结果的迭代类型，每个迭代元素是match类型
    * pattern：正则表达式的字符串或原生字符串表示
    * string：待匹配字符串
    * flags：正则表达式使用时的控制标记
re.sub(pattern, repl, string, count=0, flags=0)    在一个字符串中替换所有匹配正则表达式的子串，返回替换后的字符串
    * pattern：正则表达式的字符串或原生字符串表示
    * repl：替换匹配字符串的字符串
    * string：待匹配字符串
    * count：匹配的最大替换次数
    * flags：正则表达式使用时的控制标记
"""

# match = re.search(r'[1-9]\d{5}', 'BIT 100081')
# if match: #若为空，会报错
#     print(match.group(0))

# match = re.search(r'[1-9]\d{5}', '100081 BIT')
# if match:
#     print(match.group(0))

# ls = re.findall(r'[1-9]\d{5}', 'BIT100081 TSU100084')
# print(ls)
# for l in ls:
#     print(l)


# split = re.split(r'[1-9]\d{5}',  'BIT100081 TSU100084')
# print(split)
# split = re.split(r'[1-9]\d{5}',  'BIT100081 TSU100084', maxsplit=1)
# print(split)

# for m in re.finditer(r'[1-9]\d{5}', 'BIT100081 TSU100084'):
#     if m:
#         print(m.group(0))

print(re.sub(r'[1-9]\d{5}', ':zipoode', 'BIT100081 TUS100084'))

