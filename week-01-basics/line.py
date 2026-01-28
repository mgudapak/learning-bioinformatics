import re


class Line:

    def __init__(self, text: str):
        self.text = text

    def has_comment(self) -> bool:
        return "#" in self.text

    def strip_comments(self) -> str:
        if self.has_comment():
            return re.split("#", self.text)[0]
        else:
            return self.text

    def file_summary(filename):
        return
