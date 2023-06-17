# -*- coding: utf-8 -*-
# Author: lkm
# date: 2023/6/18 1:21

from pyecharts import options as opts
from pyecharts.charts import Gauge

# 创建仪表盘图
gauge = (
    Gauge()
    .add("", [("指标名称", 60)])  # 指标名称和初始值
    .set_global_opts(title_opts=opts.TitleOpts(title="仪表盘示例"))
)

# 渲染生成HTML文件（可选）
gauge.render("gauge.html")
gauge.render_notebook()
