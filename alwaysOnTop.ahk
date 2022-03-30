#NoEnv  ; Recommended for performance and compatibility with future AutoHotkey releases.
; #Warn  ; Enable warnings to assist with detecting common errors.
SendMode Input  ; Recommended for new scripts due to its superior speed and reliability.
SetWorkingDir %A_ScriptDir%  ; Ensures a consistent starting directory.

#SingleInstance Force

AddTitle := "         ¤¤¤¤¤ PINNED ¤¤¤¤¤"

!F12::
if !hWnd := WinExist("ahk_class ConsoleWindowClass")
	return

winactivate, ahk_class ConsoleWindowClass
Winset, Alwaysontop, , A
WinGetActiveTitle, WinTitle
WinGet, hWnd, ID, A


titleNOW = %WinTitle%

if !!InStr(titleNOW, AddTitle) {

    titleNOW := StrReplace(titleNOW,"         ¤¤¤¤¤ PINNED ¤¤¤¤¤", "")
    ;~ WinSetTitle, %titleNOW%
    WinSetTitle, % "ahk_id " hWnd,,  %titleNOW% 
}
else {

    ;~ WinSetTitle, %WinTitle% %AddTitle%
    WinSetTitle, % "ahk_id " hWnd,,  %titleNOW% %AddTitle%
}
    return


!^F12::
titleNOW =
AddTitle := "         ¤¤¤¤¤ PINNED ¤¤¤¤¤"

WinGet,Windows,List
Loop,%Windows% ; in the loop we search for titles with PIN
{
	this_id := "ahk_id " . Windows%A_Index%
	WinGetTitle,this_title,%this_id%
	;~ MsgBox %this_title%
	if !!InStr(this_title, AddTitle) {
        titleNOW =  %this_title%
        titleNOW := StrReplace(this_title,"         ¤¤¤¤¤ PINNED ¤¤¤¤¤", "")
        WinSetTitle, %this_id%,,  %titleNOW%
        WinGet, hWnd, ID, A    
        ;~ MsgBox %titleNOW%
        Winset, Alwaysontop, , %this_id%
		}

}

if (!titleNOW){
    Winset, Alwaysontop, , A
    WinGetActiveTitle, WinTitle
    WinGet, hWnd, ID, A

    titleNOW = %WinTitle%
    WinSetTitle, % "ahk_id " hWnd,,  %titleNOW% %AddTitle%
}

