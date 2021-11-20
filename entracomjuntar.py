
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.chrome.options import Options
from selenium.webdriver import ActionChains
import os

chrome_options = Options()
#download_dir = tempfile.mkdtemp()


download_dir = './temp'

chrome_options.add_experimental_option('prefs', {
        "plugins.plugins_list": [{"enabled":False,"name":"Chrome PDF Viewer"}],
        "download": {
        "prompt_for_download": False,
        "default_directory"  : download_dir
        }
    })
