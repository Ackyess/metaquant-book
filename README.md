# 诚实的量化交易

《诚实的量化交易：写给新手的第一堂课》1.1 的中英文源稿、单文件网页阅读器与电子书构建脚本。

- 在线阅读：<https://quant.leooo.fun/>
- English edition: <https://quant.leooo.fun/en/>
- `book.md`：完整的中文生活化版源稿，包含脚注
- `versions/03-humanizer-zh-round2.md`：中文精炼版源稿
- `book.en.md`：完整的英文 Story Edition 源稿
- `versions/03-humanizer-en-round2.md`：英文 Concise Edition 源稿
- `index.html`：中文单文件阅读器
- `en/index.html`：英文单文件阅读器
- `output/epub/诚实的量化交易-1.1.epub`：EPUB 3
- `output/pdf/诚实的量化交易-1.1.pdf`：带封面、目录与页码的 A5 PDF

两种语言的阅读器都保留完整版本与精炼版本。读者首次进入正文时选择一次，设置保存在同源浏览器的 `mq-reading-style-v1`；中英文切换后会沿用同一选择，也可从右上角重新选择。

## 本地预览

```bash
python -m http.server 8799
```

访问 <http://127.0.0.1:8799/>。不要直接依赖 `file://` 预览服务工作线程、语言切换缓存或深链接行为。

## 环境与依赖

建议使用 Python 3.11 或更高版本。

```bash
python -m pip install -r requirements.txt
playwright install chromium
```

PDF 由 WeasyPrint 生成，以避免不同 Chromium/CJK 字体组合造成的文本映射差异。浏览器回归默认依次查找 Playwright Chromium、系统 Chromium、Google Chrome 或 Microsoft Edge；也可以显式指定浏览器：

```bash
METAQUANT_CHROMIUM=/path/to/chromium python scripts/browser_reader_audit.py
```

Windows PowerShell 可使用 `$env:METAQUANT_CHROMIUM = "C:\\path\\to\\chrome.exe"`。

## 重建阅读器与质量门槛

修改任一精炼版源稿后，按以下顺序执行：

```bash
python scripts/build_reader_styles.py
python scripts/check_readers.py
python scripts/browser_reader_audit.py
python scripts/content_red_team_audit.py
```

- `build_reader_styles.py` 把中英文精炼版渲染并嵌入各自阅读器。
- `check_readers.py` 检查章节、脚注、练习、表格、风险边界、源稿哈希、双语结构和读者状态逻辑。
- `browser_reader_audit.py` 在本地临时服务器上实测二选一、深链接拦截、刷新记忆、重选、脚注、键盘、目录、中英状态继承，以及 390×844 和桌面视口。
- `content_red_team_audit.py` 复核中英文两版的结构同构、章节改写比例、风险边界、残留占位符、重复段落，并复用电子书与阅读器验证器。需要同时检验新生成 PDF 时，传入 `--pdf-smoke /path/to/rebuilt.pdf`。
- 浏览器审计结果写入 `audit/browser-reader-audit.json`，内容审计写入 `audit/content-audit.json`，截图写入 `audit/screenshots/`。

## 电子书

重新生成：

```bash
python scripts/build_ebooks.py --format all
```

只生成 EPUB 或 PDF：

```bash
python scripts/build_ebooks.py --format epub
python scripts/build_ebooks.py --format pdf
```

验证现有产物：

```bash
python scripts/build_ebooks.py --check
```

电子书当前以完整中文生活化版 `book.md` 为正文；网页阅读器才包含双文风切换。

## 发布边界

构建与审计脚本不会部署网站。发布到托管平台应作为独立、显式步骤执行，并在本地审计全部通过、内容经人工确认后进行。

## 许可

- 书稿、封面及生成的 HTML、EPUB、PDF 内容：CC BY-SA 4.0
- 阅读器代码与构建脚本：MIT License
- 统一署名：[@Ackyess](https://github.com/Ackyess)

完整条款见 [`LICENSE`](LICENSE)。
