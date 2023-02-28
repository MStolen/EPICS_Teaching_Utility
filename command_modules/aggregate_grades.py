import os
import re

from utils.read_spreadsheet import read_spreadsheet
from utils.zip_folder import zip_folder
from utils.safe_make_dirs import safe_make_dirs
from utils.os_copy import os_copy


def aggregate_grades(args):
    with open("src/grades_template.tex") as f:
        document_data = f.read()
    with open("src/grades_section_template.txt") as f:
        section_template = f.read().split('% ')[0]
    with open("src/grades_subsection_template.txt") as f:
        subsection_template = f.read().split('% ')[0]
    team_file = args.team_file
    grade_file_location = args.grade_files
    document_title = args.document_title
    output_dir = args.output_dir_name
    grade_file_list = [os.path.join(grade_file_location, x)
                       for x in os.listdir(grade_file_location)
                       if x.endswith('.csv')]
    grade_file_list = sorted(grade_file_list)
    team_data = read_spreadsheet(team_file)
    team_list = list(team_data["Team"].unique())
    for team in team_list:
        print("Processing Team: {0}".format(team))
        # Get name of first student on team
        student_name = team_data["Student"][team_data[team_data["Team"] == team].first_valid_index()]
        # Convert student name into first and last
        student_name = student_name.split(', ')
        student_first = student_name[1]
        student_last = student_name[0]
        this_section = section_template.format(team_name=team) + "\n\n%%%SECTIONS%%%"
        # print("Team: {0}, Student: {1}, {2}".format(team, student_last, student_first))
        # output_file.write(team)
        for grade_file in grade_file_list:
            grade_sheet = read_spreadsheet(grade_file)
            score_col_name = [column for column in grade_sheet.columns if 'Score' in column][0]
            assignment_name = score_col_name.split(' [')[0]
            print("-- Assignment: {0}".format(assignment_name))
            student_index = (grade_sheet["First Name"] == student_first) & (grade_sheet["Last Name"] == student_last)
            score_col = grade_sheet[score_col_name][student_index]
            assignment_score = score_col.to_list()[0]
            assignment_comments = grade_sheet["Feedback to Learner"][student_index].to_list()[0]
            assignment_comments = re.sub(r"(<p>)", r'{}'.format("\n\n"), assignment_comments)
            assignment_comments = re.sub(r"<b>", r'\\textbf{', assignment_comments)
            assignment_comments = re.sub(r"<i>", r'\\textit{', assignment_comments)
            assignment_comments = re.sub(r"</.>", r'{}'.format('}'), assignment_comments)
            assignment_comments = re.sub(r'#', r'\\#', assignment_comments)
            # output_file.write("{0} - {1}\n{2}\n".format(assignment_name, assignment_score, assignment_comments))
            # print("{0} - {1}\n{2}\n".format(assignment_name, assignment_score, assignment_comments))
            this_subsection = subsection_template.format(assignment_name=assignment_name,
                                                         assignment_score=assignment_score,
                                                         assignment_comments=assignment_comments) + "\n\n%%%SUBSECTIONS%%%"
            this_subsection = this_subsection.split("\\")
            this_subsection = r"\\".join(this_subsection)
            this_section = re.sub(r"(%%%SUBSECTIONS%%%)", r'{}'.format(this_subsection), this_section)
            # print(this_section)
        this_section = this_section.split("\\")
        this_section = r"\\".join(this_section)
        document_data = re.sub(r"(%%%SECTIONS%%%)", r'{}'.format(this_section), document_data)
    document_data = re.sub(r"(<<<TITLE>>>)", r'{}'.format(document_title), document_data)
    safe_make_dirs(f"products/{output_dir}")
    with open(f"products/{output_dir}/main.tex", 'w') as f:
        f.write(document_data)
    os_copy("src/epics_docs.cls", f"products/{output_dir}/epics_docs.cls")
    zip_folder(f"products/{output_dir}", f"products/{output_dir}.zip")
    return
