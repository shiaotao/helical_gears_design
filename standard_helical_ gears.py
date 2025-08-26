'''
Author: error: git config user.name && git config user.email & please set dead value or install git
Date: 2022-08-25 10:15:15
LastEditors: error: git config user.name && git config user.email & please set dead value or install git
LastEditTime: 2022-08-26 22:42:44
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
'* ↑    输入功率(N•mm)'
n1_rpm = 400.0
#* ↑    小齿轮转速(rpm)
z1 = 23
z2 = 106
#* ↑    初选小齿轮齿数、大齿轮齿数
Φd = 1
#* ↑    齿宽系数(-)由表10-8选取
σH1_MPa = 600
σH2_MPa = 550
#* ↑    小齿轮接触疲劳极限、大齿轮
KHN1 = 0.91
KHN2 = 0.95
#* ↑    小齿轮接触疲劳寿命系数
ZE = 189.8
#* ↑    弹性影响系数(1)表10-6
KHβ = 1.358
#* ↑    齿向载荷分布系数(1)表10-4

#% 标准值、推荐值

KHt = 1.2
#* ↑    初选载荷系数(-)
KA = 1
#* ↑    使用系数(1)
β_deg = 14
#* ↑    初选螺旋角(°)
α_deg = 20
#* ↑    压力角，取标准值20°
han_ = 1
#* ↑    法面齿顶高系数(-)
Sf = 1
#* ↑    许用应力安全系数(1)
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
#* ↑    calculation result: 区域系数Zʜ(-)
print('{:　^8} {:^7} {:.4f}'.format('区域系数', 'Zʜ(-)', ZH))
print('{:—^15} {:-^7} {:-^7}'.format('', '', ''))

#% 2.计算重合度系数Zε

aat1_rad = math.acos(z1*math.cos(at_rad)/(z1+2*han_*math.cos(b_rad)))
#* ↑    calculation result:
print('{:　^8} {:^7} {:.4f}'.format('', 'αat1(°)', math.degrees(aat1_rad)))
print('{:-^15} {:-^7} {:-^7}'.format('', '', ''))
aat2_rad = math.acos(z2*math.cos(at_rad)/(z2+2*han_*math.cos(b_rad)))
#* ↑    calculation result:
print('{:　^8} {:^7} {:.4f}'.format('', 'αat2(°)', math.degrees(aat2_rad)))
print('{:—^15} {:-^7} {:-^7}'.format('', '', ''))

Ealpha = (z1*(math.tan(aat1_rad)-math.tan(at_rad))+z2*(math.tan(aat2_rad)-math.tan(at_rad)))/(2*pi)
#* ↑    calculation result:
print('{:　^8} {:^7} {:.4f}'.format('', 'εα(-)', Ealpha))
print('{:-^15} {:-^7} {:-^7}'.format('', '', ''))

Ebeta = Φd*z1*math.tan(b_rad)/pi
#* ↑    calculation result:
print('{:　^8} {:^7} {:.4f}'.format('', 'εβ(-)', Ebeta))
print('{:—^15} {:-^7} {:-^7}'.format('', '', ''))

Zepsilon = math.sqrt((4-Ealpha)*(1-Ebeta)/3+(Ebeta/Ealpha))
#* ↑    calculation result: 重合度系数Zε(-)
print('{:　^8} {:^7} {:.4f}'.format('重合度系数', 'Zε(-)', Zepsilon))
print('{:—^15} {:-^7} {:-^7}'.format('', '', ''))

#% 3.计算螺旋角系数Zβ

Zbeta = math.sqrt(math.cos(b_rad))
#* ↑    calculation result: 螺旋角系数Zβ(-)
print('{:　^8} {:^7} {:.4f}'.format('螺旋角系数', 'Zβ(-)', Zbeta))
print('{:—^15} {:-^7} {:-^7}'.format('', '', ''))

#% 4.计算接触疲劳强度许用应力[σʜ]

sigmaH1_MPa = KHN1*σH1_MPa/Sf
sigmaH2_MPa = KHN2*σH2_MPa/Sf
#* ↑    calculation result: 小齿轮、大齿轮接触疲劳强度许用应力(MPa)
print('{:　^8} {:^7} {:.4f}'.format('', '[σʜ]1(MPa)', sigmaH1_MPa))
print('{:　^8} {:^7} {:.4f}'.format('', '[σʜ]2(MPa)', sigmaH2_MPa))
print('{:—^15} {:-^7} {:-^7}'.format('', '', ''))
SigmaH_MPa = min(sigmaH1_MPa, sigmaH2_MPa)
#* ↑    calculation result: 取小接触疲劳强度作为许用应力(MPa)
print('{:　^8} {:^7} {:.4f}'.format('接触疲劳强度', '[σʜ](MPa)', SigmaH_MPa))
print('{:—^15} {:-^7} {:-^7}'.format('', '', ''))

#% 5.试算小齿轮分度圆直径dt1

dt1_mm_ = math.pow((2*KHt*T1_Nmm/Φd)*(1+z1/z2)*math.pow(ZH*ZE*Zepsilon*Zbeta/SigmaH_MPa, 2), 1/3)
#* ↑    calculation result: 小齿轮分度圆直径最小值(mm)
print('{:　^8} {:^7} {:.4f}'.format('试算小分度圆', 'dt1(mm)', dt1_mm_))
print('{:—^15} {:-^7} {:-^7}'.format('', '', ''))

#% 6.计算实际载荷系数KH

v_mps = pi*dt1_mm_*n1_rpm/60000
#* ↑    calculation result: 小齿轮圆周速度(m/s)
print('{:　^8} {:^7} {:.4f}'.format('≈小圆周速度', 'v(m/s)', v_mps))
Kv = eval(input('Typing: 动载系数Kv = '))
print('{:—^15} {:-^7} {:-^7}'.format('', '', ''))
#* ↑    input value: 动载系数(1)

b_mm = Φd*dt1_mm_
#* ↑    calculation result: 小齿轮齿宽(mm)
print('{:　^8} {:^7} {:.4f}'.format('≈小齿轮齿宽', 'b(mm)', b_mm))
print('{:—^15} {:-^7} {:-^7}'.format('', '', ''))

Ft1_N = 2*T1_Nmm/dt1_mm_
#* ↑    calculation result: 齿轮圆周力(N)
print('{:　^8} {:^7} {:.4f}'.format('≈齿轮圆周力', 'Ft1(N)', Ft1_N))
print('{:-^15} {:-^7} {:-^7}'.format('', '', ''))
KAFt1b_Npmm = KA*Ft1_N/b_mm
#* ↑    calculation result:
print('{:　^8} {:^7} {:.4f}'.format('KA*Ft1/b', '', KAFt1b_Npmm))
KHa = eval(input('Typing: 齿间载荷分配系数Kʜα = '))
#* ↑    input value: 齿间载荷分配系数(1)
print('{:—^15} {:-^7} {:-^7}'.format('', '', ''))

KH = KA*Kv*KHa*KHβ
#* ↑    calculation result: 载荷系数Kʜ(1)
print('{:　^8} {:^7} {:.4f}'.format('载荷系数', 'Kʜ(1)', KH))
print('{:—^15} {:-^7} {:-^7}'.format('', '', ''))

#% 7.修正分度圆直径和模数

d1_mm = dt1_mm_*math.pow(KH/KHt, 1/3)
print('{:　^8} {:^7} {:.4f}'.format('分度圆直径', 'd1(mm)', d1_mm))
print('{:—^15} {:-^7} {:-^7}'.format('', '', ''))
m_mm = d1_mm*math.cos(b_rad)/z1
print('{:　^8} {:^7} {:.4f}'.format('模数', 'm(mm)', m_mm))
print('{:—^15} {:-^7} {:-^7}'.format('', '', ''))


'''ᴀ ʙ ᴄ ᴅ ᴇ ғ ɢ ʜ ɪ ᴊ ᴋ ʟ ᴍ ɴ o ᴘ ǫ ʀ s ᴛ ᴜ ᴠ ᴡ x ʏ ᴢ'''
