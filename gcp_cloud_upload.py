from dotenv import load_dotenv
from google.cloud import storage
import click
import os

# load variables from .env into environment
load_dotenv()


@click.command()
@click.option(
    "--bucket_id",
    default="panalysis-researching",
    help="The name of the Google Cloud Storage bucket to upload to. (within Panalysis Universal Analytics project)",
)
@click.option(
    "--folder_in_bucket",
    default="",
    help="Use forward slashes to indicate folders eg 'some/folder/heirarchy/'",
)
@click.argument("filename")
def upload_to_bucket(filename, bucket_id, folder_in_bucket):
    """
    Helper function that uploads a file that is currently on disk
    to a Google Cloud Storage bucket.
    Requires path to credential json file already exported to
    environment variable.
    """

    client = storage.Client()
    bucket = client.get_bucket(bucket_id)

    name = os.path.basename(filename)

    blob = bucket.blob(folder_in_bucket + name)
    blob.upload_from_filename(filename=filename)

    return None


if __name__ == "__main__":
    upload_to_bucket()
