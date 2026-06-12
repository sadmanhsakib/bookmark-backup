import datetime
import json
import os

from dotenv import load_dotenv
from pathlib import Path

load_dotenv()

PROJECT_ROOT = Path(__file__).parent

BOOKMARK_DIRS = os.getenv("BOOKMARK_DIRS").split(",")
OUTPUT_DIR = Path(os.getenv("OUTPUT_DIR")) or PROJECT_ROOT
MAX_BACKUP = int(os.getenv("MAX_BACKUP")) or 0


def main():
    # creating the backup
    for i, path in enumerate(BOOKMARK_DIRS, 1):
        with open(path, "r") as bookmark:
            # stores the bookmark data into a python dict
            data = json.load(bookmark)

        # gets the bookmarks in HTML format with proper indentation
        bookmark_bar = extract_bookmarks(data["roots"]["bookmark_bar"]["children"])
        other_bookmarks = extract_bookmarks(data["roots"]["other"]["children"])

        all_bookmarks = bookmark_bar + other_bookmarks

        exporting_to_HTML(bookmarks=all_bookmarks, index=i)

    backup_filenames = [
        f for f in os.listdir(OUTPUT_DIR) if f.startswith("bookmark_backup_")
    ]
    
    # removing old backups
    if MAX_BACKUP > 0 and len(backup_filenames) > MAX_BACKUP:
        backup_filenames.sort()
        
        for filename in backup_filenames[:-MAX_BACKUP]:
            os.remove(OUTPUT_DIR / filename)


def extract_bookmarks(json_data: json, indent_level: int = 0):
    """
    extracts all the bookmarks recursively from the JSON file
    if there is no indent_level as argument, use 0 as default value
    """
    html_content = ""
    indent = "  " * indent_level

    for item in json_data:
        # if the type is url, then add it to the html_content
        if item["type"] == "url":
            html_content += f'{indent}<DT><A HREF="{item["url"]}">{item["name"]}</A>\n'
        elif item["type"] == "folder":
            folder_name = item["name"]

            # Start of a folder
            html_content += f"{indent}<DT><H3>{folder_name}</H3>\n"
            html_content += f"{indent}<DL><p>\n"

            # Recursively process the children of the folder
            html_content += extract_bookmarks(item["children"], indent_level + 1)

            # End of the folder
            html_content += f"{indent}</DL><p>\n"
    return html_content


def exporting_to_HTML(bookmarks: str, index: int): 
    """exports a HTML file using the all extracted bookmarks"""
    # the initials of the file
    html_headers = """<!DOCTYPE NETSCAPE-Bookmark-file-1>
<HTML>
<meta http-equiv="Content-Type" content="text/html; charset=UTF-8" />
<TITLE>Bookmarks</TITLE>
<H1>Bookmarks</H1>
<DL><p>
"""

    html_footer = "</DL><p></HTML>"

    full_html = html_headers + bookmarks + html_footer

    filename = (
        f"bookmark_backup_{index}_{datetime.datetime.now().strftime('%Y-%m-%d')}.html"
    )
    
    os.makedirs(OUTPUT_DIR, exist_ok=True)
    
    filepath = os.path.join(OUTPUT_DIR, filename)
    
    with open(filepath, "w", encoding="utf-8") as file:
        file.write(full_html)


if __name__ == "__main__":
    main()
