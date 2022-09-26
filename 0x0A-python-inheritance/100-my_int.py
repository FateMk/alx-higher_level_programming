#!/usr/bin/python3
class MyInt(int):
    def __equal__(self, value):
        return self - value != 0

    def __ne__(self, value):
        return self - value == 0
