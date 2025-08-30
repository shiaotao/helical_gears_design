'''
Author: error: git config user.name && git config user.email & please set dead value or install git
Date: 2022-08-27 14:59:48
LastEditors: error: git config user.name && git config user.email & please set dead value or install git
LastEditTime: 2022-08-30 15:07:05
FilePath: \Python语言程序设计\机械设计与校核\main_dimensions_of_helical_gear.py
Description: 这是默认设置,请设置`customMade`, 打开koroFileHeader查看配置 进行设置: https://github.com/OBKoro1/koro1FileHeader/wiki/%E9%85%8D%E7%BD%AE
'''
import math

β_deg = 14
"#*     初选螺旋角(°)"
z1 = 28
z2 = 90
mn_mm = 2.5
"#*     标准模数mn(mm)"

print('{:^16} {:^7} {:^7}'.format('RESULTS', 'NAME', 'VALUE'))
print('{:-^15} {:-^7} {:-^7}'.format('', '', ''))

a_mm = (z1+z2)*mn_mm/(2*math.cos(math.radians(β_deg)))
"#*     理论中心距a(mm)"
print('{:　^8} {:^7} {:.4f}'.format('理论中心距', 'a(mm)', a_mm))
an_mm = eval(input('Typing: 调整中心距an = '))
"#*     调整中心距an(mm)"
print('{:-^15} {:-^7} {:-^7}'.format('', '', ''))

beta_rad = math.acos((z1+z2)*mn_mm/(2*an_mm))
print('{:　^8} {:^7} {:.4f}'.format('调整螺旋角', 'β(°)', math.degrees(beta_rad)))
print('{:-^15} {:-^7} {:-^7}'.format('', '', ''))

d1_mm = z1*mn_mm/math.cos(beta_rad)
print('{:　^8} {:^7} {:.4f}'.format('小分度圆', 'd₁(mm)', d1_mm))
d2_mm = z2*mn_mm/math.cos(beta_rad)
print('{:　^8} {:^7} {:.4f}'.format('大分度圆', 'd₂(mm)', d2_mm))
print('{:-^15} {:-^7} {:-^7}'.format('', '', ''))

print('Info: Completed!')
