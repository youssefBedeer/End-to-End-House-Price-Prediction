from abc import ABC, abstractmethod 
import pandas as pd 

class DataInspectionStrategy(ABC):
    @abstractmethod
    def inspect(self, df:pd.DataFrame):
        """
        Perform a specific type of data inspection.

        Parameters:
        df (pd.DataFrame): The dataframe on which the inspection is to be performed.

        Returns:
        None: This method prints the inspection results directly.
        """
        pass 

class DataTypesInspectionStrategy(DataInspectionStrategy):
    def inspect(self,df:pd.DataFrame):
        """
            Inspect data types and null of dataframe 

            Args:
                df (pd.DataFrame) to be inspected

            Returns:
                None : Prints the data types and non-null content for each column
        """

        print("Data Types of Data Frame") 
        return df.info()
    
class DescribeInspectionStrategy(DataInspectionStrategy):
    def inspect(self, df: pd.DataFrame):
        """
            Print statistical information about each column 

            Args:
                df (pd.DataFrame) to be inspected

            Returns:
                None : Print statistical information about each column 
        """
        print("_"*50)
        print("Statistical Information for Numerical columns\n")
        print("_"*50)
        print(df.describe())
        #----------------------------
        print("_"*50)
        print("\nStatistical Information for none-numerical columns\n")
        print("_"*50)
        print(df.describe(include=["O"]))



class DataInspector:
    def __init__(self, strategy:DataInspectionStrategy):
        """
        Initialize the strategy for DataInspector 

        Args:
            strategy (DataInspectionStrategy) 

        Returns:
            None
        """
        self._strategy = strategy

    def set_strategy(self, strategy:DataInspectionStrategy):
        """
        Set a new strategy for DataInspector

        Args:
            strategy (DataInspectionStrategy)

        Returns:
            None
        """
        self._strategy = strategy

    def execute_inspection(self, df:pd.DataFrame):
        """
        Executes the inspection using the current strategy.

        Args:
            df (pd.DataFrame): The dataframe to be inspected.

        Returns:
        None: Executes the strategy's inspection method.
        """  
        self._strategy.inspect(df)


## user code 
def explore(strategy:str, df:pd.DataFrame):
    """
    Explore data information based on strategy

    Args:
        strategy -> info, descripe 

    Returns:
        None: Print data information based on strategy
    """

    strategy =  strategy.lower() 
    if strategy == "info":
        inspector = DataInspector(strategy=DataTypesInspectionStrategy())
        inspector.execute_inspection(df)
    elif (strategy == "describe") | (strategy == "summary"):
        inspector = DataInspector(DescribeInspectionStrategy())
        inspector.execute_inspection(df)
    else:
        print("Unknown strategy")

if __name__ == "__main__":
    data = {
        "Name":["youssef", "ali", "ahmed"],
        "Age" :[21, 27, 61]
    }
    df = pd.DataFrame(data)
    explore("info", df)
