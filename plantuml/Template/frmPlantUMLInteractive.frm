VERSION 5.00
Begin {C62A69F0-16DC-11CE-9E98-00AA00574A4F} frmPlantUMLInteractive 
   Caption         =   "PlantUML/Word Interactive"
   ClientHeight    =   8355
   ClientLeft      =   45
   ClientTop       =   375
   ClientWidth     =   20190
   OleObjectBlob   =   "frmPlantUMLInteractive.frx":0000
   StartUpPosition =   1  '所有者中心
End
Attribute VB_Name = "frmPlantUMLInteractive"
Attribute VB_GlobalNameSpace = False
Attribute VB_Creatable = False
Attribute VB_PredeclaredId = True
Attribute VB_Exposed = False


Private Sub CommandButton2_Click()
    FName = "c:\temp\x.txt"
    If Len(tbPlantCode.Text) > 10 Then
        WriteToFile FName, tbPlantCode.Text
        Result = FtpStor(FName, "x.txt")
        Result = FtpRetr("c:\temp\x.png", "x.png")
        

        frmPlantUMLInteractive.imgBox.Picture = LoadPictureGDI("c:\temp\x.png")
        
    End If
End Sub


