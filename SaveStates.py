#This was written to automatically generate the text files in the USA States folder.

from Functions.Scraper import Bot
import Functions.constants as const


with Bot() as test:
    test.open_url(const.base_url)       # Opens main URL
    test.save_states()
    test.save_cities()
