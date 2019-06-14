import scrapy

class flightradar24Scraper(scrapy.Spider):
    name = 'flight'
    
    
    
    def flight_request(self):
        strt_url = 'https://www.flightradar24.com/data/flights/dy7092'
    
        yield scrapy.Request(url = strt_url, callback = self.parse)
        
    def parse(self, response):
        flight_num = response.url.split("/")[-1]
        fname = 'C:\Vivek\Work\Projects\Gold_Care_Phase_1\03_Coding_Workspace\flight-%s.html' %flight_num
        
        with open(fname,'w') as f:
            f.write(response.body)