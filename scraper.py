import os
import time
import requests
from selenium import webdriver
from logger import App_Logger
import shutil
from webdriver_manager.chrome import ChromeDriverManager
import chromedriver_binary


class Image_scrapper:
    """
    It is used for scraping images from google

    Parameters
    ----------
    name: type of images to be scrapped,eg: car,tree
    count: Number of images to be scrapped
    """

    def __init__(self):
        self.logger = App_Logger("static/imagescrapper.log")  # creating App_Logger object
        try:
            self.logger.log("info", "creating webdriver")
            chrome_options = webdriver.ChromeOptions()
            chrome_options.add_argument("--headless")
            chrome_options.add_argument("--disable-gpu")
            chrome_options.add_argument("window-size=1024,768")
            chrome_options.add_argument("--no-sandbox")
            chrome_options.add_argument("disable-dev-shm-usage")
            try:
                self.logger.log("info", "creating webdriver2")
                self.driver = webdriver.Chrome(
                    executable_path="./chromedriver", chrome_options=chrome_options)
            # ChromeDriverManager("92.0.4515.131").install()
            except Exception as e:
                self.logger.log("error", "Image_scrapper object not created -error1" + str(e))
            self.logger.log("info", "Image_scrapper object created")  # logging

        except Exception as e:
            self.logger.log("error", "Image_scrapper object not created -error" + str(e))

    def fetch_image_urls(
        self, query: str, max_links_to_fetch: int, sleep_between_interactions: int = 1
    ):
        """
        To fetch image urls, which will be later used to download the images

        Parameters
        ----------
        query: search keyword
        max_links_to_fetch: no. of links to be fetched
        sleep_between_interactions: break between 2
        """

        def scroll_to_end():
            """
            To scroll down html page while scraping to load new images

            Parameters
            ----------

            """
            self.driver.execute_script(
                "window.scrollTo(0, document.body.scrollHeight);"
            )
            time.sleep(sleep_between_interactions)

            # build the google query

        search_url = "https://www.google.com/search?safe=off&site=&tbm=isch&source=hp&q={q}&oq={q}&gs_l=img"

        # load the page
        self.driver.get(search_url.format(q=query))

        image_urls = set()
        image_count = 0
        results_start = 0

        while image_count < max_links_to_fetch:
            scroll_to_end()
            # get all image thumbnail results
            thumbnail_results = self.driver.find_elements_by_css_selector("img.Q4LuWd")
            number_results = len(thumbnail_results)
            self.logger.log(
                "info",
                f"Found: {number_results} search results. Extracting links from {results_start}:{number_results}",
            )
            for img in thumbnail_results[results_start:number_results]:
                # try to click every thumbnail such that we can get the real image behind it
                try:
                    img.click()
                    time.sleep(sleep_between_interactions)
                except Exception:
                    continue

                # extract image urls
                actual_images = self.driver.find_elements_by_css_selector("img.n3VNCb")
                for actual_image in actual_images:
                    if actual_image.get_attribute(
                        "src"
                    ) and "http" in actual_image.get_attribute("src"):
                        image_urls.add(actual_image.get_attribute("src"))

                image_count = len(image_urls)

                if len(image_urls) >= max_links_to_fetch:
                    self.logger.log(
                        "info", f"Found: {len(image_urls)} image links, done!"
                    )

                    break
            else:
                self.logger.log(
                    "info",
                    f"Found: {len(image_urls)} image links, looking for more ...",
                )
                time.sleep(30)
                return
                load_more_button = wd.find_element_by_css_selector(".mye4qd")
                if load_more_button:
                    wd.execute_script("document.querySelector('.mye4qd').click();")

            # move the result startpoint further down
            results_start = len(thumbnail_results)

        return image_urls

    def persist_image(self, folder_path: str, url: str, counter):
        """
        To save images

        Parameters
        ----------
        folder_path: target folder
        url:image url
        counter:image counter
        """
        try:
            image_content = requests.get(url).content

        except Exception as e:
            self.logger.log("error", f"Could not download {url} - {str(e)}")

        try:
            f = open(
                os.path.join(folder_path, "jpg" + "_" + str(counter) + ".jpg"), "wb"
            )
            f.write(image_content)
            f.close()
            self.logger.log("info", f"SUCCESS - saved {url} - as {folder_path}")
        except Exception as e:
            self.logger.log("error", f"Could not save {url} - {str(e)}")

    def search_and_download(self, name, count, email, target_path="./images"):
        """
        To scroll down html page while scraping to load new images

        Parameters
        ----------

        """
        target_folder = os.path.join(
            target_path, "_".join(email[: email.index("@")].lower().split(" "))
        )

        if not os.path.exists(target_folder):
            os.makedirs(target_folder)
            self.logger.log("info", f"folder created{target_folder}")

        self.logger.log("info", "Fetching Image URLs")
        res = self.fetch_image_urls(name, count, sleep_between_interactions=0.5)

        counter = 0
        for elem in res:
            self.logger.log("info", "Download Started")
            self.persist_image(target_folder, elem, counter)
            counter += 1
        # Creating ZIP file
        shutil.make_archive(
            f"static/download/{name}_{count}_" + email[: email.index("@")].lower(),
            "zip",
            "images/" + email[: email.index("@")].lower(),
        )
        # removing images folder
        shutil.rmtree("images/" + email[: email.index("@")].lower())
