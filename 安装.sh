Name()
{
    if grep -Eqii "CentOS" /etc/issue || grep -Eq "CentOS" /etc/*-release; then
        DISTRO='CentOS'
        PM='yum'
    elif grep -Eqi "Red Hat Enterprise Linux Server" /etc/issue || grep -Eq "Red Hat Enterprise Linux Server" /etc/*-release; then
        DISTRO='RHEL'
        PM='yum'
    elif grep -Eqi "Aliyun" /etc/issue || grep -Eq "Aliyun" /etc/*-release; then
        DISTRO='Aliyun'
        PM='yum'
    elif grep -Eqi "Fedora" /etc/issue || grep -Eq "Fedora" /etc/*-release; then
        DISTRO='Fedora'
        PM='yum'
    elif grep -Eqi "Debian" /etc/issue || grep -Eq "Debian" /etc/*-release; then
        DISTRO='Debian'
        PM='apt'
    elif grep -Eqi "Ubuntu" /etc/issue || grep -Eq "Ubuntu" /etc/*-release; then
        DISTRO='Ubuntu'
        PM='apt'
    elif grep -Eqi "Raspbian" /etc/issue || grep -Eq "Raspbian" /etc/*-release; then
        DISTRO='Raspbian'
        PM='apt'
    elif grep -Eqi "Manjaro Linux" /etc/issue || grep -Eq "Manjaro Linux" /etc/*-release; then
        PM='pacman'
        DISTRO='Manjaro Linux'
        echo 'Manjaro Linux'
        yay -S FFmpeg
        yay -S aria2
    elif grep -Eqi "Arch Linux" /etc/issue || grep -Eq "Arch Linux" /etc/*-release; then
        PM='pacman'
        DISTRO='Arch Linux'
        yay -S FFmpeg
        yay -S aria2
    else
        DISTRO='无法识别你的操作系统，请自行安装FFmpeg和aria2'
    fi
    if [ $PM != 'pacman' ]
    then
      echo $DISTRO;
    fi
}
echo 请在安装目录下运行此文件,否则请强行退出该脚本
sudo rm -rf /usr/share/applications/bbdown-flet-gui.desktop
sudo rm -rf /usr/local/BBDown-Flet-GUI
sudo mv desktop-entry.txt  /usr/share/applications/bbdown-flet-gui.desktop
sudo mkdir /usr/local/BBDown-Flet-GUI
sudo mv ./*  /usr/local/BBDown-Flet-GUI/
chmod 777 /usr/local/BBDown-Flet-GUI/*
Name
if [ $PM != 'pacman' ]
then
  sudo $PM install ffmpeg
  sudo $PM install aria2
fi
