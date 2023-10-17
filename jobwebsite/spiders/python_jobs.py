import scrapy
from scrapy.http import Response


class PythonJobsSpider(scrapy.Spider):
    name = "python_jobs"
    allowed_domains = ["djinni.co"]
    start_urls = ["https://djinni.co/jobs/?primary_keyword=Python"]

    def parse(self, response: Response, **kwargs):
        for jobs in response.css(".job-list-item"):
            yield {
                "jobs_name": jobs.css(".job-list-item__link::text").get().strip(),
                "company_name": jobs.css(".mr-2::text").getall()[2].strip(),
                "date_time": jobs.css(".text-muted").css(".mr-2::attr(title)").get(),
                "description": jobs.css(".job-list-item__description span::attr(data-original-text)").get(),
                "localization": jobs.css(".job-list-item__job-info > span::text").getall()[-3],
                "experience": jobs.css(".job-list-item__job-info span.nobr::text").getall()[-2],
                "english_level": jobs.css(".job-list-item__job-info span.nobr::text").getall()[-1]
            }

        next_page = response.css(".pagination").css(".page-item a::attr(href)").getall()[-1]
        if next_page is not None:
            next_page = response.urljoin(next_page)
            yield scrapy.Request(next_page, callback=self.parse)