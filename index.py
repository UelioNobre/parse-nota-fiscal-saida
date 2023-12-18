import os
from tika import parser

filepath = os.path.join(
    os.path.dirname(__file__),
    "docs",
    "23-11-movimento-de-notas-fiscais.pdf",
)

parsed_document = parser.from_file(filepath)
parsed_content = parsed_document["content"]
print(f"File path: ${parsed_content}")
