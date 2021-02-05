#
#    Copyright (c) 2017 Shane Ambler
#
#  Redistribution and use in source and binary forms, with or without
#  modification, are permitted provided that the following conditions are
#  met:
#
#  * Redistributions of source code must retain the above copyright
#    notice, this list of conditions and the following disclaimer.
#  * Redistributions in binary form must reproduce the above
#    copyright notice, this list of conditions and the following disclaimer
#    in the documentation and/or other materials provided with the
#    distribution.
#
#  THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS
#  "AS IS" AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT
#  LIMITED TO, THE IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR
#  A PARTICULAR PURPOSE ARE DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT
#  OWNER OR CONTRIBUTORS BE LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL,
#  SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT
#  LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES; LOSS OF USE,
#  DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND ON ANY
#  THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT
#  (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE
#  OF THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.
#

# made in response to BSE question -
# https://blender.stackexchange.com/q/95070/935

bl_info = {
    "name": "toggle console on top",
    "author": "1C0D, HerminOs",
    "version": (1, 0, 0),
    "blender": (2, 90, 0),
    "location": "Window menu",
    "description": "Always open system console on top",
    "category": "System",
    }

"""
For Windows only
You can add a shortcut in the window menu
thanks to ErminOs

"""

import bpy
import bpy
from ctypes import windll


def main(context):

    GetConsoleWindow = windll.kernel32.GetConsoleWindow
    ShowWindow = windll.user32.ShowWindow
    SwitchToThisWindow = windll.user32.SwitchToThisWindow
    IsWindowVisible = windll.user32.IsWindowVisible
    hWnd = GetConsoleWindow()
    if IsWindowVisible(hWnd):
        ShowWindow(hWnd, 0) # SW_HIDE
    else:
        ShowWindow(hWnd, 5) # SW_SHOW
        SwitchToThisWindow(hWnd, True) #on Top


class TOGGLE_OT_console_on_top(bpy.types.Operator):
    """Tooltip"""
    bl_idname = "wm.console_toggle_on_top"
    bl_label = "console toggle always on top"

    def execute(self, context):
        
        main(context)
        return {'FINISHED'}

def draw(self, context):
    layout = self.layout
    layout.operator("wm.console_toggle_on_top", text="Toggle Console On Top")

def register():
    bpy.utils.register_class(TOGGLE_OT_console_on_top)
    bpy.types.TOPBAR_MT_window.append(draw)


def unregister():
    bpy.utils.unregister_class(TOGGLE_OT_console_on_top)
    bpy.types.TOPBAR_MT_window.remove(draw)

