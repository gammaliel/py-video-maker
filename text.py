from nltk import sent_tokenize
import Algorithmia
import re

def fetch_wikipedia_article(content):
    client = Algorithmia.client('simAoS+NCBot8SACwnHwpY0ezGR1')   
    algo = client.algo('web/WikipediaParser/0.1.2')  
    content['source_original_content'] = algo.pipe(content['search_term']).result["content"]
    return content

# Removes blank lines, dates in paretheses, and whatever is left of Markdown
def sanitize_content(content):
    article = content['source_original_content']

    # Removes blank lines and markdown
    article = "".join([i for i in article.splitlines(True) if not (len(i) < 2 or i.startswith('='))])

    # Removes dates in parentheses
    article = re.sub("/\((?:\([^()]*\)|[^()])*\)/gm", '', article)

    content['source_original_content'] = article
    return content

def text(content):
    content = fetch_wikipedia_article(content)
    content = sanitize_content(content)
