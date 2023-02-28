import argparse
from command_modules.create_info_sheet import create_info_sheet
from command_modules.aggregate_grades import aggregate_grades

def fill_team_grades(args):
    grade_file = args.grade_file
    team_file = args.team_file
    return


if __name__ == "__main__":
    # Create argument parser
    parser = argparse.ArgumentParser(description="A utility for EPICS document creation and grading.")
    subparsers = parser.add_subparsers(description='The main commands for the program', dest='command', required=True)

    # fill team grades
    parser_fill_grades = subparsers.add_parser('fill-grades', help='Distribute grades for all members of a team')
    parser_fill_grades.add_argument('--grade-file', required=True)
    parser_fill_grades.add_argument('--team-file', required=True)
    parser_fill_grades.set_defaults(func=fill_team_grades)

    # create student info TEX file
    parser_student_info = subparsers.add_parser('student-info-doc', help='Create tex output for team info files')
    parser_student_info.add_argument('--team-file', default="class_data/team_list.csv")
    parser_student_info.add_argument('--student-info-file', default="class_data/eLearning_user_information.csv")
    parser_student_info.add_argument('--document-title', default="EPICS Class List")
    parser_student_info.add_argument('--output-dir-name', default="student_info_doc")
    parser_student_info.add_argument('--image-location')

    # aggregate team grades
    parser_grade_aggregate = subparsers.add_parser('aggregate-grades', help='Aggregate grades from assignments by team')
    parser_grade_aggregate.add_argument('--team-file', default="class_data/team_list.csv")
    parser_grade_aggregate.add_argument('--grade-files', default="class_data/grade_files")
    parser_grade_aggregate.add_argument('--document-title', default="Mid-Semester Grade Summary")
    parser_grade_aggregate.add_argument('--output-dir-name', default="semester_grade_review")

    # Parse args and run command
    top_args = parser.parse_args()
    if top_args.command == 'student-info-doc':
        create_info_sheet(top_args)
    elif top_args.command == 'aggregate-grades':
        aggregate_grades(top_args)

    # print(top_args)
    # top_args = parser.parse_args('fill-grades --grade-file taco.txt --team-file bell.csv'.split())
    # top_args.func(top_args)
    # print(top_args)

