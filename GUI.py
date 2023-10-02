import webbrowser
import flet as ft
import platform
from ttk_message import message

def main(page: ft.page):
    check_value = {
        '调用aria2c进行下载': False,
        '不要显示所有可用音视频流': False,
        '使用多线程下载': True,
        '仅下载视频': False,
        '仅下载音频': False,
        '仅下载弹幕': False,
        '仅下载字幕': False,
        '仅下载封面': False,
        '输出调试日志': False,
        '跳过混流步骤': False,
        '跳过字幕下载': False,
        '跳过封面下载': False,
        '下载音视频时强制使用HTTP协议替换HTTPS': True,
        '下载弹幕': False,
        '跳过AI字幕下载': True,
        '视频升序': False,
        '音频升序': False,
        '不替换PCDN域名': False,
        '强制替换下载服务器host': True,
    }
    page.fonts = {
        "sarasa": "Sarasa-Gothic.ttf",
        "SmileySans": "SmileySans-Oblique.otf"
    }

    def page_top():
        global user_input
        page.window_width = 1000
        page.window_height = 800
        page.theme = ft.Theme(font_family="sarasa", use_material3=True)
        page.title = "哔哩哔哩下载器"
        label = ft.Text(value="哔哩哔哩视频下载", style=ft.TextThemeStyle.DISPLAY_LARGE, font_family="SmileySans")
        user_input = ft.TextField(label="输入视频的BV号,AV号或地址")
        page.add(ft.Container(ft.Row([label], alignment=ft.MainAxisAlignment.CENTER), padding=50),
                 ft.Container(user_input, padding=20))

    def is_check(value):
        if check_value[value] is False:
            check_value[value] = True
        else:
            check_value[value] = False

    def checkbox():

        chk1 = ft.ElevatedButton(text='使用TV端解析模式（大UP主的视频可能无水印）', on_click=lambda _: login('tv'))

        chk2 = ft.ElevatedButton(text='使用网页端解析模式', on_click=lambda _: login('app'))

        chk7 = ft.Checkbox(label='调用aria2c进行下载', value=check_value['调用aria2c进行下载'],
                           on_change=lambda e: is_check('调用aria2c进行下载'))

        chk9 = ft.Checkbox(label='不要显示所有可用音视频流', value=check_value['不要显示所有可用音视频流'],
                           on_change=lambda e: is_check('不要显示所有可用音视频流'))

        chk10 = ft.Checkbox(label='使用多线程下载', value=check_value['使用多线程下载'],
                            on_change=lambda e: is_check('使用多线程下载'))

        global selector

        selector = ft.Dropdown(
            width=200,
            options=[
                ft.dropdown.Option('仅下载视频'),
                ft.dropdown.Option('仅下载音频'),
                ft.dropdown.Option('仅下载弹幕'),
                ft.dropdown.Option('仅下载字幕'),
                ft.dropdown.Option('仅下载封面')
            ]
        )

        chk16 = ft.Checkbox(label='输出调试日志', value=check_value['输出调试日志'],
                            on_change=lambda e: is_check('输出调试日志'))

        chk17 = ft.Checkbox(label='跳过混流步骤', value=check_value['跳过混流步骤'],
                            on_change=lambda e: is_check('跳过混流步骤'))

        chk18 = ft.Checkbox(label='跳过字幕下载', value=check_value['跳过字幕下载'],
                            on_change=lambda e: is_check('跳过字幕下载'))

        chk19 = ft.Checkbox(label='跳过封面下载', value=check_value['跳过封面下载'],
                            on_change=lambda e: is_check('跳过封面下载'))

        chk20 = ft.Checkbox(label='下载音视频时强制使用HTTP协议替换HTTPS',
                            value=check_value['下载音视频时强制使用HTTP协议替换HTTPS'],
                            on_change=lambda e: is_check('下载音视频时强制使用HTTP协议替换HTTPS'))

        chk21 = ft.Checkbox(label='下载弹幕', value=check_value['下载弹幕'],
                            on_change=lambda e: is_check('下载弹幕'))

        chk22 = ft.Checkbox(label='跳过AI字幕下载', value=check_value['跳过AI字幕下载'],
                            on_change=lambda e: is_check('跳过AI字幕下载'))

        chk23 = ft.Checkbox(label='视频升序', value=check_value['视频升序'],
                            on_change=lambda e: is_check('视频升序'))

        chk24 = ft.Checkbox(label='音频升序', value=check_value['音频升序'],
                            on_change=lambda e: is_check('音频升序'))

        chk25 = ft.Checkbox(label='不替换PCDN域名', value=check_value['不替换PCDN域名'],
                            on_change=lambda e: is_check('不替换PCDN域名'))

        chk26 = ft.Checkbox(label='强制替换下载服务器host', value=check_value['强制替换下载服务器host'],
                            on_change=lambda e: is_check('强制替换下载服务器host'))

        global encoding_priority

        encoding_priority = ft.TextField(label='画质优先级,用逗号分隔\n例: "1080P 高码率, 杜比视界"\n若输入有误，则默认选择最高画质')

        global select_page

        select_page = ft.TextField(label='输入要下载的分P或指定下载范围\n如：1,3,8或1-3')

        check_row1 = ft.Row(
            [chk1, chk2, chk7]
        )
        check_row3 = ft.Row(
            [chk9, chk10, chk16, selector]
        )
        global check_row4
        check_row4 = ft.Row(
            [chk21, select_page, encoding_priority]
        )
        check_row5 = ft.Row(
            [chk17, chk18, chk19, chk20]
        )
        check_row6 = ft.Row(
            [chk22, chk23, chk24, chk25, chk26]
        )
        global all_row
        all_row = ft.Column(
            [check_row1, check_row3, check_row5, check_row6, check_row4]
        )

    def pro(e):
        check_value['仅下载视频'] = False
        check_value['仅下载音频'] = False
        check_value['仅下载弹幕'] = False
        check_value['仅下载字幕'] = False
        check_value['仅下载封面'] = False
        check_value[selector.value] = True
        global is_pro
        if not is_pro:
            page.add(ft.Container(all_row, padding=20))
            is_pro = True

    def edit_config():
        global select_page
        global selector
        global sessdata
        global use_login_mode
        with open("BBDown.config", "w") as file:
            file.write(f'# 本文件是BBDown程序的配置文件\n--work-dir {download_dir}\n')
            for config in check_config.keys():
                if check_value[config] is True:
                    if select_page.value is not None:
                        file.write('--select-page ' + select_page.value + '\n')
                    elif encoding_priority is not None:
                        file.write('--encoding-priority ' + encoding_priority.value + '\n')
                    else:
                        file.write(check_config[config] + '\n')
                else:
                    continue

    def ready_to_run(e):
        edit_config()
        run(user_input)

    def page_bottom():
        global help_text
        pro_button = ft.ElevatedButton(text="高级选项", on_click=pro)
        submit = ft.ElevatedButton(text="开始下载", on_click=ready_to_run)
        github = ft.ElevatedButton(text="BBDown项目地址",
                                   on_click=lambda _: webbrowser.open('https://github.com/nilaoda/BBDown'))
        help = ft.ElevatedButton(text="帮助",
                                 on_click=lambda _: message(message=help_text, font_size=10, width=330, height=120))
        info = ft.ElevatedButton(text="关于",
                                 on_click=lambda _: message(message="本程序基于Github开源项目BBDown\n感谢原作者@nilaoda"
                                                                    "\n本程序作者：KIY7086"))

        page.add(
            ft.Container(
                ft.Row(
                    [
                        pro_button,
                        submit,
                        info,
                        help,
                        github,
                    ]
                ),
                padding=20
            )
        )

    page_top()
    page_bottom()
    checkbox()


if __name__ == '__main__':
    system = platform.system()
    if system == 'Linux':
        from Run_Linux import *
        help_text = "如果视频无法下载或二维码无法加载请多试几次\n或运行\"准备工作.sh\"\n也有可能是BBDown主程序问题"
    else:
        from Run_Windows import *
        help_text = "如果视频无法下载或二维码无法加载请多试几次\n也有可能是BBDown主程序问题"
    log = ''
    first_download = True
    is_pro = False
    print(download_dir)
    if not os.path.exists(download_dir):
        os.mkdir(download_dir)
    have_downloaded_video = False
    ft.app(target=main)
