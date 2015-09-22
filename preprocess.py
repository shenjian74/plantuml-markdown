# coding=UTF-8

plantuml_jar_file = 'plantuml/plantuml.jar'
plantuml_jar_parameters = ''
pandoc_exe_file = 'pandoc'
pandoc_html_parameters = '-S --from=markdown_github+table_captions+yaml_metadata_block --table-of-contents'
pandoc_css_file = 'http://shenjian74.github.io/plantuml-markdown/stylesheets/github.css'
pandoc_reference_docx = ''
delete_temp_file = True

import locale
import sys
import os
import re
import logging
import tempfile
import argparse

pattern_uml = re.compile("\n```uml(?P<content>.*?)\n```", re.DOTALL)
pattern_include = re.compile("!INCLUDE \"(?P<include_file>.*?)\"", re.DOTALL)
os_tempdir = tempfile.gettempdir()
logging.basicConfig(format='[%(filename)s:%(lineno)d] : %(asctime)s : %(levelname)s : %(message)s',
                    level=logging.INFO)


def print_popen_result(result):
    no_error = True
    for line in result:
        logging.error(line)
        no_error = False
    if no_error:
        logging.info('Success.')


def convert2png(content):
    global plantuml_jar_file

    fp1, tmpfilename1 = tempfile.mkstemp()
    os.write(fp1, content)
    os.close(fp1)
	
    cmdline = 'java -jar %s -tpng -charset UTF-8 %s %s 2>&1' % (plantuml_jar_file, plantuml_jar_parameters, tmpfilename1)
    logging.info('$ %s' % cmdline)
    print_popen_result(os.popen(cmdline))
    if delete_temp_file:
        os.remove(tmpfilename1)
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
        if sys.stdout.encoding:
            ret_string = unicode_string.encode(sys.stdout.encoding)
        else:
            ret_string = unicode_string.encode(default_encoding)
    except UnicodeEncodeError:
        ret_string = unicode_string.encode(default_encoding)
    return ret_string


def change_file_ext(origin, new_ext):
    if len(os.path.basename(origin).split('.')) == 1:
        return origin+'.'+new_ext

    parts = origin.split('.')
    count = len(parts)
    dest_filename = ''
    for i in xrange(count-1):
        dest_filename += parts[i] + '.'
    dest_filename += new_ext
    return dest_filename


def main(args=None):
    global plantuml_jar_file

    parser = argparse.ArgumentParser(description='Preprocessing plantuml in markdown file.')
    parser.add_argument("markdown_file", metavar='file', type=file)
    parser.add_argument("--reference-docx", type=file, help="the reference docx file used by pandoc", required=False)
    parser.add_argument("--plantuml-jar", type=file, help="the plantuml jar file", required=False)
    args = parser.parse_args()

    with args.markdown_file:
        file_content = args.markdown_file.read()
    if args.reference_docx:
        args.reference_docx.close()
        pandoc_reference_docx = args.reference_docx.name
    if args.plantuml_jar:
        args.plantuml_jar.close()
        plantuml_jar_file = args.plantuml_jar.name

    while True:
        script = re.search(pattern_include, file_content)
        if script is None:
            break
        filename1 = script.group('include_file')
        logging.debug(filename1)
        if os.path.exists(filename1):
		    with open(filename1, "rt") as finc:
			    file_content = re.sub(pattern_include, finc.read(), file_content, count=1)
        else:
            file_content = re.sub(pattern_include, "[File:\"%s\" not found]" % filename, file_content, count=1)

    while True:
        script = re.search(pattern_uml, file_content)
        if script is None:
            break
        logging.debug(script.group('content'))
        filename2 = convert2png(script.group('content'))
        if os.path.exists(filename2):
			file_content = re.sub(pattern_uml, lambda s: "![](%s)" % filename2, file_content, count=1)
        else:
            file_content = re.sub(pattern_uml, "", file_content, count=1)

    global fp2
    global tmpfilename
    fp2, tmpfilename = tempfile.mkstemp(suffix='.md', text=True)
    os.write(fp2, file_content)
    os.close(fp2)

    cmdline = '%s -S %s --css="%s" -s %s -o "%s" 2>&1' % \
              (pandoc_exe_file, pandoc_html_parameters, pandoc_css_file,
               tmpfilename, os.path.normpath(change_file_ext(args.markdown_file.name, 'html')))
    logging.info('$ %s' % chs(cmdline))
    print_popen_result(os.popen(cmdline))

    cmdline = '%s -S %s' % (pandoc_exe_file, pandoc_html_parameters)
    if len(pandoc_reference_docx):
        cmdline += ' --reference-docx="%s"' % pandoc_reference_docx
    cmdline += ' -s %s -o "%s" 2>&1' % (tmpfilename,
            os.path.normpath(change_file_ext(args.markdown_file.name, 'docx')))
    logging.info('$ %s' % chs(cmdline))
    print_popen_result(os.popen(cmdline))

    if delete_temp_file:
        os.remove(tmpfilename)


if __name__ == "__main__":
    main()



