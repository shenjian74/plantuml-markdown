# plantuml-markdown
parse plantuml tags in markdown (NOT yet complete!)

For Example:

Markdown:

    # Title1
	## Title2
	
	content
	
	```uml
	@startuml
	Alice -> Bob: Authentication Request
	Bob --> Alice: Authentication Response

	Alice -> Bob: Another authentication Request
	Alice <-- Bob: another authentication Response
	@enduml
	```

Convert to:

# Title1

## Title2

content

![](http://www.plantuml.com:80/plantuml/png/Syp9J4vLqBLJSCfFib9mB2t9ICqhoKnEBCdCprC8IYqiJIqkuGBAAUW2rJY256DHLLoGdrUSoiNbY6fONZvGNP528dP38OfjT7KXgXDngOOO3W00)
	
1. Download and Install [plantuml](http://www.plantuml.com/)
2. Config the path of [plantuml.jar](http://sourceforge.net/projects/plantuml/files/plantuml.jar/download) in "preprocess.py"
3. Finally, "python preprocess.py"

