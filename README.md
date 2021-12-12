# 求索 （SEEK）

求索（SEEK）是一个电子知识保存及分享系统，适用于出版电子书籍和管理电子档案。个人和企业都适用。

求索由王超杰博士独立开发。其英文全称是`Simply Elegant Electronic Knowledge System`，简写为SEEK。

本系统是Jupyter Book及Pandoc的无缝整合。它利用Jupyter Book生成便于在线阅读和搜索的网站，并利用Pandoc生成pdf版本以便线下打印阅读和epub版本以便使用电子书阅读器在平板电脑上线下阅读。。

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
  - `$ . buildall.sh`

具体详见:  https://wcj365.github.io/seek

实际应用：https://wcj365.github.io/1000

~~~
# Part heading

## Chapter heading

### Section heading

#### Subsection heading
~~~

## 一本书的结构

如下表所示，一本书可以包括几个辑，每一辑包含几个章，每一章包含几个节。
一本电子书，一章的内容存在一个文本。
同一辑的章放在同一个子目录。一个辑一个子目录。
子目录所属的根目录代表一本书。

组成部分      | 代表格式              | Example 千家诗
-------------| ---------------------|-----------------------------------------------
书(book)     | 根目录                | src/                                       |
辑(part)     | 子目录                | src/01_qi_jue (七绝) ，src/02_qi_lv (七律） |
章(chapter)  | 文本（Markdown格式）  | 01.md （程颢），以#开头                      |
节(section)  | 文本中的部分          | 春日偶成，以##开头                           |

## 子目录及文本命名规则

代表辑的子目录和代表章的文本，名字都要以两位数字开头。数字大小决定各个辑，各个章在书中的顺序。
比如，一下就是【千家诗】的结构和顺序：

- 第一辑 七绝 (src/01_qi_jue)
  - 第一章 程颢 (src/01_qi_jue/01.md)
    - 第一节 【春日偶成】
  - 第二章 朱熹 (src/01_qi_jue/02.md)
    - 第一节【春日】
    - 第二节【题榴花】
- 第二辑 七律 (src/02_qi_lv)
- 第三辑 五绝 (src/03_wu_jue)
- 第四辑 五律 (src/04_wu_lv)

