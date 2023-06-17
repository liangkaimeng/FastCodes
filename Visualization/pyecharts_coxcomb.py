# -*- coding: utf-8 -*-
# Author: lkm
# date: 2023/6/18 1:12

from pyecharts import options as opts
from pyecharts.charts import Pie

# 构造数据
data = [("类别1", 55), ("类别2", 78), ("类别3", 92), ("类别4", 65), ("类别5", 80)]

# 创建Pie实例
pie = (
    Pie()
    .add(
        series_name="南丁格尔玫瑰图",
        data_pair=data,
        radius=["30%", "75%"],
        rosetype="radius",
        label_opts=opts.LabelOpts(is_show=True, position="inside", formatter="{b}: {d}%"),  # 显示标签，并设置位置和格式
    )
    .set_global_opts(
        title_opts=opts.TitleOpts(title="南丁格尔玫瑰图"),
        legend_opts=opts.LegendOpts(orient="vertical", pos_top="15%", pos_left="2%"),
    )
)

# 渲染生成HTML文件（可选）
pie.render("rose_chart.html")
pie.render_notebook()
