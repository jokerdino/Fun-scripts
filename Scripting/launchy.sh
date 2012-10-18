#!/bin/sh
value=$(gsettings get org.compiz.unityshell:/org/compiz/profiles/unity/plugins/unityshell/ launcher-hide-mode)
if [ $value = 0 ]
then
 gsettings set org.compiz.unityshell:/org/compiz/profiles/unity/plugins/unityshell/ launcher-hide-mode 1
else
 gsettings set org.compiz.unityshell:/org/compiz/profiles/unity/plugins/unityshell/ launcher-hide-mode 0
fi
