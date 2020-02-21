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
@click.argument("file_path_to_csv")
def make_html_report(file_path_to_csv, destination_folder):
    """
    Create a HTML report of a csv dataset
    """

    name = os.path.basename(file_path_to_csv)

    # load data
    data = pd.read_csv(file_path_to_csv)

    # create profile report
    profile = ProfileReport(data, title=name, html={"style": {"full_width": True}})

    #create timestamp
    my_timestamp = str(datetime.now())[0:19]
    my_timestamp = my_timestamp.replace(" ", "_")
    my_timestamp = my_timestamp.replace(":", "_")

    # create tidy destination string
    name_without_extension = os.path.splitext(name)[0]
    name_without_extension = name_without_extension.replace(" ", "_")
    destination = os.path.join(destination_folder, name_without_extension + "_" + my_timestamp + ".html")

    # export to disk
    profile.to_file(output_file=destination)

    print("Ouput saved to: " + destination)

    return None


if __name__ == "__main__":
    make_html_report()
