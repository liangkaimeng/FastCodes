# -*- coding: utf-8 -*-
# Author: lkm
# date: 2023/6/16 17:35

from pyecharts.charts import Funnel
from pyecharts import options as opts

# 创建漏斗图对象
funnel = Funnel()

# 设置漏斗图的数据和配置项
data = [("步骤1", 100),
        ("步骤2", 80),
        ("步骤3", 60),
        ("步骤4", 40),
        ("步骤5", 20)]

funnel.add("漏斗图", data,
           label_opts=opts.LabelOpts(formatter="{c}%"))

# 设置全局配置项
funnel.set_global_opts(title_opts=opts.TitleOpts(title="漏斗图示例"))

# 渲染生成HTML文件
funnel.render("funnel_chart.html")
# 在Jupyter Notebook中显示图表
funnel.render_notebook()
