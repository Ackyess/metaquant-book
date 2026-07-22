# 诚实的量化交易

《诚实的量化交易：写给新手的第一堂课》1.0 单文件网页阅读器与简体中文源稿。

- 在线阅读：<https://quant.leooo.fun/>
- `index.html`：可直接打开或静态托管的完整阅读器
- `book.md`：最终简体中文编辑源稿，包含脚注
- `output/epub/诚实的量化交易-1.0.epub`：适用于 Apple Books、Kobo 与“发送至 Kindle”的 EPUB 3
- `output/pdf/诚实的量化交易-1.0.pdf`：带封面、目录与页码的 A5 固定版式
- `versions/`：早期简体稿、GPT 修订稿与手工修订快照

阅读器包含 21 个阅读屏、折叠目录、深浅主题、阅读进度与位置记忆，以及桌面/移动端脚注界面。

本地预览：

```bash
python -m http.server 8799
```

然后访问 <http://127.0.0.1:8799/>。

重新生成电子书：

```bash
python scripts/build_ebooks.py
```

## 许可

- 书稿、封面及生成的 HTML、EPUB、PDF 内容：CC BY-SA 4.0
- 阅读器代码与构建脚本：MIT License
- 统一署名：[@Ackyess](https://github.com/Ackyess)

完整条款见 [`LICENSE`](LICENSE)。
