from newspaper import Article

def GetText(url):
    # download and parse article
    article = Article(url)
    article.download()
    article.parse()
    
    # print article text
    return article.text