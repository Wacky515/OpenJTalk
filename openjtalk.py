# !/usr/bin/python
# -*- coding: utf-8 -*-
# -----------------------------------------------------------------------------
# Name:        openjtalk.py
# Purpose:     In README.md
#
# Author:      Kilo11
#
# Created:     01/13/2017
# Copyright:   (c) SkyDog 2016
# Licence:     SDS10018
# -----------------------------------------------------------------------------
# TODO:

# FIXME:

# DONE:

# モジュールインポート
import subprocess
from datetime import datetime

import os
import sys
import time
import datetime
import platform

# sysモジュール リロード
reload(sys)

# デフォルトの文字コード 出力
sys.setdefaultencoding("utf-8")

class OpenJTalk:
    """ OpenJTalkクラス """

    def jtalk(talk):
        # Depend on your install folder
        if os.name == "posix":
            open_jtalk=["open_jtalk"]
            mech=["-x","/var/lib/mecab/dic/open-jtalk/naist-jdic"]
            htsvoice=["-m","/usr/share/hts-voice/mei/mei_normal.htsvoice"]

        elif os.name == "nt":
            OPENJTALK_BINPATH = "c:/open_jtalk/bin"
            OPENJTALK_DICPATH = "c:/open_jtalk/dic"
            OPENJTALK_VOICEPATH = "c:/open_jtalk/bin/mei_normal.htsvoice"
            open_jtalk=[OPENJTALK_BINPATH + "/open_jtalk.exe"]
            mech=["-x",OPENJTALK_DICPATH]
            htsvoice=["-m",OPENJTALK_VOICEPATH]

        speed=["-r","1.0"]
        outwav=["-ow","open_jtalk.wav"]
        cmd=open_jtalk+mech+htsvoice+speed+outwav

        # Convert text encoding from utf-8 to shitf-jis
        if os.name == "posix":
            cvt = subprocess.Popen(cmd,stdin=subprocess.PIPE)

        elif os.name == "nt":
            cvt.stdin.write(t.encode("shift-jis"))

        cvt.stdin.write(talk)
        cvt.stdin.close()
        cvt.wait()

        # Play wav audio file with winsound module
        if os.name == "posix":
            aplay = ["aplay","-q","open_jtalk.wav"]
            wr = subprocess.Popen(aplay)

        elif os.name == "nt":
            winsound.PlaySound("open_jtalk.wav", winsound.SND_FILENAME)

    def say_datetime():
        dtt = datetime.now()
        if os.name == "posix":
            text = "%s月%s日、%s時%s分%s秒" % \
                    (dtt.month, dtt.day, dtt.hour, dtt.minute, dtt.second)

        elif os.name == "nt":
            text = u"%s月%s日、%s時%s分%s秒" % \
                    (dtt.month, dtt.day, dtt.hour, dtt.minute, dtt.second)
            print text
        jtalk(text)

def main():
    ojt = OpenJTlk()
    ojt.say_datetime()

if __name__ == "__main__":
    main()
