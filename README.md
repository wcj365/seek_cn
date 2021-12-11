# 求索 - 简易电子知识库 

Simple & Easy Electronic Knowledge Base, 简称SEEK。

本系统是Jupyter Book及Pandoc的无缝整合。

- 利用Jupyter Book生成可便于在线阅读和搜索的网站。
- 利用Pandoc生成便于线下阅读和打印的PDF版本。

## References

https://scastiel.dev/posts/2021-01-21-how-i-use-pandoc-to-create-my-programming-ebooks/

https://github.com/keevol/pandoc_md_book_starter

http://www.atdevin.com/3582.html

https://jdhao.github.io/2017/12/10/pandoc-markdown-with-chinese/

https://www.overleaf.com/learn/latex/XeLaTeX

## 使用说明

1. 初始化 
  - `$ setup.sh`
2. 生成网站 
  - `$ . jupyterbook.sh`
3. 生成PDF 
  - `$ . pandoc.sh`
4. 同时生成网站和PDF 
  - `$ . all.sh`

具体详见:  https://wcj365.github.io/peeps

~~~
# Part heading

## Chapter heading

### Section heading

#### Subsection heading
~~~