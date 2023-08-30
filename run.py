from Functions.Scraper import Bot
import time
import Functions.constants as const

def run(search):
    with Bot() as web:
        web.open_url(const.base_url)       # Opens main URL
        web.select_state(const.state)      # Selects State
        web.select_county(const.county)    # Selects County
        time.sleep(5)                      # Wait for webpage to load [Increase time if internet is slow]
        web.search_bar(search)             # Search the term
        web.search_per_page(const.posts)   # Mark 50 results/page
        web.all_headings(const.print_data)
        
        web. download_sections(const.download)      # Open or Download files as Word.doc
        # web.download_pdf()        # Download as PDF


run("Minimum trees per lot")
#run("vegetation")
#run("trees allowed on lot")
#run("tree types")
#run("native")
#run("tree height")

#time.sleep(const.remain_open)
