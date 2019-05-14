import win32api, win32con, win32gui


def click(x,y):
    win32api.SetCursorPos((x,y))
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,x,y,0,0)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,x,y,0,0)


def next():
    lista = win32gui.GetCursorPos()
    click(lista[0], lista[1])
    print(lista[0], lista[1])
