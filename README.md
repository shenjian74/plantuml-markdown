---
title:  'plantuml-markdown README'
...

Parse plantuml tags in markdown file, convert markdown to html/docx

Use this block in markdown to include UML image.
	```uml
	......
	```

Use this line to include file content in local disk.
	!INCLUDE "/path/file" 

	

## Preview

![](http://www.plantuml.com:80/plantuml/png/JSox3G8n303GtbEup5NqIOaeaBWA6C2A7HAHE2XdFhSzY0O6U6yn6WP-fvaq2kDCuyhzgG5AGhVNMEyiU9uF4reMHRVACW6YttPzo32qZgNHHGA8SadWZqRAD7uLkfEqMnyqLaobVdo0VvwjrGtt-FeMRm00)

## Example

Markdown

    ### Title3
	#### Title4
	
	line1
	
	line2
	
	```uml
	@startuml
	Alice -> Bob: Authentication Request
	Bob --> Alice: Authentication Response

	Alice -> Bob: Another authentication Request
	Alice <-- Bob: another authentication Response
	@enduml
	```

Show as:

### Title3

#### Title4

line1

line2

![](http://www.plantuml.com:80/plantuml/png/Syp9J4vLqBLJSCfFib9mB2t9ICqhoKnEBCdCprC8IYqiJIqkuGBAAUW2rJY256DHLLoGdrUSoiNbY6fONZvGNP528dP38OfjT7KXgXDngOOO3W00)

## Install	

1. Download and Install [pandoc](https://pandoc.org/installing.html), An old version already in the "prerequisite" directory.
1. Download and Install [graphviz](https://www.graphviz.org/download/), An old version already in the "plantuml" directory.
1. Config some parameters in "preprocess.py"

	* plantuml_jar_file -- Where is [plantuml.jar](http://sourceforge.net/projects/plantuml/files/plantuml.jar/download), An old version already in the "plantuml" directory.
	* plantuml_jar_parameters -- default NULL
	* pandoc_exe_file -- Where is the pandoc execute file
	* pandoc_html_parameters -- pandoc's parameters for html
	* pandoc_css_file -- CSS file for html, see "--css" in [pandoc](http://pandoc.org/README.html)
	* pandoc_reference_docx -- local docx template file, see "--reference-docx" in [pandoc](http://pandoc.org/README.html)

1. Finally, "python preprocess.py [--plantuml-jar /path-to/plantuml.jar] [--reference-docx /path-to/reference.docx] markdown_file"

## Document

* [PlantUML Language Reference Guide](http://www.plantuml.com/PlantUML_Language_Reference_Guide.pdf)






