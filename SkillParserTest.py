import os
import skill_parser

fileNames = []
for root, dirs, files in os.walk("."):
    for filename in files:
        if filename.endswith("Resume.docx"):
            print("Detected skills for " + filename + ":")
            print(skill_parser.get_skills(filename))
            print()