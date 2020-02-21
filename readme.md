# In production tools

#### gcp_cloud_upload.py
Upload files to a Google Cloud Storage bucket in the Panalysis Universal Analytics project

Basic usage:

```bash
python gcp_cloud_upload.py path_to_file_to_upload.mp4
```

#### csv_profile.py
Generate a HTML report about a csv dataset, powered by pandas-profiling

Basic usage:

```bash
python csv_profile.py path_to__csv_file_to_create_report_on.csv
```

#### xlsx_profile.py
Generate a HTML report about a xlsx dataset, powered by pandas-profiling

```bash
python xlsx_profile.py path_to__xlsx_file_to_create_report_on.xlsx
```

# Wishlist

- upload folders and files contained to Google Cloud Storage 
- move HTML saved files from downloads to saved_htmls folders
- convert video to gif
- cloud vision API
- markdown to HTML converter
- load csv into SQLite database
- screen record to gif 