# Transcription Notebook

____

# License

<a rel="license" href="http://creativecommons.org/licenses/by-nc-sa/4.0/"><img alt="Creative Commons License" style="border-width:0" src="https://i.creativecommons.org/l/by-nc-sa/4.0/88x31.png" /></a><br />This work is licensed under a <a rel="license" href="http://creativecommons.org/licenses/by-nc-sa/4.0/">Creative Commons Attribution-NonCommercial-ShareAlike 4.0 International License</a>.

© 2019 James M. Tucker
____

# Description
While it is feasible to create a web based front-end to facilitate the process of transcription, it is equally possible to use existing software, as is the case here. Thus, the excel notebook is used for three reasons:
1. The cost to engineer a web-based front-end is not trivial;
2. The Excel file ensures data accuracy at several levels, thus enforcing best philological practices;
3. Processing data in an Excel format is extensively supported in languages such as Perl, Python, and JavaScript.

The  The following information structure facilitates a careful analysis of ancient artefacts, either lapidary and/or non-lapidary and in whatever language.

## Create a Notebook
The `create_trans.py` script generates a working notebook. To run this script, navigate to `~/DSS_Editions/transcriptions/` in your terminal. The script takes three arguments:
1. frag_id
2. roi_file
3. scroll_id

The `frag_id` is any id you assign to the artefact; thus, it is relative to whatever id you decide. What is more important for the script, however, is the `roi_file`. A `roi_id` file designates a Region of Interest (roi) on an image. I discussed this method some years ago in two conference presentations. I have made available the lecture from one of these conferences [here](https://www.academia.edu/7290280/Digital_Editions_of_the_Scrolls_and_Fragments_of_the_Judaean_Desert_Preliminary_Thoughts). The `roi_id` can be generated from either manual tagging of an artifact or by Computer Vision tools. Given the complexity and fragmentary status of the Judaean Desert fragments, both manual and computer vision tools are necessary (see below for further information about `roi_id`). Lastly, `scroll_id` is also a relative designation.

### Example
As an example, the following bash command could be used to generate a transcription notebook. Assuming you are in the transcriptions directory:

```
python3 create_trans.py 001 roi.csv 001
```

## Structure of the Notebook
The notebook is structured into two worksheets: `CHARs` and `SIGNs`.

The rationale to make two worksheets is as follows. A digtial edition is fundamentally the "[interpretation of ancient media into new media](https://www.academia.edu/37560923/Material_Philology_and_Digital_Editions_Charting_a_Way_Forward)". Thus, any digital edition today is fundamentally built around high-resolution images of ancient artefacts. Once an image has been marked up with `region of interests` (= `rois`), one then has to provide a definition of aforedesignated rois. Once the specifications of the `rois` are made, it is no longer necessary to have this data primary. Thus, the `roi` specifications are placed in the `SIGNs` worksheet, and the `CHARs` workheet now comes into focus. Each worksheet is hereby explained in terms of their definitions and datatypes:

### The SIGNs Worksheet

The following fields are located on the `SIGNs` worksheet:

* `roi_id`:
  * datatype = `INT`
  * definition = a segmented portion of a source image (normally in a a linear development of ids for the `rois`, thus rois += 1)

* `iaa_related_to`:
  * datatype = `INT` (id of of your image file, if you are storing your files in a database, otherwise change datatype to `VARCHAR` and use the filename)
  * definition = the source from which the `rois` were annotated/computed

* `pam_related_to`:
  * datatype = `INT` (see datatype above for `iaa_related_to`)
  * definition = see above under `iaa_related_to`

* `label`:
  * datatype = `VARCHAR`
  * definition = file source from which the `rois` were generated. This is automatically generated from Fiji, and reduplicates data from `iaa_related_to` or `pam_related_to`. Depending on further datamunging desires, this is not necessary, but it is preserved nonetheless.

* `Area`:
  * datatype = `INT`
  * definition = the area of the segmented roi


* `Mean`:
  * datatype = `FLOAT`
  * definition = Mean grey value (cf. [30.7](https://imagej.nih.gov/ij/docs/guide/146-30.html))

* `Min`:
  * datatype = `INT`
  * definition = Min grey value (cf. [30.7](https://imagej.nih.gov/ij/docs/guide/146-30.html))

* `Max`:
  * datatype = `INT`
  * definition = Max of grey value (cf. [30.7](https://imagej.nih.gov/ij/docs/guide/146-30.html))

* `BX`:
  * datatype = `INT`
  * definition = x-coordinate of bounding rectangle (cf. [30.7](https://imagej.nih.gov/ij/docs/guide/146-30.html))

* `BY`:
  * datatype = `INT`
  * definition = y-coordinate of bounding rectangle (cf. [30.7](https://imagej.nih.gov/ij/docs/guide/146-30.html))

* `Width`:
  * datatype = `INT`
  * definition = width of bounding rectangle (cf. [30.7](https://imagej.nih.gov/ij/docs/guide/146-30.html))

* `Height`:
  * datatype = `INT`
  * definition = height of bounding rectangle (cf. [30.7](https://imagej.nih.gov/ij/docs/guide/146-30.html))

* `Major`:
  * datatype = `FLOAT`
  * definition = For computational reasons but not necessary if not desired (cf. [30.7](https://imagej.nih.gov/ij/docs/guide/146-30.html))

* `Minor`:
  * datatype = `FLOAT`
  * definition = For computational reasons but not necessary if not desired (cf. [30.7](https://imagej.nih.gov/ij/docs/guide/146-30.html))

* `Angle`:
  * datatype = `FLOAT`
  * definition = Since the methodology ensures that transformations are always understood as interpretations, the need to regress to the original image is therefore crucial. This, however, complicates digital palaeographical practices. To correct this, this column centers the character to the angle of the dry-line.

* `Circ.`:
  * datatype = `FLOAT`
  * definition = Shape descriptor (cf. [30.7](https://imagej.nih.gov/ij/docs/guide/146-30.html)); Not necessary in most cases.

* `AR`:
  * datatype = `FLOAT`
  * definition = Shape descriptor (cf. [30.7](https://imagej.nih.gov/ij/docs/guide/146-30.html)); Not necessary in most cases.

* `Round`:
  * datatype = `FLOAT`
  * definition = Shape descriptor (cf. [30.7](https://imagej.nih.gov/ij/docs/guide/146-30.html)); Not necessary in most cases.

* `Solidity`:
  * datatype = `FLOAT`
  * definition = Shape descriptor (cf. [30.7](https://imagej.nih.gov/ij/docs/guide/146-30.html)); Not necessary in most cases.

### CHARs

The following fields are located on the `CHARs` worksheet:

* `id`:
  * datatype = `INT`
  * definition = for database purposes, leave blank

* `uni_id`:
  * datatype = `INT`
  * definition = a unique id assigned to every `roi`; again for database purposes so leave it blank

* `roi_id`:
  * datatype = `INT`
  * definition = for [Fiji](https://imagej.nih.gov/ij/docs/guide/146.html) datafile; not necessary if using apart from Fiji

* `editors_sigla_id`:
  * datatype = `INT`
  * definition = All of the Judean Desert fragments have been published. Either create an index of these and use the numerical index id, or simply convert field to `VARCHAR` and use a sigla (e.g., `4Q51_1_b`)

* `word_id`:
  * datatype = `INT`
  * definition = Use the word_id from Accordance/QWB; if desired to link with Accordance in a Python Jupyter Notebook (example coming soon!)

* `he_mach`:
  * datatype = `INT`
  * definition = This is generated from a Machine Learning Algorithm. Leave blank and/or ignore.

* `reading_order`:
  * datatype = `INT`
  * definition = A sequence of numbers to specify the reading order of the chars.

* `reading_order_alt`:
  * datatype = `INT`
  * definition = An alternate sequence of numbers to specify the reading order of the chars.; if more than two, iterate to the nth occasion by simply adding a column.

* `attr`:
  * datatype = `ENUM` (transformed, reinked, reinked?, retraced, retraced?, supralinear, sublinear, creased)
  * definition = This field captures __palaeographical__ attributes of a character

* `related_to`:
  * datatype = `INT`
  * definition = If a character, e.g., relates to a lacuna or is partially damaged by a larva hole, then link the two ids here (roi_ids); these can be computed and properly related into their associated tables later. Use a standard separator for multiple ids (e.g., 40-41-39, 40,41,39, or 40.41.39) [no need to be consistent, a script can detect the separator]

* `is_joined`:
  * datatype = `TINYINT`
  * definition = More than one sign makes the char, based on a palaeographical _conclusion_. If so, associate specify it is joined. _N.B.: If a char is joined on the basis on two or more signs, then the reading_order is the same for all chars!_

* `kerning`:
  * datatype = `TINYINT`
  * definition = Is the char under question kerned with the character adjacent to its writing direction? If so, mark with 1.

* `damaged`:
  * datatype = `ENUM` (TRUE, FALSE, RELEVANT_X [or *_W], RELEVANT_Y [or *_H])
  * definition = Is the char under question damaged by either material causes or severe surface wear? If so, mark with 1. If, however, the width or height of the character is still believed to be relevant for font statistics, then designate which axis is still potentially undamaged. This is a preliminary decision. The font algorithm can run further metrics against the roi and include in the [Font Report](https://jamesmtucker.com). N.B.: The font algorithm is not yet published, but will be made available at the above link in due time.

* `he_human_0`:
  * datatype = `VARCHAR`
  * definition = Define the sign with a char. Options are:
    - range of chars: א-ת;
    - ◦: readings are made on a fragment by fragment basis, without resorting to coincident text. Thus, use this siglum to designate an indeterminate character. Again, this is defined in relation to _palaeographical analysis_.;
    - s: scribal mark (describe in commentary);
    - and m: material damage (descirbe in commentary)

* `he_human_1`:
  * datatype = `VARCHAR`
  * definition = Define the sign with a char. Options are:
    - range of chars: א-ת;
    - ◦: readings are made on a fragment by fragment basis, without resorting to coincident text. Thus, use this siglum to designate an indeterminate character. Again, this is defined in relation to _palaeographical analysis_.;
    - s: scribal mark (describe in commentary);
    - and m: material damage (descirbe in commentary)

* `he_human_2`:
  * datatype = `VARCHAR`
  * definition = Define the sign with a char. Options are:
    - range of chars: א-ת;
    - ◦: readings are made on a fragment by fragment basis, without resorting to coincident text. Thus, use this siglum to designate an indeterminate character. Again, this is defined in relation to _palaeographical analysis_.;
    - s: scribal mark (describe in commentary);
    - and m: material damage (descirbe in commentary)

* `he_human_3`:
  * datatype = `VARCHAR`
  * definition = Define the sign with a char. Options are:
    - range of chars: א-ת;
    - ◦: readings are made on a fragment by fragment basis, without resorting to coincident text. Thus, use this siglum to designate an indeterminate character. Again, this is defined in relation to _palaeographical analysis_.;
    - s: scribal mark (describe in commentary);
    - and m: material damage (descirbe in commentary)

* `line_id`:
  * datatype = `INT`
  * definition = Line number on the fragment itself.

* `line_status_int`:
  * datatype = `ENUM` (DAMAGED, DAMAGED_STILL_READ, NOT_DAMAGED)
  * definition = Designate the status of the beginning, middle, and end of line.

* `line_status_mid`:
  * datatype = `ENUM` (DAMAGED, DAMAGED_STILL_READ, NOT_DAMAGED)
  * definition = Designate the status of the beginning, middle, and end of line.

* `line_status_end`:
  * datatype = `ENUM` (DAMAGED, DAMAGED_STILL_READ, NOT_DAMAGED)
  * definition = Designate the status of the beginning, middle, and end of line.

* `commentary`:
  * datatype = `VARCHAR`
  * definition = If you desire to clarify your decisions on the character level. Commentary for columns, sheets, and scrolls can be found/located elsewhere.
