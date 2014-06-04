Set oShell = CreateObject ("Wscript.Shell") 
Dim strArgs
strArgs = """F:\BitNami\djangostack-1.4.5-0\python\python.exe"" ""F:\BitNami\djangostack-1.4.5-0\python\Lib\idlelib\idle.py"""
oShell.Run strArgs, 0, false
