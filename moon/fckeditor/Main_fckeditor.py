# -*- coding: utf-8 -*-
import os
import fckeditor.fckeditor_version
import fckeditor.fckeditor_dangerfile



def exec(URL):
    fckeditor.fckeditor_version.attack(URL)
    fckeditor.fckeditor_dangerfile.attack(URL)





if __name__ == "__main__":
    exec()
