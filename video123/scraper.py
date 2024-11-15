import subprocess
import os


def download_video(url):
    # 使用项目目录下的 downloads 文件夹
    download_dir = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'downloads')
    
    # 确保下载目录存在
    os.makedirs(download_dir, exist_ok=True)
    
    try:
        yt_dlp_command = [
            'yt-dlp',
            '--proxy', 'http://127.0.0.1:7897',  # 代理设置
            '--socket-timeout', '30',          # 添加超时设置
            '--retries', '3',                  # 添加重试次数
            '--fragment-retries', '3',         # 片段重试次数
            '--force-ipv4',                    # 强制使用 IPv4
            '-o', os.path.join(download_dir, '%(title)s.%(ext)s'),  # 输出路径设置
            url
        ]
        
        # 执行下载命令
        result = subprocess.run(yt_dlp_command, capture_output=True, text=True)
        
        if result.returncode == 0:
            return "已保存至项目下载目录！"
        else:
            return f"下载失败: {result.stderr}"
            
    except Exception as e:
        return f"发生错误: {str(e)}"
