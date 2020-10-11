from storages.backends.azure_storage import AzureStorage
from pathlib import Path
import os

from os.path import join, dirname
from dotenv import load_dotenv

dotenv_path = join(dirname(__file__), '.env')
load_dotenv(dotenv_path)


class AzureMediaStorage(AzureStorage):
    account_name = os.getenv("ACCOUNT_NAME")
    account_key = os.getenv("ACCOUNT_KEY")
    azure_container = 'media'
    expiration_secs = None

class AzureStaticStorage(AzureStorage):
    account_name = os.getenv("ACCOUNT_NAME")
    account_key = os.getenv("ACCOUNT_KEY")
    azure_container = 'static'
    expiration_secs = None