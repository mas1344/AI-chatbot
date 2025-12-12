
from langchain_community.document_loaders import TextLoader
from backend.constants import DATA_PATH

def extract_text_from_md(path) -> str:

    loader = TextLoader(path)

    document = loader.load()

    all_text = document[0].page_content

    return all_text

def export_text_to_txt(text, export_path):
    with open(export_path, "w") as file:
        file.write(text)

if __name__=="__main__":
    for md_path in DATA_PATH.glob("*.md"):
        md_text = extract_text_from_md(md_path)

        filename = f"{md_path.stem.casefold()}.txt"

        export_text_to_txt(md_text, DATA_PATH / filename)



