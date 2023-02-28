# EPICS Teaching Utility

This Python program is designed to streamline processes for UT Dallas EPICS
instructors. This utility relies on the output files of the
[EPICS Team Builder App](https://github.com/UTDallasEPICS/epics-team-builder-web-app)
and [eLearning](https://elearning.utdallas.edu). Using these files, LaTex documents
are created to make teaching EPICS easier.

The program is broken up into two modules:
* A team notes document
* A grade aggregation document

## Setup

The original program was written using Python 3.8.3. I'm unaware of the compatibility
with other Python versions, but no depreciation errors are thrown at the time of 
creating this application.

### Virtual Environment

To set up the application, I recommend first creating a Python virtual
environment using the command line with the following command
(make sure you are in the top level directory of the project).

```bash
# Create virtual environment named 'venv'
python3 -m venv venv
```

You can then activate this environment using one of the following commands

```bash
# Mac/Linux (bash or zsh)
source venv/bin/activate

# Windows Command Prompt (eww)
venv/Scripts/activate.bat

# Windows Power Shell (ew)
venv/Scripts/Activate.ps1
```

For other shells see [the official Python documentation](https://docs.python.org/3.8/library/venv.html).
**You will need to be in this environment to run the program!**

**To exit** the virtual environment use the `deactivate` command.

### Python Dependencies

A requirements file is included for installing dependencies. From within your
virtual environment, run the requirements install command:

```bash
pip install -r requirements.txt
```

### Directory and File Setup

The following is the recommended directory and file structure:
* class_data/
    * grade_files/
      * [eLearning_grade_download_with_notes1].csv
      * [eLearning_grade_download_with_notes2].csv
      * ...
    * student_photos/
      * [studentIDNumber].png
      * [0123456789].png
      * ...
    * eLearning_user_information.csv
    * team_list.xlsx (output from EPICS Team Builder App in CSV or XLSX format)

You can run the `setup_dirs.sh` script to create the directories.
Names fo files in square brackets are unimportant (they can be the default),
although it is beneficial to name the grade files in the order you want them
to be output (they will be alphabetized when running the grade aggregation program)

#### Grade Files

These files are used for the grade aggregation module. They should be in comma
delimited format with comments included for each column.

#### Student Photos

The student photos are used for packaging the notes document for compilation 
with a LaTeX to PDF application. They should be in the format of
[STUDENT_ID_NUMBER].png

##### Downloading Student Photos

The easiest way I have found to download student photos is using FireFox.

1. Open the UTD-Photo Roster under Course Tools in the eLearning Course
Management toolbar (on the left of the page).
2. Type `Ctrl-I` to open the page info window.
3. Select the **media** tab.
4. Scroll down until you see a list of files in the format of ##########.png
   (generally these ID numbers start with 2)
5. Select all the images (click the first one, then `Shift-Click` the last one)
6. Click the **Save As...** button and save the files in the
`class_data/student_photos` directory.

#### Team List

The team list file is required for all modules.
It is considered the source of truth regarding team membership. If this file
is incorrect, the module outputs may be incorrect. As long as the format remains
unchanged from the team builder output, the application should function.

#### eLearning User Information

The eLearning User Information file is used to determine the name of the correct
picture file to put above students names. It should be a comma delimited CSV file
downloaded from eLearning.

# Program Operation

## Team Notes Document

This module creates a document with a page dedicated to each team. Each team
member is listed with their picture above them and lines for writing notes are
given below the team. There is also a table of contents at the beginning.
To create the team notes document run the following command:

```bash
python -m EPICS_util team-notes-sheet
```

This will create a notes document with the default settings
(using the file names and structure shown above). Add the `-h`
argument to get a list of the other arguments. The most used argument will be
the `--document-title` argument. Use it in the following way to add a 
custom title to the document

```bash
python -m EPICS_util team-notes-sheet --document-title "Spring 2023 Team Notes"
```

The output will be a folder named **studnet_info_doc** and a ZIP file of the same name.
The folder contains all the files to compile the LaTeX document into a PDF.
Alternatively, the ZIP file can be uploaded to [Overleaf](https://www.overleaf.com/)
as a new project that will automatically compile. This is the easiest way to
create the files in this program.

## Team Grade Aggregation Document

This module creates a document that aggregates all scores of the given assignments
(in the `class_data/grade_files` folder). The score and comments received are sorted
for each team to easily have a picture of the team's grade history in once place.
To create the team grade aggregation document run the following command:

```bash
python -m EPICS_util aggregate-grades
```

This will create a grade notes document with the default settings
(using the file names and structure shown above). Add the `-h`
argument to get a list of the other arguments. The most used argument will be
the `--document-title` argument. Use it in the following way to add a 
custom title to the document

```bash
python -m EPICS_util aggregate-grades --document-title "Mid-Semester Grade Notes"
```

The output will be a folder named **semester_grade_review** and a ZIP file of the same name.
The folder contains all the files to compile the LaTeX document into a PDF.
Alternatively, the ZIP file can be uploaded to [Overleaf](https://www.overleaf.com/)
as a new project that will automatically compile. This is the easiest way to
create the files in this program.