import crawler5
import cloud
def online(sear):
    brower = crawler5.crawler('http://weibo.com')
    brower.log_in()
    # nums=eval(input('输入爬取的页数：'))
    #sears = input('输入爬虫关键词：') + '/'
    #sears = sears.split('/')
    # sears=input('输入爬虫关键词：').split('/')
    brower.get_outcomes(1, sear)
    # brower.get_outcomes(nums,sears)
    brower.brower.quit()
    word_cloud = cloud.data(sear)
    word_cloud.read_all()
    word_cloud.ciyun()
