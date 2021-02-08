# -*- coding: utf8 -*-

import xlsxwriter
import csv
import os
import sys
import datetime
import argparse

# version 1.0
# James M. Tucker, PhD (cand.)
# University of Toronto
# (c) 2019 by James M. Tucker
# Depedencies: xlsxwriter install with `pip3 install xlsxwriter`
# documentation: https://xlsxwriter.readthedocs.io/contents.html

def make_transcriber_notebook(args):
    """
    Create a transcriber xlsx notebook. Each notebook corresponds to a fragment, and contains a transcription 
    along with various other interpreted values. See the README.md for additional details.
    """
    # args
    frag_id = args.frag_id
    roi_file = args.roi_file
    scroll_id = args.scroll_id

    wb_name = str(scroll_id) + "_" + str(frag_id) + '.xlsx'

    ws1_name_chars = 'CHARs'
    ws2_name_rois = 'SIGNs'
    
    with xlsxwriter.Workbook(wb_name) as workbook:
        workbook.set_properties({
            'title': 'This worksheet contains sign(s) and their interepretation for {}'.format(wb_name),
            'subject': 'Edition of Fragment ' + str(frag_id),
            'author': 'James M. Tucker',
            'manager': 'James M. Tucker',
            'category': 'ROI, Digital Editions, Philology',
            'keywords': 'Digital Edition, Transcription, Serekh',
            'comments': 'Created with Python and XLSX Writer by (c) 2019 James M. Tucker'
        })

        # define properties
        workbook.set_custom_property('Checked by', 'James')
        workbook.set_custom_property('Document number', scroll_id)
        workbook.set_custom_property('Reference number', str(frag_id))
        workbook.set_custom_property('Has review', True)
        workbook.set_custom_property('Signed off', False)
        workbook.set_custom_property('Editor', 'James M. Tucker')
        cell_format = workbook.add_format()
    
        # Add worksheet with nam
        chars = workbook.add_worksheet(ws1_name_chars)

        header_labels_chars = [
            {'A1': 'id'},                   #0
            {'B1': 'uni_id'},               #1
            {'C1': 'roi_id'},               #2
            {'D1': 'editors_sigla_id'},     #3
            {'E1': 'word_id'},              #4
            {'F1': 'he_mach'},              #5
            {'G1': 'reading_order'},        #6
            {'H1': 'reading_order_alt'},    #7
            {'I1': 'attr'},                 #8
            {'J1': 'related_to'},           #9
            {'K1': 'is_joined'},            #10
            {'L1': 'kerning'},              #11
            {'M1': 'damaged'},              #12
            {'N1': 'he_human_0'},           #13
            {'O1': 'he_human_1'},           #14
            {'P1': 'he_human_2'},           #15
            {'Q1': 'he_human_3'},           #16
            {'R1': 'line_id'},              #17
            {'S1': 'line_status_int'},      #18
            {'T1': 'line_status_mid'},      #19
            {'U1': 'line_status_end'},      #20
            {'V1': 'commentary'}            #21
        ]

        signs = workbook.add_worksheet(ws2_name_rois)

        header_labels_signs = [
            {'A1': 'roi_id'},               #0
            {'B1': 'iaa_related_to'},       #1
            {'C1': 'pam_related_to'},       #2
            {'D1': 'Label'},                #3
            {'E1': 'Area'},                 #4
            {'F1': 'Mean'},                 #5
            {'G1': 'Min'},                  #4
            {'H1': 'Max'},                  #5
            {'I1': 'BX'},                   #6
            {'J1': 'BY'},                   #7
            {'K1': 'Width'},                #8
            {'L1': 'Height'},               #9
            {'M1': 'Major'},                #10
            {'N1': 'Minor'},                #12
            {'O1': 'Angle'},                #13
            {'P1': 'Circ.'},                #14
            {'Q1': 'AR'},                   #15
            {'R1': 'Round'},                #16
            {'S1': 'Solidity'}              #17
        ]


        row_count = 1
        roi_id = 2

        with open(roi_file, 'rt') as csvfile:
            reader = csv.DictReader(csvfile)
            for item in header_labels_chars:
                for k,v in item.items():
                    chars.write(k, v, cell_format.set_bold(True))
        
            for item in header_labels_signs:
                for k,v in item.items():
                    signs.write(k, v, cell_format.set_bold(True))

            for row in reader:
                signs.write_number(row_count, 0, int(row[' ']))
                chars.write_formula(row_count, 2, str('=SIGNs!' + 'A' + str(roi_id)))
            
                roi_id += 1

                signs.write_string(row_count, 3, str(row['Label']))
                signs.write_number(row_count, 4, int(row['Area']))
                signs.write_number(row_count, 5, float(row['Mean']))
                signs.write_number(row_count, 6, int(row['Min']))
                signs.write_number(row_count, 7, int(row['Max']))
                signs.write_number(row_count, 8, int(row['BX']))
                signs.write_number(row_count, 9, int(row['BY']))
                signs.write_number(row_count, 10, int(row['Width']))
                signs.write_number(row_count, 11, int(row['Height']))
                signs.write_number(row_count, 12, float(row['Major']))
                signs.write_number(row_count, 13, float(row['Minor']))
                signs.write_number(row_count, 14, int(row['Angle']))
                signs.write_number(row_count, 15, float(row['Circ.']))
                signs.write_number(row_count, 16, float(row['AR']))
                signs.write_number(row_count, 17, float(row['Round']))
                signs.write_number(row_count, 18, float(row['Solidity']))

                boolean_list = ['True', 'False']
                damaged_list = ['False', 'True', 'relevant_x', 'relevant_y']
                attr = ['transformed', 'reinked', 'retraced', 'reinked?', 'retraced?', 'supralinear', 'sublinear', 'creased']
                line_stats = ['DAMAGED', 'DAMAGED_STILL_READ', 'NOT_DAMAGED']
                
                # for greek, latin, or syriac add an optional kwarg for the language, otherwise default to hebrew
                chars_opts = ['א', 'ב', 'ג', 'ד', 'ה', 'ו', 'ז', 'ח', 'ט', 'י', 'כ', 'ך', 'ל', 'מ', 'ם', 'נ', 'ן', 'ס', 'ע', 'פ', 'ף', 'צ', 'ץ', 'ק', 'ר', 'ש', 'ת', '◦', 'l', 's', 'm']

                chars.data_validation('I' + str(row_count), {'validate': 'list', 'source': })
                chars.data_validation('K' + str(row_count), {'validate': 'list', 'source': boolean_list})
                chars.data_validation('L' + str(row_count), {'validate': 'list', 'source': boolean_list})
                chars.data_validation('M' + str(row_count), {'validate': 'list', 'source': damaged_list})
                chars.data_validation('S' + str(row_count), {'validate': 'list', 'source': line_stats})
                chars.data_validation('T' + str(row_count), {'validate': 'list', 'source': line_stats})
                chars.data_validation('U' + str(row_count), {'validate': 'list', 'source': line_stats})
                chars.data_validation('N' + str(row_count), {'validate': 'list', 'source': chars_opts})
                chars.data_validation('O' + str(row_count), {'validate': 'list', 'source': chars_opts})
                chars.data_validation('P' + str(row_count), {'validate': 'list', 'source': chars_opts})
                chars.data_validation('Q' + str(row_count), {'validate': 'list', 'source': chars_opts})                                                                                                                                                   
            
                row_count += 1

def main(argv):
    """
    """
    parser = argparse.ArgumentParser()
    parser.add_argument("scroll_id", help="There must be a scroll id", type=str)
    parser.add_argument("frag_id", help="There must be a fragment id", type=str)
    parser.add_argument("roi_file", help="Path to the saved ROI csv", type=str)
    args = parser.parse_args()
    
    make_transcriber_notebook(args)

if __name__ == '__main__':
    main(sys.argv[1:])