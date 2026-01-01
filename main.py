import asyncio from scraper.engine import CompanyScraper from enrichment.processor import DataEnricher

async def main(): # Phase 1: Scraping Raw Names scraper = CompanyScraper(source_url="https://example-directory.com") raw_companies = await scraper.run()

# Phase 2: AI-Powered Enrichment (Website + LinkedIn)
enricher = DataEnricher()
enriched_data = await enricher.process_batch(raw_companies)

# Phase 3: Output Results
for company in enriched_data:
    print(f"Company: {company['name']} | Site: {company['website']} | LinkedIn: {company['linkedin']}")


if name == "main": asyncio.run(main())