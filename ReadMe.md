# 问答：操作系统原理

2022年9月至10月。

- `第○章.md`：每章的问答作业。

- `renormalize.py`：规范文件名。

  用于提交作业。第一次使用前要先填充文件名模板。

- `clean_html_table.py`：清理 HTML 表格。

  作业题目公布于 [Moodle 网络教室](https://lexue.bit.edu.cn/course/view.php?id=11242)，其中表格源代码（HTML）较为复杂，不宜直接插入`第○章.md`。因此清理后再插入。（先用此脚本清理，再手动微调。）

## 可能存在的疑问

### 公式显示异常

> `\qty`

这来自 physics 宏包，MathJax 适当配置后才支持。

---

> You can't use ‘macro parameter character #’ in math mode.

Web 上的公式毕竟不是 LaTeX，只支持个别宏包，所以我自己定义了一些“次品”，如`\SI`。

如果你的 Markdown 查看器支持 MathJax 全局宏（例：Typora），应当能正常显示；不然（例：2022年10月的 GitHub）只好凑活看了。

### 提交的 commit date 和 author date 不一致

我清理过敏感信息，因此不一致。

可参考 [GitHub 文档](https://docs.github.com/en/account-and-profile/setting-up-and-managing-your-github-profile/managing-contribution-settings-on-your-profile/troubleshooting-commits-on-your-timeline#how-github-uses-the-git-author-date-and-commit-date)。

### 回答是否可靠？

不一定。

不过有不少题目我和同学交流过，或者与答案核对过。

欢迎提出 issues。
