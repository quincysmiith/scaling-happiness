# utility script to move html files from one folder to another

import os
import shutil
import click

@click.command()
@click.option(
    "--original_folder",
    default="/home/fuzzy/Downloads",
    help="The directory that matching files will be moved from"
)
@click.option(
    "--new_folder",
    default="/home/fuzzy/Documents/Projects/saved_html",
    help="The directory that matching files will be moved to"
)
@click.option(
    "--file_extension",
    default=".html",
    help="Files that end with this will be moved to the new folder"
)
def move_files_of_type(original_folder, new_folder, file_extension):
    """
    Move files that end with a certain suffix to a new folder.
    This deletes the version from the original location
    """

    html_list = []

    with os.scandir(original_folder) as it:
        for entry in it:
            if entry.name.endswith(".html") and entry.is_file():
                html_list.append(entry.name)


    for item in html_list:
        orig_path = os.path.join(original_folder, item)
        new_path = os.path.join(new_folder, item)
        shutil.copyfile(orig_path, new_path)
        os.remove(orig_path)




if __name__ == "__main__":
    move_files_of_type()