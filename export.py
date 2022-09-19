import csv
from time import time
from dataclasses import dataclass
from typing import List
from zipfile import ZipFile


@dataclass
class AnkiAppCard:
    text_for_front: str
    text_for_back: str
    tags: List[str] | None = None
    image_filename_for_front: str = ''
    image_filename_for_back: str = ''
    audio_filename_for_front: str = ''
    audio_filename_for_back: str = ''


def generate_csv_file(cards: List[AnkiAppCard]) -> str:
    csv_filename = f'{time()}.csv'
    with open(csv_filename, 'w', encoding='utf-8') as f:
        writer = csv.writer(f)

        for card in cards:
            writer.writerow([
                card.text_for_front,
                card.text_for_back,
                ','.join(card.tags) if card.tags is not None else '',
                card.image_filename_for_front,
                card.image_filename_for_back,
                card.audio_filename_for_front,
                card.audio_filename_for_back,
            ])

    return csv_filename

def generate_filenames(cards: List[AnkiAppCard]) -> List[str]:
    filenames = []

    for card in cards:
        if card.image_filename_for_front:
            filenames.append(card.image_filename_for_front)
        if card.image_filename_for_back:
            filenames.append(card.image_filename_for_back)
        if card.audio_filename_for_front:
            filenames.append(card.audio_filename_for_front)
        if card.audio_filename_for_back:
            filenames.append(card.audio_filename_for_back)

    return filenames

def export_zip(cards: List[AnkiAppCard]) -> None:
    csv_filename = generate_csv_file(cards)
    filenames = generate_filenames(cards)

    zip_filename = f'{time()}.zip'
    with ZipFile(zip_filename, 'w') as zip:
        zip.write(csv_filename)
        for filename in filenames:
            zip.write(filename)

def naive_test():
    hello_card = AnkiAppCard(
        text_for_front='used when meeting or greeting someone',
        text_for_back='hello',
        tags=['exclamation', 'noun'],
        audio_filename_for_back='hello.mp3'
    )
    export_zip([hello_card])

if __name__ == '__main__':
    naive_test()