#!/usr/bin/env python
#coding: utf-8
import cmd
from keyboard import keyboardDetect
from logger import logger
import sys
reload(sys)

sys.setdefaultencoding("utf-8")

__author__ = 'Huang xiongbiao(billo@qq.com)'

class CLI(cmd.Cmd):

    def __init__(self):
        cmd.Cmd.__init__(self)
        self.intro = "Tickeys v0.0.1 - Linux\nType 'help' for help"
        self.prompt = ">>> "
        self.detecter = keyboardDetect()
        self.detecter.startDetecting()
        self.volume = 100.0
        self.pitch = 10.0
        self.style = 'bubble'


    def default(self, line):
        print "Command '%s' is invalid, try 'help'" % line

    def help_setstyle(self):
        print "Set style, change the sound's effect"

    def do_setstyle(self, arg):
        style_index = raw_input("Input the effect style (0:bubble 1:mechanical 2:sword 3:typewriter) you want:")
        style_list = ['bubble', 'mechanical', 'sword', 'typewriter']

        try:
            style_index = int(style_index)
            assert(0 <= style_index <= 3)
        except Exception:
            print "Input must between 0~3!!"
            return

        self.style = style_list[style_index]
        self.detecter.setStyle(self.style)

    def help_setvol(self):
        print "Set volume, input the volume you want"

    def do_setvol(self, arg):
        volume = raw_input("Input the volume(0~100) you want:")

        try:
            volume = float(volume)
            assert(0 <= volume <= 100)
        except Exception:
            print "Volume must between 0~100!!"
            return

        self.volume = volume
        self.detecter.setVolume(self.volume/100.0)

    def help_getvol(self):
        print "Get the volume"

    def do_getvol(self, arg):
        print self.volume

    def help_setpitch(self):
        print "Set pitch, input the pitch you want"

    def do_setpitch(self, arg):
        pitch = raw_input("Input the pitch(0~20, default 10) you want:")

        try:
            pitch = float(pitch)
            assert(0 <= pitch <= 20)
        except Exception:
            print "Pitch must between 0~20!!"
            return

        self.pitch = pitch
        self.detecter.setPitch(self.pitch/10.0)

    def help_getpitch(self):
        print "Get the pitch"

    def do_getpitch(self, arg):
        print self.pitch

    def help_getinfor(self):
        print "Get tickeys' sound effect, volume and pitch"

    def do_getinfor(self, arg):
        print "Sound effect: %s  Volume: %s  Pitch: %s" % (self.style, self.volume, self.pitch)

    def do_quit(self, arg):
        self.detecter.stopDetecting()
        sys.exit(0)
        return True


if __name__ == "__main__":
    cli = CLI()
    cli.cmdloop()