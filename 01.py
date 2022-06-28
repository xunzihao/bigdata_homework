from calendar import c
from collections import Counter
import pandas as pd
import requests
from lxml import etree
import pyecharts.options as opts
from pyecharts.charts import Line
from pyecharts.commons.utils import JsCode
import matplotlib.pyplot as plt
# 获取json并读取
# url = "https://pvp.qq.com/zlkdatasys/data_zlk_xpflby.json"
# response_original = requests.get(url).json()
# 拿数据 url_list用于获取皮肤名和英雄名
# url_list = []
# skin_hero_name_list = []
# skin_release_date_list = []
#
# for i in response_original['pcblzlby_c6']:
#     url = i['pcblzlbyxqydz_c4']
#     image_url = "https:" + url
#     url_list.append(image_url)
#     skin_release_date = i['lbyrq_e5']
#     skin_release_date_list.append(skin_release_date)
#     skin_release_date = pd.DataFrame(skin_release_date_list, columns=['发布日期'])
# skin_release_date.to_excel('发布时间.xlsx')
#
# for j in range(len(url_list)):
#     response = requests.get(url_list[j])
#     response.encoding = 'gbk'
#     text = response.text
#     selector = etree.HTML(text)
#     skin_hero_name = selector.xpath('//*[@id="showSkin"]/div/div/span/text()')
#     skin_hero_name_list.append(skin_hero_name)
#     skin_hero_name = pd.DataFrame(data=skin_hero_name_list, columns=['皮肤名', '英雄名'])
# skin_hero_name.to_excel('skin_hero_name.xlsx')

# f1 = pd.read_excel('skin_hero_name.xlsx')
# f2 = pd.read_excel('发布时间.xlsx')
# all = pd.concat([f1, f2], axis=1)
# all.drop(all.columns[[0, 3]], axis=1, inplace=True)
# all.to_excel('all.xlsx')

# ---------------------------------------------------以上不改动
# 分析每月发布的皮肤数量（为绘图库提供数据）
all = pd.read_excel('all copy.xlsx')  # 读取文件
time = all["发布日期"].tolist()  # 形成列表
clear_time = [str(i)[0:6] for i in time]  # 提取年月
result = Counter(clear_time)  # 统计
d = sorted(result.items(), key=lambda x: x[0], reverse=False)  # 按照年月排序
x = [i[0] for i in d]  # 年月（x轴）
y = [i[1] for i in d]  # 皮肤数量（y轴）

plt.figure(figsize=(30,7))
# for i in range(len(x)):
plt.bar(x,y)
plt.rcParams['font.sans-serif']=['Arial Unicode MS']#设置中文字体
plt.rcParams['axes.unicode_minus']=False#设置负号正常显示
plt.title('2017-03至2022-06英雄皮肤分布')
plt.xlabel("英雄名")
# plt.xticks(fontproperties = 'Times New Roman', size = 15)
plt.ylabel("数量")
plt.show()
# # 分析每个英雄发布的皮肤数量（为绘图库提供数据）
# all = pd.read_excel('all copy.xlsx')  # 读取文件
# hero_name = all["英雄名"].tolist()  # 形成列表
# result = Counter(hero_name)  # 统计
# print(result)
# d = result.items()  # key=lambda x: x[0], reverse=False)#按照年月排序
# x2 = [i[0] for i in d]  # 英雄名（x轴）
# y2 = [i[1] for i in d]  # 皮肤数量（y轴）
# # pd.DataFrame(x2,columns=["英雄名"]).to_excel("英雄名.xlsx")
# # pd.DataFrame(y2,columns=["每名英雄发布的皮肤数量"]).to_excel("每名英雄发布的皮肤数量.xlsx")
# a1=pd.read_excel("英雄名.xlsx")#将英雄名单独输出
# a2=pd.read_excel("每名英雄发布的皮肤数量.xlsx")#将每名英雄发布的皮肤数量单独输出
# a3=pd.concat([a1,a2],axis=1)#上述两个文件合并
# a3.drop(a3.columns[[0,2]],axis=1,inplace=True)#去除不必要的列
# a3.to_excel("a3.xlsx")#保存 以备后用

# import pyecharts.options as opts
# from pyecharts.charts import Line
# from pyecharts.commons.utils import JsCode
# # 绘制每月发布的皮肤数量图
# js_formatter = """function (params) {
#         return params.seriesData[0].data;
#     }"""

# (
#     Line(init_opts=opts.InitOpts(width="1600px", height="800px"))
#     .add_xaxis(
#         xaxis_data=x1,

#     )
#     .add_yaxis(
#         series_name="每个月发布的皮肤数量",
#         is_smooth=True,
#         symbol="emptyCircle",
#         is_symbol_show=True,
#         color="#d14a61",
#         y_axis=y1,
#         label_opts=opts.LabelOpts(is_show=True),
#         linestyle_opts=opts.LineStyleOpts(width=2),
#     )
#     .set_global_opts(
#         legend_opts=opts.LegendOpts(),
#         tooltip_opts=opts.TooltipOpts(trigger="none", axis_pointer_type="cross"),
#         xaxis_opts=opts.AxisOpts(
#             type_="category",
#             axistick_opts=opts.AxisTickOpts(is_align_with_label=True),
#             axisline_opts=opts.AxisLineOpts(
#                 is_on_zero=True, linestyle_opts=opts.LineStyleOpts(color="#d14a61")
#             ),
#             axispointer_opts=opts.AxisPointerOpts(
#                 is_show=True, label=opts.LabelOpts(formatter=JsCode(js_formatter))
#             ),
#         ),
#         yaxis_opts=opts.AxisOpts(
#             type_="value",
#             splitline_opts=opts.SplitLineOpts(
#                 is_show=True, linestyle_opts=opts.LineStyleOpts(opacity=1)
#             ),
#         ),
#     )
#     .render_notebook()
# )

# # # # 绘制每个英雄发布的皮肤数量图
# # #
# # #
# # # js_formatter = """function (params) {
# # #         return params.seriesData[0].data;
# # #     }"""
# # #
# # # (
# # #     Line(init_opts=opts.InitOpts(width="1600px", height="800px"))
# # #     .add_xaxis(
# # #         xaxis_data=x2,
# # #
# # #     )
# # #     .add_yaxis(
# # #         series_name="每个英雄出的皮肤数量",
# # #         is_smooth=True,
# # #         symbol="emptyCircle",
# # #         is_symbol_show=True,
# # #         color="#d14a61",
# # #         y_axis=y2,
# # #         label_opts=opts.LabelOpts(is_show=True),
# # #         linestyle_opts=opts.LineStyleOpts(width=2),
# # #     )
# # #     .set_global_opts(
# # #         legend_opts=opts.LegendOpts(),
# # #         tooltip_opts=opts.TooltipOpts(trigger="none", axis_pointer_type="cross"),
# # #         xaxis_opts=opts.AxisOpts(
# # #             type_="category",
# # #             axistick_opts=opts.AxisTickOpts(is_align_with_label=True),
# # #             axisline_opts=opts.AxisLineOpts(
# # #                 is_on_zero=True, linestyle_opts=opts.LineStyleOpts(color="#d14a61")
# # #             ),
# # #             axispointer_opts=opts.AxisPointerOpts(
# # #                 is_show=True, label=opts.LabelOpts(formatter=JsCode(js_formatter))
# # #             ),
# # #         ),
# # #         yaxis_opts=opts.AxisOpts(
# # #             type_="value",
# # #             splitline_opts=opts.SplitLineOpts(
# # #                 is_show=True, linestyle_opts=opts.LineStyleOpts(opacity=1)
# # #             ),
# # #         ),
# # #     )
# # #     .render("每个英雄发布的皮肤数量图.html")
# # # )
# #
# #
# #
# #
# # from pyecharts.charts import Sunburst
# # from pyecharts import options as opts
# #
# # data = [
# #     {
# #         "name": "Flora",
# #         "itemStyle": {"color": "#da0d68"},
# #         "children": [
# #             {"name": "Black Tea", "value": 1, "itemStyle": {"color": "#975e6d"}},
# #             {
# #                 "name": "Floral","value":3,
# #                 "itemStyle": {"color": "#e0719c"},
# #             },
# #         ],
# #     },
# #     {
# #         "name": "Fruity",
# #         "itemStyle": {"color": "#da1d23"},
# #         "children": [
# #             {
# #                 "name": "Berry","value":4,
# #                 "itemStyle": {"color": "#dd4c51"},
# #
# #             },
# #             {
# #                 "name": "Dried Fruit","value":2,
# #                 "itemStyle": {"color": "#c94a44"},
# #             },
# #             {
# #                 "name": "Other Fruit","value": 8,
# #                 "itemStyle": {"color": "#dd4c51"},
# #
# #             },
# #             {
# #                 "name": "Citrus Fruit","value": 4,
# #                 "itemStyle": {"color": "#f7a128"},
# #             },
# #         ],
# #     },
# #     {
# #         "name": "Sour/\nFermented",
# #         "itemStyle": {"color": "#ebb40f"},
# #         "children": [
# #             {
# #                 "name": "Sour","value":6,
# #                 "itemStyle": {"color": "#e1c315"},
# #             },
# #             {
# #                 "name": "Alcohol/\nFremented","value":4,
# #                 "itemStyle": {"color": "#b09733"},
# #             },
# #         ],
# #     },
# #     {
# #         "name": "Green/\nVegetative",
# #         "itemStyle": {"color": "#187a2f"},
# #         "children": [
# #             {"name": "Olive Oil", "value": 1, "itemStyle": {"color": "#a2b029"}},
# #             {"name": "Raw", "value": 1, "itemStyle": {"color": "#718933"}},
# #             {
# #                 "name": "Green/\nVegetative","value":7,
# #                 "itemStyle": {"color": "#3aa255"},
# #             },
# #             {"name": "Beany", "value": 1, "itemStyle": {"color": "#5e9a80"}},
# #         ],
# #     },
# #     {
# #         "name": "Other",
# #         "itemStyle": {"color": "#0aa3b5"},
# #         "children": [
# #             {
# #                 "name": "Papery/Musty","value":10,
# #                 "itemStyle": {"color": "#9db2b7"},
# #             },
# #             {
# #                 "name": "Chemical","value":6,
# #                 "itemStyle": {"color": "#76c0cb"},
# #             },
# #         ],
# #     },
# #     {
# #         "name": "Roasted",
# #         "itemStyle": {"color": "#c94930"},
# #         "children": [
# #             {"name": "Pipe Tobacco", "value": 1, "itemStyle": {"color": "#caa465"}},
# #             {"name": "Tobacco", "value": 1, "itemStyle": {"color": "#dfbd7e"}},
# #             {
# #                 "name": "Burnt","value":4,
# #                 "itemStyle": {"color": "#be8663"},
# #             },
# #             {
# #                 "name": "Cereal","value":2,
# #                 "itemStyle": {"color": "#ddaf61"},
# #             },
# #         ],
# #     },
# #     {
# #         "name": "Spices",
# #         "itemStyle": {"color": "#ad213e"},
# #         "children": [
# #             {"name": "Pungent", "value": 1, "itemStyle": {"color": "#794752"}},
# #             {"name": "Pepper", "value": 1, "itemStyle": {"color": "#cc3d41"}},
# #             {
# #                 "name": "Brown Spice","value":4,
# #                 "itemStyle": {"color": "#b14d57"},
# #             },
# #         ],
# #     },
# #     {
# #         "name": "Nutty/\nCocoa",
# #         "itemStyle": {"color": "#a87b64"},
# #         "children": [
# #             {
# #                 "name": "Nutty","value":3,
# #                 "itemStyle": {"color": "#c78869"},
# #             },
# #             {
# #                 "name": "Cocoa","value":2,
# #                 "itemStyle": {"color": "#bb764c"},
# #             },
# #         ],
# #     },
# #     {
# #         "name": "Sweet",
# #         "itemStyle": {"color": "#e65832"},
# #         "children": [
# #             {
# #                 "name": "Brown Sugar","value":4,
# #                 "itemStyle": {"color": "#d45a59"},
# #             },
# #             {"name": "Vanilla", "value": 1, "itemStyle": {"color": "#f89a80"}},
# #             {"name": "Vanillin", "value": 1, "itemStyle": {"color": "#f37674"}},
# #             {"name": "Overall Sweet", "value": 1, "itemStyle": {"color": "#e75b68"}},
# #             {"name": "Sweet Aromatics", "value": 1, "itemStyle": {"color": "#d0545f"}},
# #         ],
# #     },
# # ]
# #
# # c = (
# #     Sunburst(init_opts=opts.InitOpts(width="1000px", height="600px"))
# #     .add(
# #         "",
# #         data_pair=data,
# #         highlight_policy="ancestor",
# #         radius=[0, "95%"],
# #         sort_="null",
# #         levels=[
# #             {},
# #             {
# #                 "r0": "15%",
# #                 "r": "35%",
# #                 "itemStyle": {"borderWidth": 2},
# #                 "label": {"rotate": "tangential"},
# #             },
# #             {"r0": "35%", "r": "70%", "label": {"align": "right"}},
# #             {
# #                 "r0": "70%",
# #                 "r": "72%",
# #                 "label": {"position": "outside", "padding": 3, "silent": False},
# #                 "itemStyle": {"borderWidth": 3},
# #             },
# #         ],
# #     )
# #     .set_global_opts(title_opts=opts.TitleOpts(title="Sunburst-官方示例"))
# #     .set_series_opts(label_opts=opts.LabelOpts(formatter="{b}"))
# #     .render("00001.html")
# # )
