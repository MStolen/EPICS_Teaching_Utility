import pathlib

import re
import argparse
import os
from utils.read_spreadsheet import read_spreadsheet
from utils.os_copy import os_copy
from utils.safe_make_dirs import safe_make_dirs
from utils.zip_folder import zip_folder


def create_info_sheet(args):
    # TODO Add better comments
    # Load in team member data
    team_file = args.team_file
    student_file = args.student_info_file
    document_title = args.document_title
    output_dir = args.output_dir_name
    image_location = args.image_location
    team_data = read_spreadsheet(team_file)
    student_data = read_spreadsheet(student_file)

    # Read in latex template
    with open("src/notes_template.tex") as f:
        tex_data = f.read()

    # Read in section template
    with open("src/notes_section_template.txt") as f:
        section_template = f.read()
    section_template = section_template.split('%')[0]

    # Create dictionary of team member lists
    team_sets = dict()
    for team in team_data["Team"]:
        team_sets[team] = list(zip(team_data["Student"][team_data["Team"] == team].tolist(),
                                   team_data["Email"][team_data["Team"] == team].tolist()))

    for team in team_sets:
        num_students = len(team_sets[team])
        column_width = round(5.4/num_students, 1)
        paragraph_string = "p{{{0:02.1f}in}}".format(column_width)*num_students
        image_string = ""
        name_string = ""
        extra_par = "&"*(num_students-1)

        for (student, email) in team_sets[team]:
            student = student.split(', ')
            first_name = student[1]
            last_name = student[0]
            netid = email.split('@')[0]
            student_ind = list(set(student_data.index[student_data["Username"] == netid]))
            # student_ind = list(set(student_data.index[student_data["Last Name"] == last_name]) &
            #                    set(student_data.index[student_data["First Name"] == first_name]))
            # student_ind = student_data.index[student_data[""]]
            # print(student_ind)
            id_num = int(student_data["Student ID"][student_ind])
            if os.path.isdir(image_location):
                if os.path.isfile(os.path.join(image_location, f"{id_num}.png")):
                    image_string += "\\includegraphics[width={0:02.1f}in]{{StudentPictures/{1}.png}} &".format(
                        column_width, id_num)
                else:
                    image_string += "\\includegraphics[width={0:02.1f}in]{{NoImage.png}} &".format(
                        column_width)
            else:
                image_string += "\\includegraphics[width={0:02.1f}in]{{StudentPictures/{1}.png}} &".format(column_width,
                                                                                                           id_num)
            name_string += first_name + ' ' + last_name + ' & '
        image_string = image_string[0:-2]
        name_string = name_string[0:-3]
        this_section = section_template.format(team_name=' '.join([word for word in team.split(' ')[2:]]),
                                               paragraph_string=paragraph_string,
                                               image_string=image_string,
                                               name_string=name_string,
                                               extra_par=extra_par,
                                               num_stud=num_students,
                                               mentor_name='') + "\n\n%%%SECTIONS%%%"
        this_section = this_section.split("\\")
        this_section = r"\\".join(this_section)
        tex_data = re.sub(r"(%%%SECTIONS%%%)", r'{}'.format(this_section), tex_data)
    tex_data = re.sub(r"(<<<TITLE>>>)", r'{}'.format(document_title), tex_data)
    # print(tex_data)

    safe_make_dirs(f'products/{output_dir}')
    os_copy("src/epics_docs.cls", f"products/{output_dir}/epics_docs.cls")
    os_copy("src/NoImage.png", f"products/{output_dir}/NoImage.png")
    if image_location:
        os_copy(image_location, f"products/{output_dir}/StudentPictures")
    elif pathlib.Path('class_data/student_photos').is_dir():
        os_copy('class_data/student_photos', f"products/{output_dir}/StudentPictures")
    with open(f"products/{output_dir}/main.tex", 'w') as f:
        f.write(tex_data)
    zip_folder(os.path.join("products", f"{output_dir}"), f"products/{output_dir}.zip")
    return

# team_name, paragraph_string, image_string, extra_par, mentor_name
# paragraph_string = "p{Xin}" the same number of times as there are team members
# image_string = "\includegraphics[width=Xin]{photo_path/ID_NUM.png} &" where width same as above once for each student
# name_string = "STUDENT NAME & FIRST LAST & ..."
# extra_par = "&" repeated 1- num students
# num_stud = number of students


if __name__ == "__main__":
    parser = argparse.ArgumentParser("Test this module")
    parser.add_argument('--team-file', default="class_data/team_list.csv")
    parser.add_argument('--student-info-file', default="class_data/eLearning_user_information.csv")
    parser.add_argument('--document-title', default="EPICS Class List")
    args_in = parser.parse_args()
    create_info_sheet(args_in)
