# -*- coding: utf-8 -*-
# Author: lkm
# date: 2023/6/18 1:17

from pyecharts import options as opts
from pyecharts.charts import Tree

# 创建树图的数据
data = [
    {
        "name": "节点1",
        "children": [
            {"name": "节点1.1"},
            {"name": "节点1.2"},
            {
                "name": "节点1.3",
                "children": [
                    {"name": "节点1.3.1"},
                    {"name": "节点1.3.2"},
                ],
            },
        ],
    },
    {
        "name": "节点2",
        "children": [
            {"name": "节点2.1"},
            {"name": "节点2.2"},
        ],
    },
]

# 创建树图
tree = (
    Tree()
    .add("", data, collapse_interval=2, orient="TB")
    .set_global_opts(title_opts=opts.TitleOpts(title="树图示例"))
)

# 渲染生成HTML文件（可选）
tree.render("tree.html")
tree.render_notebook()
