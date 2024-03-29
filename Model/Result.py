from dataclasses import dataclass


@dataclass
class Result:
    original: str
    image: str
    confirmed: str

    def __init__(self, **result):
        self.original = result['original']
        self.image = result['image']
        try:
            self.confirmed = result['confirmed']
        except KeyError:
            self.confirmed = None

    def serialize(self):
        return {"original": self.original, "image": self.image, "confirmed":self.confirmed}