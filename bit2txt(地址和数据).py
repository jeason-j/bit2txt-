# -*- coding: utf-8 -*-
# @Time    : 2019/6/13 10:32
# @Author  : 
# @Site    : 
# @File    : bit2txt(地址和数据).py
# @Software: PyCharm
# Function : 128M Flash bit转txt，包含地址和数据
# @Email   :
# @Version :

import time
import binascii

# 读取bit文件 和 bit文件的长度
file_bit = open('hexbin_test.bin', 'rb')
# 读取bit文件全部内容，（byte类型:b'\x01\x02\x03\x04\x05\x06\x07\x0f'）
file_bit_read = file_bit.read()
file_bit_len = len(file_bit_read)
print((file_bit_len))
# print(type(file_bit_read))
# print(file_bit_read)
# print('here')


count = 0
# 写入txt文件
with open('bit2txt.txt', 'w') as fp:
    while count < len(file_bit_read):
        # 读取bit文件中byte （int类型：1）
        bit_read_byte = file_bit_read[count]
        # print(type(bit_read_byte))
        # print(bit_read_byte)

        # hex（）将读取int 类型 10进制--转换成16进制字符串（str类型：0x1）
        bit_read_hex = hex(bit_read_byte)
        # print(type(bit_read_hex))
        # print(bit_read_hex)
        # 去掉十六进制0x，0x1-->1
        bit_read_hex_no_0x = bit_read_hex.replace('0x', '')
        # print(bit_read_hex_no_0x)

        # 测试用，延时0.5s
        # time.sleep(0.5)

        # 数据，十六进制字符串 补全2位，小写转大写
        data_read_hex = bit_read_hex_no_0x.zfill(2).upper()
        # print(data_read_hex)

        # 将count 转换成 16进制 地址
        addr_hex = hex(count)
        # 地址,去除0x，然后，补全成8位 00000 0000,并转成大写
        addr_hex_8bit = addr_hex.replace('0x', '').zfill(8).upper()


        # 写入bin文件，地址 + 空格 + 数据 + 回车
        fp.write(addr_hex_8bit + ' ' + data_read_hex + '\n')
        count += 1

print('执行完毕')





