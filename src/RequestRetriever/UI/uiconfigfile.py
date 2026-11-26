import configparser

import os


class Config:

    def __init__(self):

        # Create configuration object

        self.config = configparser.ConfigParser()

        # Get current directory

        current_dir = os.path.dirname(__file__)

        # Get INI file path

        config_path = os.path.join(

            current_dir,

            "uiconfigfile.ini"

        )

        # Read configuration file

        self.config.read(config_path, encoding="utf-8")

        # Read UI configurations

        self.PAGE_TITLE = self.config["DEFAULT"]["PAGE_TITLE"]

        self.PAGE_ICON = self.config["DEFAULT"]["PAGE_ICON"]

        self.LAYOUT = self.config["DEFAULT"]["LAYOUT"]

        self.APP_DESCRIPTION = self.config["DEFAULT"]["APP_DESCRIPTION"]

        self.INPUT_LABEL = self.config["DEFAULT"]["INPUT_LABEL"]

        self.INPUT_PLACEHOLDER = self.config["DEFAULT"]["INPUT_PLACEHOLDER"]

        self.BUTTON_NAME = self.config["DEFAULT"]["BUTTON_NAME"]

        self.RESULT_TITLE = self.config["DEFAULT"]["RESULT_TITLE"]