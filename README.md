# wiki-table-scraper
extracts, cleans, and formats data tables from wikipedia into JSON

web page url is defined in the code, not by CL arguments

with no edits, this script will generate a (mostly) cleaned JSON table of the data from <a href="https://en.wikipedia.org/wiki/List_of_mass_shootings_in_the_United_States#1920s">this wiki page</a> as "table.json"

to scrape a different page, you must supply:

  url =  " "
  (with a url)

If multiple tables are on page (and you want to scrape them all)

  for i in range (1, x):
  (x = number of tables on page + 1)

If single table, comment out the for loops


I plan to turn this into an application that lets you do all this through a GUI instead of editing code

Maybe a website, maybe a chrome extension — we shall see
