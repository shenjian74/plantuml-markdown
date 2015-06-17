# plantuml-markdown
parse plantuml tags in markdown (NOT yet complete!)

tags: plantuml markdown

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
1. Download and Install [plantuml](http://www.plantuml.com/)
2. Config the path of [plantuml.jar](http://sourceforge.net/projects/plantuml/files/plantuml.jar/download) in "preprocess.py"
3. Finally, "python preprocess.py"






