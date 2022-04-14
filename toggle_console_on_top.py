bl_info = {
    "name": "toggle console on top",
    "author": "1C0D, HerminOs",
    "version": (1, 1, 2),
    "blender": (2, 90, 0),
    "location": "Window menu",
    "description": "Always open system console on top",
    "category": "System",
    }

"""
For Windows only
-open console/show on top 
-close console
thanks to ErminOs

"""

import bpy
from ctypes import windll

class TOGGLE_OT_console_on_top(bpy.types.Operator):
    """Tooltip"""
    bl_idname = "wm.console_toggle_on_top"
    bl_label = "console toggle always on top"
    
    open_console : bpy.props.BoolProperty()

    def execute(self, context):
        
        GetConsoleWindow = windll.kernel32.GetConsoleWindow
        ShowWindow = windll.user32.ShowWindow
        SwitchToThisWindow = windll.user32.SwitchToThisWindow
        MakeActive = windll.user32.SetActiveWindow
        IsWindowVisible = windll.user32.IsWindowVisible
        hWnd = GetConsoleWindow()

        if self.open_console:
            if IsWindowVisible(hWnd):
                SwitchToThisWindow(hWnd, True) #on Top
                MakeActive(hWnd)
            else:
                ShowWindow(hWnd, 5) # SW_SHOW
                SwitchToThisWindow(hWnd, True) #on Top
        else:
            # if IsWindowVisible(hWnd):
            ShowWindow(hWnd, 0) # SW_HIDE
        return {'FINISHED'}

def draw(self, context):
    layout = self.layout
    console_toggle = "wm.console_toggle_on_top"
    ops = layout.operator(console_toggle, text="Console On/Top")
    ops.open_console=True
    ops = layout.operator(console_toggle, text="Console Off")
    ops.open_console=False

def register():
    bpy.utils.register_class(TOGGLE_OT_console_on_top)
    bpy.types.TOPBAR_MT_window.append(draw)


def unregister():
    bpy.utils.unregister_class(TOGGLE_OT_console_on_top)
    bpy.types.TOPBAR_MT_window.remove(draw)

