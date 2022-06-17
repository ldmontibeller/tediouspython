from pathlib import Path

p = Path(r'C:\Users\*your_username*\*your_absolute_filepath_with_simple_slash_because_we_are_using_the_letter_r_for_a_raw_input*')
#I wanted all the .docx files
for source_file in p.glob("*.docx"):
    if source_file.is_file():
        print("OLD:", source_file)
        old_name = source_file.name
        #Here i wanted to remove the first 3 characters of the filename
        new_name = old_name[3:]
        print(new_name)
        source_file.rename(Path(p,new_name))
      


