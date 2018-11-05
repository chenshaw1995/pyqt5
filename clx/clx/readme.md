# base

run a spider:
scrapy crawl quotes

extracting data
scrapy shell "http://quotes.toscrape.com/page/1/"

#selectors

Using the shell, you can try selecting elements using CSS with the response object:

>>> response.css('title')
[<Selector xpath='descendant-or-self::title' data='<title>Quotes to Scrape</title>'>]

extract the text from the title above, you can do:

>>> response.css('title::text').extract()
['Quotes to Scrape']

There are two things to note here: one is that we’ve added ::text to the CSS query, to mean we want to select only the text elements directly inside <title> element. If we don’t specify ::text, we’d get the full title element, including its tags:

>>> response.css('title').extract()
['<title>Quotes to Scrape</title>']

### use regular expression in selectors

Using selectors with regular expressions
Selector also has a .re() method for extracting data using regular expressions. However, unlike using .xpath() or .css() methods, .re() returns a list of unicode strings. So you can’t construct nested .re() calls.

Here’s an example used to extract image names from the HTML code above:

>>> response.xpath('//a[contains(@href, "image")]/text()').re(r'Name:\s*(.*)')
[u'My image 1',
 u'My image 2',
 u'My image 3',
 u'My image 4',
 u'My image 5']

# ref
https://doc.scrapy.org/en/latest/intro/tutorial.html#our-first-spider
https://doc.scrapy.org/en/latest/topics/selectors.html
https://doc.scrapy.org/en/latest/intro/tutorial.html#our-first-spider
https://www.linode.com/docs/development/python/use-scrapy-to-extract-data-from-html-tags/

# run scrapy on notebook

https://stackoverflow.com/questions/40856730/how-to-run-scrapy-project-in-jupyter
https://docs.scrapy.org/en/latest/topics/practices.html#run-scrapy-from-a-script
