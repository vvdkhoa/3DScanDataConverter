' https://superuser.com/questions/455364/how-to-create-a-shortcut-using-a-batch-script
' 
Set oWS = WScript.CreateObject("WScript.Shell")
'
' Create desktop shortcut path
strDesktop = oWS.SpecialFolders("Desktop")
sLinkFile = strDesktop + "\DataConverter.LNK"
'
' Get absolute path from Relative path
strBatFile ="ScanDataConverter.LNK"
dim fso, fullPathToBat
set fso = CreateObject("Scripting.FileSystemObject")
fullPathToBat = fso.GetAbsolutePathName(strBatFile)
'
' Create shortcut
Set oLink = oWS.CreateShortcut(sLinkFile)
    oLink.TargetPath = fullPathToBat
 '  oLink.Arguments = ""
 '  oLink.Description = "MyProgram"   
 '  oLink.HotKey = "ALT+CTRL+F"
 '  oLink.IconLocation = "C:\Program Files\MyApp\MyProgram.EXE, 2"
 '  oLink.WindowStyle = "1"   
 '  oLink.WorkingDirectory = "C:\Program Files\MyApp"
oLink.Save
