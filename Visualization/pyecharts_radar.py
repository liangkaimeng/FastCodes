# -*- coding: utf-8 -*-
# Author: lkm
# date: 2023/6/16 17:25

from pyecharts import options as opts
from pyecharts.charts import Radar

# 数据
categories = ['输出', 'KDA', '发育', '团战', '生存']
values = [[4, 3, 5, 2, 4]]  # 注意数据是二维列表，支持多组数据

# 创建雷达图实例
radar = (
    Radar()
    .add_schema(schema=[opts.RadarIndicatorItem(name='输出', max_=10, color='black'),
                        opts.RadarIndicatorItem(name='KDA', max_=10, color='black'),
                        opts.RadarIndicatorItem(name='发育', max_=5, color='black'),
                        opts.RadarIndicatorItem(name='团战', max_=5, color='black'),
                        opts.RadarIndicatorItem(name='生存', max_=5, color='black')],
                splitline_opt=opts.SplitLineOpts(is_show=True,
                                                 linestyle_opts=opts.LineStyleOpts(width=2)))
    .add("数据", values, color="cyan", areastyle_opts=True, label_opts=True)
    .set_series_opts(label_opts=opts.LabelOpts(is_show=False), markline_opts=True, effect_opts=True)
    .set_global_opts(title_opts=opts.TitleOpts(title="雷达图"))
)

# 渲染图表到HTML文件中
radar.render("radar_chart.html")
