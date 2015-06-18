# coding=UTF-8

import locale
import sys
import os
import re
import logging
import tempfile
import argparse

__author__ = 'Shen Jian'

plantuml_jar_file = 'C:\\PortableApps\\plantuml\\plantuml.jar'
plantuml_jar_parameters = ''
pandoc_exe_file = 'C:\\Users\\10016632\\AppData\\Local\\Pandoc\\pandoc.exe'
pandoc_html_parameters = '-S --from=markdown+pipe_tables+yaml_metadata_block --table-of-contents'
pandoc_css_file = 'http://shenjian74.github.io/plantuml-markdown/stylesheets/github.css'
pandoc_reference_docx = ''
delete_temp_file = False

pattern = re.compile("```uml(?P<content>.*)```", re.DOTALL)
os_tempdir = tempfile.gettempdir()
logging.basicConfig(format='[%(filename)s:%(lineno)d] : %(asctime)s : %(levelname)s : %(message)s',
                    level=logging.INFO)


def convert2png(content):
    fp, tmpfilename = tempfile.mkstemp()
    os.write(fp, content)
    os.close(fp)
    cmdline = 'java -jar %s -tpng -charset UTF-8 %s %s' % (plantuml_jar_file, plantuml_jar_parameters, tmpfilename)
    print '$ %s' % cmdline
    os.popen(cmdline)
    if delete_temp_file:
        os.remove(tmpfilename)
    return tmpfilename + ".png"

def chs(string):
    os_encoding = locale.getpreferredencoding()
    default_encoding = "UTF-8"
    if isinstance(string, str):
        try:
            unicode_string = unicode(string, default_encoding)
        except UnicodeDecodeError:
            try:
                unicode_string = unicode(string, os_encoding)
            except UnicodeDecodeError:
                raise
    elif isinstance(string, unicode):
        unicode_string = string
    else:
        raise ValueError("Unknown type.")

    try:
        ret_string = unicode_string.encode(sys.stdout.encoding)
    except UnicodeEncodeError:
        ret_string = unicode_string.encode(default_encoding)
    return ret_string

def main(args=None):

    parser = argparse.ArgumentParser(description='Preprocessing plantuml in markdown file.')
    parser.add_argument("markdown_file", metavar='file', type=file)
    args = parser.parse_args()

    with args.markdown_file:
        file_content = args.markdown_file.read()

    index = 1
    while True:
        script = re.search(pattern, file_content)
        if script is None:
            break
        tmpfilename = convert2png(script.group('content'))
        file_content = re.sub(pattern, lambda s: "![](%s)" % tmpfilename, file_content)
        index += 1

    fp, tmpfilename = tempfile.mkstemp()
    os.write(fp, file_content)
    os.close(fp)
    # cmdline = 'pandoc -S --from=markdown+pipe_tables+yaml_metadata_block ' \
    #           '--reference-docx "%bat_path%zte_reference.docx" ' \
    #           '--css="D:\git@OSC\Workspace\projects\CSS\github.css" ' \
    #           '--table-of-contents -s %p1% -o "%%~df%%~pf%%~nf.docx'
    cmdline = '%s -S %s --css="%s" -s %s -o "%s.html"' % \
              (pandoc_exe_file, pandoc_html_parameters, pandoc_css_file,
               tmpfilename, os.path.normpath(args.markdown_file.name))
    print '$ %s' % cmdline
    os.popen(cmdline)
    cmdline = '%s -S %s --reference-docx "%s" -s %s -o "%s.docx"' % \
              (pandoc_exe_file, pandoc_html_parameters, pandoc_reference_docx,
               tmpfilename, os.path.normpath(args.markdown_file.name))
    print '$ %s' % cmdline
    os.popen(cmdline)
    if delete_temp_file:
        os.remove(tmpfilename)


if __name__ == "__main__":
    main()



