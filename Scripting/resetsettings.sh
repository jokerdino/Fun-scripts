#!/bin/bash

cd $HOME;
rm -rf .gnome .gnome2 .gconf .gconfd .metacity .cache .dbus .dmrc .mission-control .thumbnails ~/.config/dconf/user ~.compiz*
echo "Settings resetted"

gsettings set com.canonical.Unity.Launcher favorites "['application://nautilus-home.desktop', 'application://firefox.desktop', 'application://polly.desktop', 'application://tomboy.desktop', 'application://gtg.desktop', 'application://gnome-terminal.desktop', 'application://gedit.desktop', 'application://gnome-control-center.desktop', 'unity://running-apps', 'unity://expo-icon']"
gsettings set com.canonical.Unity.Devices blacklist "['18B4B7BBB4B799A8-OS', '75065C917775DC5A-']"
gsettings set com.canonical.indicator.datetime show-seconds "true"
gsettings set com.canonical.indicator.datetime show-day "true"
gsettings set com.canonical.indicator.datetime time-format "24-hour"
gsettings set com.canonical.indicator.datetime show-week-numbers "true"


echo "Added items and blacklisted mounts."

gsettings set org.gnome.shell.overrides button-layout "close,minimize,maximize:"
gsettings set org.gnome.desktop.wm.preferences focus-mode "sloppy"
gsettings set org.gnome.desktop.wm.preferences action-double-click-titlebar "toggle-shade"
gsettings set org.gnome.shell favorite-apps "['nautilus.desktop', 'firefox.desktop', 'polly.desktop', 'tomboy.desktop', 'gtg.desktop', 'gnome-terminal.desktop', 'gedit.desktop', 'gnome-control-center.desktop']"
gsettings set org.gnome.shell.calendar show-weekdate "true"
gsettings set org.gnome.desktop.interface clock-show-seconds "true"
gsettings set org.gnome.desktop.interface clock-show-date "true"

echo "Replacing current session"

if [ "$XDG_CURRENT_DESKTOP" = "Unity" ]
then
 unity --replace & disown

else
 bash theme.sh
 gnome-shell --replace & disown

fi
