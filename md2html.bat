@rem convert markdown to html
%~d1
cd %~dp1
python preprocess.py --plantuml-jar plantuml/plantuml.jar --reference-doc reference/reference.docx %1
@IF %ERRORLEVEL% NEQ 0 pause
