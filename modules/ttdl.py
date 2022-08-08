from bs4 import BeautifulSoup as bs
import requests as req


def TikTokDownloader(url):
    try:

        headers = {

            'Host': 'musicaldown.com',
            'User-Agent': 'Mozilla/5.0 (Linux; Android 10) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.88 Mobile Safari/537.36',
        }

        reqWeb = req.get("https://musicaldown.com/id", headers=headers)
        bsoup = bs(reqWeb.text, 'html.parser')
        keyName1 = bsoup.find('input', {'id': 'link_url'})['name']
        keyName2 = bsoup.find('input', {'type': 'hidden'})['name']
        tokenValue = bsoup.find('input', {'type': 'hidden'})['value']

        postBody = {keyName1: url,
                    keyName2: tokenValue, 'verify': 1}
        reqPost = req.post("https://musicaldown.com/id/download",
                           data=postBody, headers=headers, cookies=reqWeb.cookies)

        initScrapeLink = bs(reqPost.text, 'html.parser')

        getLinks = []
        if 'Check out' in initScrapeLink.find('title').string:
            extractLinks = initScrapeLink.find_all(
                'a', {'target': '_blank'})
            for extractLink in extractLinks:
                getLinks.append(extractLink['href'])

            return {
                'success': True,
                'msg': 'Success Get Download Link',
                'links': getLinks
            }

        else:
            return {
                'success': False,
                'msg': 'Cannot Get Download Link, Check Your Url'
            }

    except:
        return {
            'success': False,
            'msg': 'Something Error, Try Again'
        }


# TikTokDownloader('https://vt.tiktok.com/ZSwWCk5o')
