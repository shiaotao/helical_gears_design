'''
Author: error: git config user.name && git config user.email & please set dead value or install git
Date: 2022-08-25 10:15:15
LastEditors: error: git config user.name && git config user.email & please set dead value or install git
LastEditTime: 2022-08-28 19:08:36
FilePath: \Python语言程序设计\机械设计与校核\standard_helical_ gears.py
Description: 这是默认设置,请设置`customMade`, 打开koroFileHeader查看配置 进行设置: https://github.com/OBKoro1/koro1FileHeader/wiki/%E9%85%8D%E7%BD%AE
'''
'''
standard_helical_ gears.py
标准斜齿圆柱齿轮的设计
'''
import math

#% 变量输入

T1_Nmm = 270.83877e3
"#*     输入功率(N•mm)"
n1_rpm = 86.7924528
"#*     小齿轮转速(rpm)"
z1 = 22
z2 = 70
#* ↑    初选小齿轮齿数、大齿轮齿数
Φd = 1
"#*     齿宽系数(-)由表10-8选取"
σH1_MPa = 600
"#*     小齿轮接触疲劳极限(MPa)"
σH2_MPa = 550
"#*     大齿轮接触疲劳极限(MPa)"
KHN1 = 0.95
"#*     小齿轮接触疲劳寿命系数"
KHN2 = 0.98
"#*     大齿轮接触疲劳寿命系数"
ZE = 189.8
"#*     弹性影响系数(1)表10-6"
#? KHβ = 1.358
#?     齿向载荷分布系数(1)表10-4
σF1_MPa = 500
"#*     小齿轮弯曲疲劳极限(MPa)"
σF2_MPa = 350
"#*     大齿轮弯曲触疲劳极限(MPa)"
KFN1 = 0.92
"#*     小齿轮弯曲疲劳寿命系数"
KFN2 = 0.95
"#*     大齿轮弯曲疲劳寿命系数"

#% 标准值、推荐值

KHt = 1.2
"#*     初选载荷系数(-)"
KA = 1
"#*     使用系数(1)"
β_deg = 14
#* ↑    初选螺旋角(°)
α_deg = 20
#* ↑    压力角，取标准值20°
han_ = 1
"#*     法面齿顶高系数han*(-)"
cn_ = 0.25
"#*     法面顶隙系数cn*(-)"
Sf = 1
"#*     接触许用应力安全系数(1)"
Sf_ = 1.4
"#*     弯曲许用应力安全系数(1)"
pi = math.pi
"#*     由math.pi得到的圆周率(1)"

'''
按齿面接触疲劳强度设计
'''
print('{:^16} {:^7} {:^7}'.format('RESULTS', 'NAME', 'VALUE'))
print('{:—^15} {:-^7} {:-^7}'.format('', '', ''))

#% 1.计算区域系数ZH

an_rad = math.radians(α_deg)
#* ↑    conversion result: 法面压力角(rad)
b_rad = math.radians(β_deg)
"#*     conversion result: 初选螺旋角(rad)"
at_rad = math.atan(math.tan(an_rad)/math.cos(b_rad))
#* ↑    calculation result: 端面压力角(rad)
at_deg = math.degrees(at_rad)
#* ↑    conversion result: 端面压力角(°)
print('{:　^8} {:^7} {:.4f}'.format('端面压力角', 'αt(°)', at_deg))
print('{:—^15} {:-^7} {:-^7}'.format('', '', ''))

betab_rad = math.atan(math.tan(b_rad)*math.cos(at_rad))
"#*     calculation result: 基圆螺旋角βb(rad)"
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
"#*     calculation result: 试算小齿轮分度圆直径最小值(mm)"
print('{:　^8} {:^7} {:.4f}'.format('试算小分度圆', 'dt1(mm)', dt1_mm_))
print('{:—^15} {:-^7} {:-^7}'.format('', '', ''))

#% 6.计算实际载荷系数KH

v_mps = pi*dt1_mm_*n1_rpm/60000
#* ↑    calculation result: 小齿轮圆周速度(m/s)
print('{:　^8} {:^7} {:.4f}'.format('≈小圆周速度', 'v(m/s)', v_mps))
Kv = eval(input('Typing: 图10-8动载系数Kv = '))
print('{:—^15} {:-^7} {:-^7}'.format('', '', ''))
#* ↑    input value: 动载系数(1)

b_mm_ = Φd*dt1_mm_
"#*     calculation result: 试算小齿轮齿宽b'(mm)"
print('{:　^8} {:^7} {:.4f}'.format('≈小齿轮齿宽', 'b(mm)', b_mm_))
KHb = eval(input('Typing: 表10-4齿向载荷分布系数Kʜβ = '))
"#*     input value: 齿向载荷分布系数Kʜβ(1)"
print('{:—^15} {:-^7} {:-^7}'.format('', '', ''))

Ft1_N_ = 2*T1_Nmm/dt1_mm_
#* ↑    calculation result: 齿轮圆周力(N)
print('{:　^8} {:^7} {:.4f}'.format('≈齿轮圆周力', 'Ft1(N)', Ft1_N_))
print('{:-^15} {:-^7} {:-^7}'.format('', '', ''))
KAFt1b_Npmm_ = KA*Ft1_N_/b_mm_
#* ↑    calculation result:
print('{:　^8} {:^7} {:.4f}'.format('KA*Ft1/b (N/mm)', '', KAFt1b_Npmm_))
KHa = eval(input('Typing: 表10-3齿间载荷分配系数Kʜα = '))
#* ↑    input value: 齿间载荷分配系数(1)
print('{:—^15} {:-^7} {:-^7}'.format('', '', ''))

KH = KA*Kv*KHa*KHb
"#* ↑    calculation result: 载荷系数Kʜ(1)"
print('{:　^8} {:^7} {:.4f}'.format('载荷系数', 'Kʜ(1)', KH))
print('{:—^15} {:-^7} {:-^7}'.format('', '', ''))

#% 7.修正分度圆直径和模数

d1_mm = dt1_mm_*math.pow(KH/KHt, 1/3)
"#*     calculation result: 修正小分度圆直径d1(mm)"
print('{:　^8} {:^7} {:.4f}'.format('分度圆直径', 'd1(mm)', d1_mm))
print('{:—^15} {:-^7} {:-^7}'.format('', '', ''))
m_mm = d1_mm*math.cos(b_rad)/z1
"#*     calculation result: 修正模数m(mm)"
print('{:　^8} {:^7} {:.4f}'.format('模数', 'm(mm)', m_mm))
print('{:—^15} {:-^7} {:-^7}'.format('', '', ''))

'''
按齿根弯曲疲劳强度校核
'''
print('{:^16} {:^7} {:^7}'.format('RESULTS', 'NAME', 'VALUE'))
print('{:—^15} {:-^7} {:-^7}'.format('', '', ''))

#% 8.计算齿根弯曲疲劳强度计算用载荷系数Kғ

u_mps = pi*d1_mm*n1_rpm/60000
"#*     calculation result: 校核用设计圆周速度u(m/s)"
print('{:　^8} {:^7} {:.4f}'.format('校核小圆周速度', 'u(m/s)', u_mps))
Ku = eval(input('Typing: 图10-8动载系数Ku = '))
"#*     input value: 校核用动载系数(1)"
print('{:—^15} {:-^7} {:-^7}'.format('', '', ''))

b_mm = Φd*d1_mm
"#*     calculation result: 修正小齿轮齿宽(mm)"
print('{:　^8} {:^7} {:.4f}'.format('小齿轮齿宽', 'b(mm)', b_mm))
print('{:—^15} {:-^7} {:-^7}'.format('', '', ''))
KAFt1b_Npmm = KA*(2*T1_Nmm/d1_mm)/b_mm
#* ↑    calculation result:
print('{:　^8} {:^7} {:.4f}'.format('KA*Ft1/b (N/mm)', '', KAFt1b_Npmm))
KFa = eval(input('Typing: 表10-3齿间载荷分配系数Kғα = '))
"#*     input value: 齿根弯曲疲劳强度校核用齿间载荷分配系数Kғα(1)"
print('{:—^15} {:-^7} {:-^7}'.format('', '', ''))

h_mm = (2*han_+cn_)*m_mm
"#*     calculation result: 齿全高h(mm)"
bph = b_mm/h_mm
"#*     calculation result: 宽高比b/h(1)"
print('{:　^8} {:^7} {:.4f}'.format('b/h', '', bph))
KFb = eval(input('Typing: 图10-13齿向载荷分布系数Kғβ = '))
"#*     input value: 齿根弯曲疲劳强度校核用齿向载荷分布系数Kғβ(1)"
print('{:—^15} {:-^7} {:-^7}'.format('', '', ''))

KF = KA*Ku*KFa*KFb
"#*     calculation result: 齿根弯曲疲劳强度计算用载荷系数Kғ(1)"
print('{:　^8} {:^7} {:.4f}'.format('弯曲载荷系数', 'Kғ(1)', KF))
print('{:—^15} {:-^7} {:-^7}'.format('', '', ''))

#% 9.计算弯曲重合度系数Yε和弯曲螺旋角系数Yβ

Ealphav = Ealpha/math.pow(math.cos(betab_rad), 2)
"#*     calculation result:"
Yepsilon = 0.25+0.75/Ealphav
"#*     calculation result: 弯曲重合度系数Yε(1)"
print('{:　^8} {:^7} {:.4f}'.format('弯曲重合度系数', 'Yε(1)', Yepsilon))
print('{:—^15} {:-^7} {:-^7}'.format('', '', ''))

Ybeta = 1-Ebeta*β_deg/120
"#*     calculation result: 弯曲螺旋角系数Yβ"
print('{:　^8} {:^7} {:.4f}'.format('弯曲螺旋角度系数', 'Yβ(1)', Ybeta))
print('{:—^15} {:-^7} {:-^7}'.format('', '', ''))

#% 10.计算弯曲许用应力[σғ]

sigmaF1_MPa = KFN1*σF1_MPa/Sf_
"#*     calculation result: 小齿轮弯曲疲劳强度许用应力[σғ]₁(MPa)"
sigmaF2_MPa = KFN2*σF2_MPa/Sf_
"#*     calculation result: 大齿轮弯曲疲劳强度许用应力[σғ]₂(MPa)"
print('{:　^8} {:^7} {:.4f}'.format('', '[σғ]₁(MPa)', sigmaF1_MPa))
print('{:　^8} {:^7} {:.4f}'.format('', '[σғ]₂(MPa)', sigmaF2_MPa))
print('{:—^15} {:-^7} {:-^7}'.format('', '', ''))

#% 11.引入齿形系数Yғa和应力修正系数Ysa

zv1 = z1/math.pow(math.cos(b_rad), 3)
"#*     calculation result: 小齿轮当量齿数zv1(1)"
print('{:　^8} {:^7} {:.4f}'.format('小齿轮当量齿数', 'zv₁(1)', zv1))
YFa1 = eval(input('Typing: 表10-5小齿轮齿形系数Yғa₁ = '))
"#*     input value: 小齿轮齿形系数Yғa₁(1)"
YSa1 = eval(input('Typing: 小齿轮应力修正系数Ysa₁ = '))
"#*     input value: 小齿轮应力修正系数Ysa₁(1)"
print('{:-^15} {:-^7} {:-^7}'.format('', '', ''))
zv2 = z2/math.pow(math.cos(b_rad), 3)
"#*     calculation result: 大齿轮当量齿数zv2(1)"
print('{:　^8} {:^7} {:.4f}'.format('大齿轮当量齿数', 'zv₂(1)', zv2))
YFa2 = eval(input('Typing: 表10-5大齿轮齿形系数Yғa₂ = '))
"#*     input value: 大齿轮齿形系数Yғa₂(1)"
YSa2 = eval(input('Typing: 大齿轮应力修正系数Ysa₂ = '))
"#*     input value: 大齿轮应力修正系数Ysa₂(1)"
print('{:—^15} {:-^7} {:-^7}'.format('', '', ''))

YFa1YSa1 = YFa1*YSa1/sigmaF1_MPa
YFa2YSa2 = YFa2*YSa2/sigmaF2_MPa
#* ↑    calculation result:
print('{:　^8} {:^7} {:.4f}'.format('', 'Yғa*Ysa/[σғ]1', YFa1YSa1))
print('{:　^8} {:^7} {:.4f}'.format('', 'Yғa*Ysa/[σғ]2', YFa2YSa2))
print('{:—^15} {:-^7} {:-^7}'.format('', '', ''))
YFaYSa = max(YFa1YSa1, YFa2YSa2)
"#*     calculation result: 代数式Yғa*Ysa/[σғ]值(1)"

#% 12.校核齿轮模数

m_mm_ = math.pow(2*KF*T1_Nmm*Yepsilon*Ybeta*math.pow(math.cos(b_rad)/z1, 2)*YFaYSa/Φd, 1/3)
"#*     calculation result: 校核模数的最小值(mm)"
print('{:　^8} {:^7} {:.4f}'.format('校核模数', 'm\'(mm)', m_mm_))
print('{:—^15} {:-^7} {:-^7}'.format('', '', ''))

print('Info: Completed!')

'''ᴀ ʙ ᴄ ᴅ ᴇ ғ ɢ ʜ ɪ ᴊ ᴋ ʟ ᴍ ɴ o ᴘ ǫ ʀ s ᴛ ᴜ ᴠ ᴡ x ʏ ᴢ'''
