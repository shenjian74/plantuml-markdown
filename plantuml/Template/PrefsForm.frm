VERSION 5.00
Begin {C62A69F0-16DC-11CE-9E98-00AA00574A4F} PrefsForm 
   Caption         =   "PlantUML Preferences (Word add-in)"
   ClientHeight    =   3840
   ClientLeft      =   45
   ClientTop       =   375
   ClientWidth     =   9090
   OleObjectBlob   =   "PrefsForm.frx":0000
   StartUpPosition =   1  '所有者中心
End
Attribute VB_Name = "PrefsForm"
Attribute VB_GlobalNameSpace = False
Attribute VB_Creatable = False
Attribute VB_PredeclaredId = True
Attribute VB_Exposed = False




Private Sub btnVectorGraphics_Click()
    If PrefsForm.btnVectorGraphics.Caption = "ON" Then
        PrefsForm.btnVectorGraphics.Caption = "OFF"
    Else
        PrefsForm.btnVectorGraphics.Caption = "ON"
    End If
End Sub

Private Sub btnFTP_Click()
      If PrefsForm.btnFTP.Caption = "ON" Then
        PrefsForm.btnFTP.Caption = "OFF"
    Else
        PrefsForm.btnFTP.Caption = "ON"
    End If
End Sub

Private Sub okButton_Click()
    PrefsForm.Hide
End Sub
