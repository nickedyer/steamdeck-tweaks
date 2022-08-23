#!/usr/bin/bash

if [ "$EUID" -ne 0 ]
  then echo "ERROR: Please run this script as root."
  [[ "$0" = "$BASH_SOURCE" ]] && exit 1 || return 1
fi

echo "This script will install TigerVNC on your Steam Deck."
echo "It is operating under the following assumptions:"
echo "  1. The current user is \"deck\""
echo "  2. Your Steam Deck's system is current in read-only mode"
echo "  2. You have not installed anything from pacman or the AUR previously"
echo "  3. You are okay with resetting pacman keys"
echo ""
read -p "Press Y to continue, or press any other key to quit: " -n 1 -r
echo    # (optional) move to a new line
if [[ ! $REPLY =~ ^[Yy]$ ]]
then
  echo "Quitting..."
  [[ "$0" = "$BASH_SOURCE" ]] && exit 1 || return 1
fi
echo "Continuing..."

steamos-readonly disable
pacman-key --init
pacman-key --populate archlinux
pacman -S tigervnc --noconfirm
echo ""
echo "Please type in the password that should be used to connect to the VNC server."
sudo -u deck vncpasswd
mkdir /home/deck/.vnc
touch /home/deck/.vnc/config
echo "session=kde" > /home/deck/.vnc/config
echo "geometry=1280x800" >> /home/deck/.vnc/config
wget https://upload.wikimedia.org/wikipedia/commons/thumb/a/a9/TigerVNC_logo.svg/240px-TigerVNC_logo.svg.png -O /home/deck/.vnc/tigervnc.png
chown deck:deck -R /home/deck/.vnc
chmod -R 755 /home/deck/.vnc

touch /home/deck/Desktop/vnc-server.desktop
echo "[Desktop Entry]" > /home/deck/Desktop/vnc-server.desktop
echo "Name=Start VNC Server" >> /home/deck/Desktop/vnc-server.desktop
echo "Exec=x0vncserver -rfbauth /home/deck/.vnc/passwd" >> /home/deck/Desktop/vnc-server.desktop
echo "Icon=/home/deck/.vnc/tigervnc.png" >> /home/deck/Desktop/vnc-server.desktop
echo "Terminal=true" >> /home/deck/Desktop/vnc-server.desktop
echo "Type=Application" >> /home/deck/Desktop/vnc-server.desktop
echo "StartupNotify=false" >> /home/deck/Desktop/vnc-server.desktop
chown deck:deck /home/deck/Desktop/vnc-server.desktop
chmod 755 /home/deck/Desktop/vnc-server.desktop
echo "VNC Server installed."
