import pdfkit
import json
import argparse
import base64


parser = argparse.ArgumentParser(description='Create letter worksheets')
parser.add_argument('--input', help='Input file name Eg. --input=sample.json', required=True)
args = vars(parser.parse_args())
options = {
    'page-size':'A4',
    'dpi':400,
    'encoding':'utf-8', 
    'margin-top':'0cm',
    'margin-bottom':'0cm',
    'margin-left':'0cm',
    'margin-right':'0cm',
    'disable-smart-shrinking': ''
}
with open(args['input']) as input_file:
    data = json.load(input_file)
    for json_record in data:
        with open(json_record['template']) as template_file:
            content = template_file.read()
            for key in json_record:
                if key.startswith("img_"):
                    with open(json_record[key], 'rb') as image_file:
                        base64_str = base64.b64encode(image_file.read())
                        replace = "{{{}}}".format(key.upper())
                        content = content.replace(replace, str(base64_str.decode('utf-8')))
                else:
                    replace = "{{{}}}".format(key.upper())
                    content = content.replace(replace, json_record[key])
        file_name = str(json_record['worksheet_id_val']) +"_"+json_record['file_out']+""+".pdf"
        pdfkit.from_string(content, file_name, options=options)
