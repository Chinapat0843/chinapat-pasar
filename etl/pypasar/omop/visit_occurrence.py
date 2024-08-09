import traceback
import os
from sqlalchemy import create_engine, text
from dotenv import load_dotenv
from ..db.utils.postgres import postgres
from ..db.utils.bigquery import bigquery
# Load environment variables from the .env file
load_dotenv()


class visit_occurrence:

    def __init__(self):
        self.engine = postgres().get_engine()  # Get PG Connection
        # self.engine = bigquery().get_engine()  # Get BQ Connection

    def execute(self):
        try:
            self.initialize()
            self.process()
            self.finalize()
        except Exception as err:
            print(f"Error occurred {self.__class__.__name__}")
            raise err

    def initialize(self):
        pass

    def process(self):
        # In batches
        # Read from source
        # Transform
        # Ingest into OMOP Table
        pass

    def finalize(self):
        # Verify if needed
        pass