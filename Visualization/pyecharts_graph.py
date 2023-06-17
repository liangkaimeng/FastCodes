# -*- coding: utf-8 -*-
# Author: lkm
# date: 2023/6/18 1:15

from pyecharts import options as opts
from pyecharts.charts import Graph

# 创建节点和边的数据
nodes = [
    {"name": "节点1", "symbolSize": 50},
    {"name": "节点2", "symbolSize": 30},
    {"name": "节点3", "symbolSize": 40},
    {"name": "节点4", "symbolSize": 35},
    {"name": "节点5", "symbolSize": 25},
]
links = [
    {"source": "节点1", "target": "节点2"},
    {"source": "节点1", "target": "节点3"},
    {"source": "节点2", "target": "节点3"},
    {"source": "节点4", "target": "节点5"},
]

# 创建关系图
graph = (
    Graph()
    .add("", nodes, links, repulsion=8000)
    .set_global_opts(title_opts=opts.TitleOpts(title="关系图示例"))
)

# 渲染生成HTML文件（可选）
graph.render("graph.html")
graph.render_notebook()
