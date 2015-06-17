__author__ = 'Shen Jian'
# coding=UTF-8

import os
import re
import logging
import tempfile
import argparse

pattern = re.compile("```uml.*```", re.DOTALL)
os_tempdir = tempfile.gettempdir()
logging.basicConfig(format='[%(filename)s:%(lineno)d] : %(asctime)s : %(levelname)s : %(message)s',
                    level=logging.INFO)


def main(args=None):

    parser = argparse.ArgumentParser(description='Preprocessing plantuml in markdown file.')
    parser.add_argument("markdown_file", metavar='file', type=file)
    args = parser.parse_args()
    print args

    with args.markdown_file:
        file_content = args.markdown_file.read()

    index = 1
    while True:
        script = re.search(pattern, file_content)
        if script is None:
            break
        tmpfilename = os.path.join(os_tempdir, 'plantuml_img%d.png' % index)
        file_content = re.sub(pattern, lambda s: "![](%s)" % tmpfilename, file_content)
        index += 1

    fp, tmpfilename = tempfile.mkstemp()
    os.write(fp, file_content)
    os.close(fp)
    print tmpfilename

    # cmdline = 'java -jar plantuml.jar -tpng'
    # result = os.popen(cmdline, 'r')
    # for line in result.readlines():
    #     if find(line, "Cross") != -1:
    #         return atof(split(line)[-1])


if __name__ == "__main__":
    main()



