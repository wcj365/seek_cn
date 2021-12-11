# 求索知库

简单雅致的电子知识保存及分享系统

Simply Elegant Electronic Knowledge System, 简称SEEK。

本系统是Jupyter Book及Pandoc的无缝整合。

- 利用Jupyter Book生成可便于在线阅读和搜索的网站。
- 利用Pandoc生成便于线下阅读和打印的pdf和epub版本。

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

具体详见:  https://wcj365.github.io/seek

实际应用：https://wcj365.github.io/1000

~~~
# Part heading

## Chapter heading

### Section heading

#### Subsection heading
~~~


Component  | Representation                | Example 千家诗
-----------| ------------------------------|-----------------------------------
Book 书    | root folder                   | src/                                               |
Part 辑    | sub folders                   | src/01_qi_jue (七绝)                               |
Chapter 章 | markdown files                | 01.md （程颢） first line is chapter title with #  |
Section 节 | sections within a chapter     | 春日偶成，first line is section title ##            |