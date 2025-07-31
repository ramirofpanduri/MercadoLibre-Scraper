import pytz
from apscheduler.schedulers.blocking import BlockingScheduler
from .scraper.ml_scraper import scrape_mercadolibre
from .database.save_products import save_products


arg_timezone = pytz.timezone("America/Argentina/Buenos_Aires")


def job():
    print("Scraping")
    products = scrape_mercadolibre(
        "https://www.mercadolibre.com.ar/ofertas?domain_id=MLA-CELLPHONES&container_id=MLA779505-1#deal_print_id=4ae460f0-52b3-11f0-ac2b-8f126b64e4a0&c_tracking_id=4ae460f0-52b3-11f0-ac2b-8f126b64e4a0")
    save_products(products)
    print(f"{len(products)} productos processed.")


if __name__ == "__main__":
    scheduler = BlockingScheduler(timezone=arg_timezone)
    scheduler.add_job(job, "interval", hours=12)
    print("Scraper running every 12 hours")
    scheduler.start()
