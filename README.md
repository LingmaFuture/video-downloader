# 视频下载器

一个基于 Django 和 yt-dlp 的简单视频下载工具，支持从多个平台下载视频。

## 功能特点

- 简洁的用户界面
- 支持多平台视频下载
- 自定义下载目录
- 代理支持
- 响应式设计

## 环境要求

- Python 3.12+
- Django 5.1.3+
- yt-dlp

## 安装步骤

1.克隆仓库

```bash
git clone https://github.com/LingmaFuture/video-downloader.git
cd video_downloader
```

2.创建并激活虚拟环境

```bash
python -m venv .venv
# Windows
.venv\Scripts\activate
# Linux/Mac
source .venv/bin/activate
```

3.安装依赖

```bash
pip install -r requirements.txt
```

4.运行迁移

```bash
python manage.py migrate
```

5.启动服务器

```bash
python manage.py runserver
```

## 使用说明

1. 访问 <http://127.0.0.1:8000>
2. 在输入框中粘贴视频链接
3. 点击"下载视频"按钮
4. 视频将被下载到用户的 Downloads 目录

## 代理设置

如果需要使用代理，可以在 `video123/scraper.py` 中修改代理设置：

```python
yt_dlp_command = [
    'yt-dlp',
    '--proxy', 'http://127.0.0.1:7897',  # 修改为您的代理地址
    '-o', os.path.join(download_dir, '%(title)s.%(ext)s'),
    url
]
```

## 项目结构

```plaintext
video-downloader/
├── manage.py
├── requirements.txt
├── README.md
├── video-downloader/
│   ├── settings.py
│   ├── urls.py
|   ├── asgi.py
│   └── wsgi.py
└── video123/
    ├── apps.py
    ├── views.py
    ├── scraper.py
    ├── urls.py
    └── templates/
        └── index.html
```

## 常见问题

1. **下载失败**
   - 检查网络连接
   - 确认代理设置是否正确
   - 验证 yt-dlp 是否最新版本

2. **代理错误**
   - 确保代理服务器正在运行
   - 验证代理端口是否正确

## 贡献指南

1. Fork 项目
2. 创建特性分支 (`git checkout -b feature/AmazingFeature`)
3. 提交更改 (`git commit -m 'Add some AmazingFeature'`)
4. 推送到分支 (`git push origin feature/AmazingFeature`)
5. 开启 Pull Request

## 许可证

此项目基于 MIT 许可证 - 查看 [LICENSE](LICENSE) 文件了解详情

## 联系方式

作者邮箱：<rockwaychen@qq.com>

项目链接: [https://github.com/LingmaFuture/video-downloader](https://github.com/LingmaFuture/video-downloader)
