import requests
import scrapy

def get_info(anime_id):

    url = f'https://myanimelist.net/anime/{anime_id}'

    request = requests.get(url)
    html = request.content.decode('utf-8')
    sel = scrapy.Selector(text=html)

    xpath = '//p[@itemprop="description"]/text()'
    sinopse = ''.join(sel.xpath(xpath).extract())

    xpath = '//img[@itemprop="image"]/@data-src'
    img_url = sel.xpath(xpath).extract_first()

    xpath = '//a[@class="iframe js-fancybox-video video-unit promotion"]/@href'
    teaser_url = sel.xpath(xpath).extract_first()

    return {
        'url': url,
        'sinopse': sinopse,
        'image': img_url,
        'teaser': teaser_url
    }