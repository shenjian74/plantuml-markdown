__author__ = 'Shen Jian'
# coding=UTF-8

import os
import re
import logging
import tempfile
import argparse
from platform import popen

pattern = re.compile("```uml(?P<content>.*)```", re.DOTALL)
os_tempdir = tempfile.gettempdir()
logging.basicConfig(format='[%(filename)s:%(lineno)d] : %(asctime)s : %(levelname)s : %(message)s',
                    level=logging.INFO)


def convert2png(content, filename):
    fp, tmpfilename = tempfile.mkstemp()
    os.write(fp, content)
    os.close(fp)
    cmdline = 'java -jar plantuml.jar -tpng %s' % tmpfilename
    print 'cmd:%s' % cmdline
    result = os.popen(cmdline, 'r')
    print result.readlines()
    os.remove(tmpfilename)

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
        convert2png(script.group('content'), tmpfilename)
        file_content = re.sub(pattern, lambda s: "![](%s)" % tmpfilename, file_content)
        index += 1

    fp, tmpfilename = tempfile.mkstemp()
    os.write(fp, file_content)
    os.close(fp)
    # cmdline = 'pandoc -S --from=markdown+pipe_tables+yaml_metadata_block ' \
    #           '--reference-docx "%bat_path%zte_reference.docx" ' \
    #           '--css="D:\git@OSC\Workspace\projects\CSS\github.css" ' \
    #           '--table-of-contents -s %p1% -o "%%~df%%~pf%%~nf.docx'
    cmdline = 'pandoc -S --from=markdown+pipe_tables+yaml_metadata_block --css="github.css" ' \
              '--table-of-contents -s %s -o output.html' % tmpfilename
    print cmdline
    lines = os.popen(cmdline, 'r')
    print result.readlines()
    os.remove(tmpfilename)


if __name__ == "__main__":
    main()



