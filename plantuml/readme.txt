plantuml之word模板安装方法：

1. 确认本机安装有java运行环境，如果没有，从oracle网站下载
2. 拷贝『Template\PlantUML_Template.dotm』文件到『%appdata%\Microsoft\Word\STARTUP』
3. 拷贝『Plantuml.jar』文件到『%appdata%』目录
4. 运行graphviz-2.38.msi，安装GraphViz

顺利的话，重启Word，就能看到plantuml菜单了。

* 有关UML语法的详细说明，可在"PlantUML_Language_Reference_Guide.pdf"中查找。
* 如果遇到宏报错，可尝试将文档内容拷贝到一新建文档中。