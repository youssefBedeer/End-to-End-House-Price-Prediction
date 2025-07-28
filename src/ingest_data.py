from abc import ABC, abstractmethod 
import zipfile 
import os 
import pandas as pd 
import datetime



# interface 

class DataIngestor(ABC):
    @abstractmethod
    def ingest(self, file_path:str)-> pd.DataFrame:
        pass 


# Implement a concrete class for a ZIP ingestion 
class ZipDataIngestor(DataIngestor):
    def ingest(self, file_path:str, file_name:str=None)-> pd.DataFrame:
        """Extract .ZIP file and return content as pandas dataframe"""
        # Ensure the file is a zip file 
        if not file_path.endswith(".zip"):
            raise ValueError ("Not a zip file")
        
        # extract zip file 


        with zipfile.ZipFile(file_path, "r") as zip_ref:
            folder_name = "extracted_data"
            zip_ref.extractall(os.path.join("../",folder_name))


        # expole extracted data 
        extracted_folder_path = str(f"../{folder_name}")
        extracted_data = os.listdir(folder_name)
        csv_files = [f for f in extracted_data if f.endswith(".csv")] 
        print(f"Number of CSV files = {len(csv_files)}")

        
        if len(csv_files) == 0:
            raise ValueError (f"No csv files found extracted_data\n content of extracted_data folder\n{os.listdir(extracted_folder_path)}")
        if len(csv_files) > 1:
            print(csv_files)
            if file_name is None:
                raise ValueError(f"Multiple CSV files Please specify file_name while using the function read_file()")
            elif file_name not in csv_files:
                raise ValueError(f"file_name {file_name} not found")
            else: 
                csv_file_name = file_name
        else:
            csv_file_name = csv_files[0] 
            print(csv_file_name)

        # create dataframe 
        csv_file_path = os.path.join(folder_name,str(csv_file_name))
        df = pd.read_csv(csv_file_path)

        return df

# Implement Factory 
class DataIngestorFactory:
    @staticmethod
    def get_data_ingestor(file_extensiton: str)->DataIngestor:
        """Return the appropirate DataIngestor based on file extention"""
        file_extensiton = file_extensiton.lower() 
        if file_extensiton == ".zip":
            return ZipDataIngestor() 
        else:
            raise ValueError(f"No ingestor available for file extention: {file_extensiton}")

## user code 
def read_file(factory:DataIngestorFactory, file_extensiton, file_path, file_name=None):
    ingestor = factory.get_data_ingestor(file_extensiton)
    return ingestor.ingest(file_path, file_name=file_name) 



if __name__ == "__main__":
    file_path = r'data\folder.zip'
    factory = DataIngestorFactory() 

    read_file(factory=factory, file_extensiton='.zip', file_path=file_path)