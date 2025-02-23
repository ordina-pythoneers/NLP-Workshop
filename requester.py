"""Module to add files to the database instance."""

import requests


if __name__ == "__main__":
    # Every time you run this module, it will add the file(s) in the dict below
    # to the database instance.
    files = {"file": open("file.txt", "rb")}  # pylint: disable=consider-using-with
    r = requests.post("http://localhost:8000/upload_file", files=files)
    print(r.content)
    print(r.status_code)
