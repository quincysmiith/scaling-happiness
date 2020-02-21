import pandas as pd
from pandas_profiling import ProfileReport
import click
import os
from datetime import datetime


@click.command()
@click.option(
    "--destination_folder",
    default="C:\\Users\\Marquin\\Documents\\dataset_reports",
    help="The directory that the output html report will be saved to.",
)
@click.option(
    "--sheet_number",
    default=0,
    help="Starting at 0, the sheet number to extract data from",
)
@click.argument("file_path_to_xlsx")
def make_html_report_from_xlsx(file_path_to_xlsx, sheet_number, destination_folder):
    """
    Create a HTML report of a xlsx dataset.
    Data must be in a table form.
    """

    name = os.path.basename(file_path_to_xlsx)

    # load data
    data = pd.read_excel(file_path_to_xlsx, sheet_name=sheet_number)

    # create profile report
    profile = ProfileReport(data, title=name, html={"style": {"full_width": True}})

    # create timestamp
    my_timestamp = str(datetime.now())[0:19]
    my_timestamp = my_timestamp.replace(" ", "_")
    my_timestamp = my_timestamp.replace(":", "_")

    # create tidy destination string
    name_without_extension = os.path.splitext(name)[0]
    name_without_extension = name_without_extension.replace(" ", "_")
    destination = os.path.join(
        destination_folder, name_without_extension + "_" + my_timestamp + ".html"
    )

    # export to disk
    profile.to_file(output_file=destination)

    print("Ouput saved to: " + destination)

    return None


if __name__ == "__main__":
    make_html_report_from_xlsx()
