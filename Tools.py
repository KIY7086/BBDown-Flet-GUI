import getpass
import tkinter as tk
from tkinter import ttk
from ttk_message import message
import os
import subprocess
import time
from PIL import ImageTk, Image
import ttkthemes

user_name = getpass.getuser()

check_config = {
        '调用aria2c进行下载': '--use-aria2c',
        '不要显示所有可用音视频流': '--hide-streams',
        '使用多线程下载': '--multi-thread',
        '仅下载视频': '--video-only',
        '仅下载音频': '--audio-only ',
        '仅下载弹幕': '--danmaku-only',
        '仅下载字幕': '--sub-only',
        '仅下载封面': '--cover-only',
        '输出调试日志': '--debug',
        '跳过混流步骤': '--skip-mux',
        '跳过字幕下载': '--skip-subtitle',
        '跳过封面下载': '--skip-cover',
        '下载音视频时强制使用HTTP协议替换HTTPS': '--force-http',
        '下载弹幕': '--download-danmaku',
        '跳过AI字幕下载': '--skip-ai',
        '视频升序': '--video-ascending',
        '音频升序': '--audio-ascending',
        '不替换PCDN域名': '--allow-pcdn',
        '强制替换下载服务器host': '--force-replace-host',
    }
