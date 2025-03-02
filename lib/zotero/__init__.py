# %%
import pandas as pd
from pyzotero import zotero
from pyzotero.zotero import Zotero
import dotenv
import json
from marker.converters.pdf import PdfConverter
from marker.models import create_model_dict
from marker.config.parser import ConfigParser
import os

from bs4 import BeautifulSoup

dotenv.load_dotenv()

def extract_text(html_string):
    soup = BeautifulSoup(html_string, "lxml")
    return soup.get_text()

config = {
    "output_format": "json",
    "languages": "en",
    "disable_image_extraction": True,
    "processors": "marker.processors.text.TextProcessor",
    "LOKY_MAX_CPU_COUNT": 8,
}

config_parser = ConfigParser(cli_options=config)
converter = PdfConverter(
    artifact_dict=create_model_dict(),
    config=config_parser.generate_config_dict(),
    processor_list=config_parser.get_processors(),
    renderer=config_parser.get_renderer(),
)

# %%
zot = zotero.Zotero(
    library_id=os.getenv("LIB_ID"),
    library_type="user",
    api_key=os.getenv("ZOT_API"),
    local=True,
)
# %%

collection_id: str = "ZU7ZFBKU"

items: list = zot.collection_items(collection_id)
articles: list = [
    x for x in items if x.get("data", {}).get("itemType") == "journalArticle"
]
for article in articles:
    attachment = article.get("links").get("attachment")
    if attachment is None:
        continue
    pdf_id = attachment.get("href").split("/")[-1]

    with open("temp.pdf", "wb") as f:
        f.write(zot.file(pdf_id))

    document = converter(filepath="temp.pdf")

    ids = []
    texts = []
    for page in document.children:
        entries = [p for p in page.children if p.block_type == "Text"]

        ids += [x.id.replace("/page/", "").replace("/Text/", ":") for x in entries]
        texts += [extract_text(html_string=x.html) for x in entries]

    result: dict = {
        "key": article.get("data").get("key"),
        "title": article.get("title"),
        "journal": article.get("publicationTitle"),
        "authors": article.get("creators"),
        "DOI": article.get("DOI"),
        "ids": ids,
        "texts": texts,
    }
    with open(file=f"../../data/processed/jsons/{result["key"]}.json", mode="w") as f:
        f.write(json.dumps(result))
# %%
zot.collections()
# %%
