# -*-* coding:UTF-8
import json


class OutputModule:

    def __init__(self, export_path, source_data):
        self.export_path = export_path
        self.source_data = source_data

    def export_json(self):
        """ 生成json文件 """
        with open(self.export_path, "w", encoding='utf-8') as f:
            json.dump(self.source_data, f, indent=4, ensure_ascii=False)

    def export_md(self):
        """ 生成md文件 """
        with open(self.export_path, "w", encoding='utf-8') as f:
            json.dump(self.source_data, f, indent=4, ensure_ascii=False)
#
#     @staticmethod
#     def export_html():
#         html_content = """
# <html>
# <head>
#     <meta http-equiv="Content-Type" content="text/html; charset=UTF-8">
#     <link href="static/style.css" rel="stylesheet" type="text/css">
#     <title>信息收集报告</title>
#     <script src="https://cdn.bootcss.com/vue/2.2.2/vue.min.js"></script>
#     <script src="https://cdn.bootcss.com/jquery/3.2.1/jquery.min.js"></script>
# </head>
#
# <body style="padding-right: 320px;">
# <div class="main-inner" id="main">
#     <div id="posts" class="posts-expand">
#         <header class="post-header">
#             <h1 class="post-title" itemprop="name headline">信息收集报告</h1>
#             <div class="post-meta">
#               <span class="post-time">
#                 <span class="post-meta-item-text">生成于</span>
#                 <time title="Post created" itemprop="dateCreated datePublished">%(create_time)s</time>
#               </span>
#             </div>
#         </header>
#         <div class="post-body" itemprop="articleBody" v-for="row in rows">
#
#             <div>
#                 <a v-bind:href="'#'+row.query">
#                     <h1 v-bind:id="row.query">{{row.query}}</h1>
#                 </a>
#                 <pre>{{row.data}}</pre>
#                 </br>
#             </div>
#         </div>
#
#     </div>
#     <aside id="sidebar" class="sidebar sidebar-active" style="display: block; width: 320px;">
#         <div class="sidebar-inner">
#             <ul class="sidebar-nav motion-element"
#                 style="opacity: 1; display: block; transform: translateX(0px);">
#                 <li class="sidebar-nav-toc sidebar-nav-active" data-target="post-toc-wrap">目录</li>
#             </ul>
#             <!--noindex-->
#             <section class="post-toc-wrap motion-element sidebar-panel sidebar-panel-active"
#                      style="opacity: 1; display: block; transform: translateX(0px);">
#                 <div class="post-toc" style="max-height: 750px; width: calc(100% + 0px);">
#                     <div class="post-toc-content">
#
#                         <ol class="nav">
#
#                             <li class="nav-item nav-level-1" v-for="row in rows">
#                                 <a class="nav-link" v-bind:href="'#'+row.query">
#                                     <span class="nav-text">{{row.query}}</span>
#                                 </a>
#                             </li>
#                         </ol>
#                     </div>
#                 </div>
#
#             </section>
#         </div>
#     </aside>
# </div>
# </body>
# <script>
#     var example = new Vue({
#         el: '#main',
#         data: {
#             rows: %(source_data)s
#         }
#     })
# </script>
# </html>
#         """
#         create_time = time.strftime("%Y-%m-%d", time.localtime(time.time()))
#         html_content = html_content.replace('%(create_time)s', create_time).replace('%(source_data)s', json.dumps(source_data))
#         with open(export_path, "w", encoding='utf-8') as f:
#             f.write(html_content)
