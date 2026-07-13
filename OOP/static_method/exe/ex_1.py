import math


class PhotoAlbum:
    def __init__(self, pages: int):
        self.pages = pages
        self.photos = [[] for _ in range(pages)]

    @classmethod
    def from_photos_count(cls, photos_count: int):
        pages = math.ceil(photos_count / 4)
        return cls(pages)

    def add_photo(self, label: str):
        for page_index, page in enumerate(self.photos):
            if len(page) < 4:
                page.append(label)
                slot_number = len(page)
                page_number = page_index + 1
                return f"{label} photo added successfully on page {page_number} slot {slot_number}"
        return "No more free slots"

    def display(self):
        lines = ["-" * 11]
        for page in self.photos:
            lines.append(" ".join("[]" for _ in page))
            lines.append("-" * 11)
        return "\n".join(lines)
