django 将会默认在这个目录里查找模板文件

你项目的TEMPLATES配置项描述了Django如何载入和渲染模板的，默认的设置文件设置了DjangoTemplates后端
并将APP_DIRS设置为True,

这一选项将会让DjangoTemplates在每个INSTALLED_APPS文件夹当中寻找“templates”子目录.

