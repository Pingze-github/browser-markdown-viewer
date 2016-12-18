# browser-markdown-viewer
A simple markdown file viewer. It turns your markdown into html file and call the browser to show it.
# Markdown浏览器阅读器
一个简单的markdown文件阅读器。它将你的markdown文件转换成html文件并调用浏览器来显示。

## Installation
1. Make sure you have Python2.7.
2. Install the unofficial Libraries.
```
pip install misaka
pip install pygments
pip install pyquery
```

## 安装
1. 确保你有Pyhton2.7及以上版本（非Python3）。
2. 安装非官方库。
```
pip install misaka
pip install pygments
pip install pyquery
```

## Usage
1. (Only in Windows) Change your .md's "default open mode" into the "bmv.exe". 
2. Or use the Python script "bmv.py" by command ```python bmv.py -i [filepath]```.

## 使用
1. （Windows下有效）更改你的.md文件的默认打开方式为“bmv.exe”。
2. 或者使用Python脚本“bmv.py”。命令为 ```python bmv.py -i [filepath]```。

## Note
1. The temp htmls are saved in the temp dir: "C:/Windows/Temp/bmv". It's the default temp dir of Windows. If you use other OS or just want to change it, edit the variable ```tempdir``` in the script "bmv.py".
2. You can change the html's style by edit css files.
3. "bmv.exe" is just converted from "bmv.bat".

## 注意
1. 临时生成的html文件被储存在临时文件夹"C:/Windows/Temp/bmv"。这是Windows系统的公用文件夹，如果你使用其他操作系统或者只是想要改变，可以编辑脚本“bmv.py”中的```tempdir```变量。
2. 你可以通过更改css文件来改变html的显示样式。
3. “bmv.exe”只是"bmv.bat"转换来的。目的是为了能够设置成默认打开方式。
