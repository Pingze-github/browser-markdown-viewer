# coding=u8

import sys
import os
import getopt
import misaka as m
from pygments import highlight
from pygments.formatters import HtmlFormatter
from pygments.lexers import get_lexer_by_name
import webbrowser
import hashlib
from pyquery import PyQuery as pq

thisDir = os.path.split(os.path.realpath(sys.argv[0]))[0] 
tempdir = 'C:/Windows/Temp/bmv' # dir to save .html
cpath1 = thisDir+'/css/main/main.css' # style of full html
cpath2 = thisDir+'/css/md/github.css' # style of markdown

class HighlighterRenderer(m.HtmlRenderer):
    def blockcode(self, text, lang):
        if not lang:
            return '\n<pre><code>{}</code></pre>\n'.format(
                text.strip())
        lexer = get_lexer_by_name(lang, stripall=True)
        formatter = HtmlFormatter()
        return highlight(text, lexer, formatter)

def compile(markdown):
    renderer = HighlighterRenderer()
    md = m.Markdown(renderer, extensions=('fenced-code','tables','math','math-explicit','quote','highlight','autolink','footnotes','strikethrough','underline'))
    with open(cpath1,'r') as f1, open(cpath2,'r') as f2:
        main_style = f1.read()
        highlight_style = f2.read()
    article = md(markdown)
    html = '<html><head><style>'+main_style+"</style><style>"+highlight_style+'</style></head><body><article class="markdown-body">'+article+'</article></body><html>'
    return html

def src_fix(html,mpath):
    mdir = os.path.dirname(mpath)
    d = pq(html)
    images = d("img")
    for i in range(len(images)):
        image = images.eq(i)
        src = (image).attr('src')
        src_abs = mdir + src
        if ('http' not in src) and os.path.exists(src_abs) and os.path.isfile(src_abs):
            html = html.replace(src,src_abs)
    return html

def create(mpath):
    with open(mpath,'r') as f:
        markdown = f.read()
    markdown = markdown.decode('utf-8','ignore')
    html = compile(markdown)
    html = src_fix(html,mpath)
    hash_str = mpath + html.encode('utf-8')
    hname = hashlib.md5(hash_str).hexdigest() + '.html'
    hpath = tempdir+hname
    if(not (os.path.exists(hpath) and os.path.isfile(hpath))):  
        html = html.encode('utf-8','ignore')
        with open(hpath,'w') as f:
            f.write(html)
    return hpath

def main():
    opts, args = getopt.getopt(sys.argv[1:], "hi:o:", ["help", "input="])

    def showhelp():
            print ' -i filepath (open file)'
            print ' -h (show help info)'

    input_file = ''
    if (len(opts)<1):
        showhelp()
    for op, value in opts:
            if op == '-i':
                    input_file = value
                    hpath = create(input_file)
                    print("Open markdown file: {} as {} ".format(input_file,hpath))
                    webbrowser.open(hpath)
            elif op == '-h':
                    showhelp()
                    sys.exit()
            else:
                    showhelp()
                    sys.exit()                


if __name__ == '__main__':
    main()
