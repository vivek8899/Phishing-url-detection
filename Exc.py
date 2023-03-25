import requests as re
import os

# 1 A FOLDER TO SAVE HTML FILES
folder = "mini_dataset"  # Write your own folder name

if not os.path.exists(folder):
    os.mkdir(folder)


# 2 A FUNCTION THAT SCRAPES AND RETURNS IT
def scrape_content(URL):
    response = re.get(URL)
    if response.status_code == 200:
        print("HTTP connection is succuessful! for the URL:", URL)
        return response
    else:
        print("HTTP connection is NOT successful! for the URL:", URL)
        return None


# 3 A FUNCTION TO SAVE A HTML FILE OF THE SCRAPED WEBPAGE IN A DIRECTORY

path = os.getcwd() + "/" + folder  # You can define the path manually.


def save_html(to_where, text, name):
    file_name = name + ".html"

    with open(os.path.join(to_where,file_name), "w", encoding="utf-8") as f:
            f.write(text)


# 4 DEFINE YOUR OWN URL LIST HERE as BELOW EXAMPLE

URL_list = [
    "https://www.kaggle.com",
    "https://stackoverflow.com",
    "https://www.researchgate.net",
    "https://www.python.org",
    "https://www.w3schools.com",
    "https://wwwen.uni.lu",
    "https://github.com",
    "https://scholar.google.com",
    "https://www.mendeley.com",
    "https://www.overleaf.com"
]


# 5 DEFINE A FUNCTION WHICH TAKES THE URL LIST and RUN STEP 2 and STEP 3 for EACH URL
def create_mini_dataset(to_where, URL_list):
    for i in range(0, len(URL_list)):
        content = scrape_content(URL_list[i])
        if content is not None:
            save_html(to_where, content.text, str(i))
        else:
            pass
    print("Mini dataset is created!")


create_mini_dataset(path, URL_list)