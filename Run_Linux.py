from Tools import *

download_dir = '/home/' + user_name + '/BiliVideo'


def login(mode):
    if mode == 'tv':
        subprocess.Popen(r'./BBDown logintv', shell=True)
    else:
        subprocess.Popen(r'./BBDown login', shell=True)
    time.sleep(0.5)
    root = tk.Tk()
    root.title("显示图片")
    root.configure(bg='white')
    window = ttk.Frame(root)
    style = ttkthemes.ThemedStyle(window)
    style.set_theme('arc')
    root.resizable(False, False)
    root.wm_attributes('-topmost', 1)
    image_path = 'qrcode.png'
    while True:
        try:
            image = Image.open(image_path)
            break
        except:
            continue
    image = ImageTk.PhotoImage(image)
    qrcode = ttk.Label(root, image=image)
    qrcode.pack()
    ttk.Frame(window, height=5).pack(side=tk.BOTTOM)
    ttk.Button(window, text='确定', command=lambda: root.destroy()).pack()
    window.pack()
    root.mainloop()
    os.remove('qrcode.png')
    global use_login_mode
    use_login_mode = mode


def run(user_input):
    global download_dir
    if user_input.value == '':
        message(message='请先输入BV、AV号或链接')
    else:
        message(message=f'下载时不会有任何显示，请您耐心等待\n文件将会下载到\n{download_dir}目录下', width=310)
        while True:
            icmp_out = subprocess.Popen(r"./BBDown " + user_input.value, shell=True,
                                        stdout=subprocess.PIPE, stderr=subprocess.PIPE)
            stdout, stderr = icmp_out.communicate()
            time.sleep(0.5)
            try:
                output = stdout.decode(encoding="utf-8")
            except UnboundLocalError:
                continue
            print(output)
            if "任务完成" in output:
                os.remove('BBDown.config')
                time.sleep(2)
                message(message=f'视频已下载到/home/BiliVideo目录下')
                break
            elif "输入有误" in output:
                message("BV/AV号/或地址输入有误")
                break
