'''
Author: error: git config user.name && git config user.email & please set dead value or install git
Date: 2022-08-25 10:15:15
LastEditors: error: git config user.name && git config user.email & please set dead value or install git
LastEditTime: 2022-08-25 16:14:46
FilePath: \Python语言程序设计\机械设计与校核\standard_helical_ gears.py
Description: 这是默认设置,请设置`customMade`, 打开koroFileHeader查看配置 进行设置: https://github.com/OBKoro1/koro1FileHeader/wiki/%E9%85%8D%E7%BD%AE
'''
'''
standard_helical_ gears.py
标准斜齿圆柱齿轮的设计
'''
import math

#% 变量输入

T1_Nmm = 6.119424e4
#* ↑    输入功率(N•mm)
n1_rpm = 400.0
#* ↑    小齿轮转速(rpm)
z1 = 23
z2 = 106
#* ↑    初选小齿轮齿数、大齿轮齿数
Φd = 1
#* ↑    齿宽系数(-)由表10-8选取


#% 标准值、推荐值

KHt = 1.2
#* ↑    初选载荷系数(-)
β_deg = 14
#* ↑    初选螺旋角(°)
α_deg = 20
#* ↑    压力角，取标准值20°
han_ = 1
#* ↑    法面齿顶高系数(-)
pi = math.pi
#* ↑    圆周率(-)

'''
按齿面接触疲劳强度设计
'''
print('{:^16} {:^7} {:^7}'.format('RESULTS', 'NAME', 'VALUE'))
print('{:—^15} {:-^7} {:-^7}'.format('', '', ''))

#% 1.计算区域系数ZH

an_rad = math.radians(α_deg)
#* ↑    conversion result: 法面压力角(rad)
b_rad = math.radians(β_deg)
#* ↑    conversion result: 初选螺旋角(rad)
at_rad = math.atan(math.tan(an_rad)/math.cos(b_rad))
#* ↑    calculation result: 端面压力角(rad)
at_deg = math.degrees(at_rad)
#* ↑    conversion result: 端面压力角(°)
print('{:　^8} {:^7} {:.4f}'.format('端面压力角', 'αt(°)', at_deg))
print('{:—^15} {:-^7} {:-^7}'.format('', '', ''))

betab_rad = math.atan(math.tan(b_rad)*math.cos(at_rad))
#* ↑    calculation result: 基圆螺旋角(rad)
betab_deg = math.degrees(betab_rad)
#* ↑    conversion result: 基圆螺旋角(°) 
print('{:　^8} {:^7} {:.4f}'.format('基圆螺旋角', 'βb(°)', betab_deg))
print('{:—^15} {:-^7} {:-^7}'.format('', '', ''))

ZH = math.sqrt(2*math.cos(betab_rad)/(math.cos(at_rad)*math.sin(at_rad)))
#* ↑    calculation result: 区域系数(-)
print('{:　^8} {:^7} {:.4f}'.format('区域系数', 'Zʜ(-)', ZH))
print('{:—^15} {:-^7} {:-^7}'.format('', '', ''))

#% 2.计算重合度系数Zε

aat1_rad = math.acos(z1*math.cos(at_rad)/(z1+2*han_*math.cos(b_rad)))
#* ↑    calculation result:
print('{:　^8} {:^7} {:.4f}'.format('', 'αat1(°)', math.degrees(aat1_rad)))
print('{:—^15} {:-^7} {:-^7}'.format('', '', ''))
aat2_rad = math.acos(z2*math.cos(at_rad)/(z2+2*han_*math.cos(b_rad)))
#* ↑    calculation result:
print('{:　^8} {:^7} {:.4f}'.format('', 'αat2(°)', math.degrees(aat2_rad)))
print('{:—^15} {:-^7} {:-^7}'.format('', '', ''))

Ealpha = (z1*(math.tan(aat1_rad)-math.tan(at_rad))+z2*(math.tan(aat2_rad)-math.tan(at_rad)))/(2*pi)
#* ↑    calculation result:
print('{:　^8} {:^7} {:.4f}'.format('', 'εα(-)', Ealpha))
print('{:—^15} {:-^7} {:-^7}'.format('', '', ''))

Ebeta = Φd*z1*math.tan(b_rad)/pi
print('{:　^8} {:^7} {:.4f}'.format('', 'εβ(-)', Ebeta))
print('{:—^15} {:-^7} {:-^7}'.format('', '', ''))

#Zepsilon = math.sqrt()

'''ᴀ ʙ ᴄ ᴅ ᴇ ғ ɢ ʜ ɪ ᴊ ᴋ ʟ ᴍ ɴ o ᴘ ǫ ʀ s ᴛ ᴜ ᴠ ᴡ x ʏ ᴢ'''
