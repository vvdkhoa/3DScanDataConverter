' https://superuser.com/questions/455364/how-to-create-a-shortcut-using-a-batch-script
' 
Set oWS = WScript.CreateObject("WScript.Shell")
'
' Create desktop shortcut path
strDesktop = oWS.SpecialFolders("Desktop")
sLinkFile = strDesktop + "\ScanÉfÅ[É^ïœä∑.LNK"
'
' Get absolute path of bat file
strBatFile ="Scripts\ScanDataConverter.bat"
dim fso, fullPathToBat
set fso = CreateObject("Scripting.FileSystemObject")
fullPathToBat = fso.GetAbsolutePathName(strBatFile)
'
'Get absolute IconLocation path
strIconLocation = "Scripts\Icons\icon.ico"
fullPathToIconLocation = fso.GetAbsolutePathName(strIconLocation)
'
'Get absolute WorkingDirectory path
strWorkingDirectory = "Scripts\"
fullPathToWorkingDirectory = fso.GetAbsolutePathName(strWorkingDirectory)
'
' Create shortcut
Set oLink = oWS.CreateShortcut(sLinkFile)
    oLink.TargetPath = fullPathToBat
 '  oLink.Arguments = ""
 '  oLink.Description = "MyProgram"   
 '  oLink.HotKey = "ALT+CTRL+F"
 '  oLink.IconLocation = "C:\Program Files\MyApp\MyProgram.EXE, 2"
    oLink.IconLocation = fullPathToIconLocation
 '  oLink.WindowStyle = "1"   
    oLink.WorkingDirectory = fullPathToWorkingDirectory
oLink.Save
