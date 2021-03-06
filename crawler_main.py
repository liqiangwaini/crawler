import html_downloader
import html_parser
import url_manager
import html_outputer


class SpiderMain(object):
    def __init__(self):
        self.urls = url_manager.UrlManager()
        self.downloader = html_downloader.HtmlDownloader()
        self.parser = html_parser.HtmlParser()
        self.outputer = html_outputer.HtmlOutputer()

    def craw(self, root_url):
        count = 1
        self.urls.add_new_url(root_url)
        while self.urls.has_new_url():
            try:
                new_url = self.urls.get_new_url()
                print 'craw %d : %s' %(count, new_url)
                html_content = self.downloader.download(new_url)
                new_urls, new_data = self.parser.parser(new_url, html_content)
                self.urls.add_new_urls(new_urls)
                self.outputer.collect_data(new_data)

                if count == 10:
                    break
                count = count + 1
            except BaseException, e:
                print e.message
                print 'craw fail'

        self.outputer.output_html()

if __name__=="__main__":
    root_url = "http://baike.baidu.com/item/%E8%9C%98%E8%9B%9B/8135707"
    obj_crawler = SpiderMain()
    obj_crawler.craw(root_url)
