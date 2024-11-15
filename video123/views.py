from django.shortcuts import render
from .scraper import download_video  # 确保从scraper.py导入download_video函数

from django.http import FileResponse
import os

import subprocess
from django.http import JsonResponse

def get_video_url(request):
    video_page_url = request.GET.get('url')
    command = ['yt-dlp', '--get-url', video_page_url]
    process = subprocess.run(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE, universal_newlines=True)
    if process.returncode == 0:
        video_url = process.stdout.strip()
        return JsonResponse({'url': video_url})
    else:
        return JsonResponse({'error': '解析失败'}, status=400)

def download_file(request):
    # 这里以下载位于项目根目录下的 downloads 文件夹中的 example.pdf 文件为例
    filepath = 'downloads/example.pdf'
    abs_path = os.path.join(os.path.dirname(__file__), filepath)
    response = FileResponse(open(abs_path, 'rb'), as_attachment=True, filename='example.pdf')
    return response

def index(request):
    download_message = ''
    if request.method == 'POST':
        video_url = request.POST.get('video_url', '')
        # 调用download_video函数，并将结果存储在download_message变量中
        download_message = download_video(video_url)
    return render(request, 'index.html', {'download_message': download_message})