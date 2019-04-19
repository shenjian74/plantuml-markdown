@rem convert markdown to html
%~d1
cd %~dp1
python %~dp0preprocess.py --plantuml-jar %~dp0plantuml/plantuml.jar --reference-doc %~dp0reference/reference.docx %1
@IF %ERRORLEVEL% NEQ 0 pause
