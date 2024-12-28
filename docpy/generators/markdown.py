from typing import List
from docpy.definitions import Definition
from docpy.generator import Generator


class Markdown(Generator):
    def generate(self, definitions: List[Definition]):
        content = "# Documentation"
        for item in definitions:

            if item.type == "function":
                content += f"\n\n## Function: `{item.name}`\n"
                content += f"- File: {item.file}\n"
                content += f"- Args: {', '.join(item.arguments)}\n"

            elif item.type == "class":
                content += f"\n\n## Class: `{item.name}`\n"
                content += f"- File: {item.file}\n"
                
                for method in item.methods:
                    content += f"\n\n### Method: `{method.name}`\n"
                    content += f"- Args: {', '.join(method.arguments)}\n"

            if item.docstring:
                content += f"- Description: {item.docstring}"

        return content