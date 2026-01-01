from playwright.async_api import async_playwright

class CompanyScraper: def init(self, source_url): self.source_url = source_url

async def run(self):
    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=True)
        page = await browser.new_page()
        await page.goto(self.source_url)
        
        # Logic to extract company names from the specific directory layout
        names = await page.locator(".company-title").all_inner_texts()
        
        await browser.close()
        return [name.strip() for name in names]