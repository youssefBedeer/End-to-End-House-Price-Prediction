import pandas as pd 
import seaborn as sns
import matplotlib.pyplot as plt 
from abc import ABC, abstractmethod

# Template Pattern for missing value 
class MissingValuesAnalysisTemplate(ABC):
    def analyze(self, df:pd.DataFrame):
        """
        Performs a complete missing values analysis by identifying and visualizing missing values.

        Args:
            df (pd.DataFrame): The dataframe to be analyzed.

        Returns:
            None: This method performs the analysis and visualizes missing values.
        """

        self.IdentifyMissingValues(df)
        self.VisualizeMissingValues(df)

    @abstractmethod
    def IdentifyMissingValues(self, df:pd.DataFrame):
        pass 
    def VisualizeMissingValues(self, df:pd.DataFrame):
        pass

# concrete class for missing values Identification
# ------------------------------------------------
# Implemnt methods
class SimpleMissingValuesAnalysis(MissingValuesAnalysisTemplate):
    def IdentifyMissingValues(self, df:pd.DataFrame):
        print(f"{'*'*50}\nMissing Values Count By Column\n{'*'*50}")
        missing_values = df.isna().sum() 
        print(missing_values[missing_values > 0])
              
    def VisualizeMissingValues(self, df:pd.DataFrame):
        print(f"{'*'*50}\nVisualize Missing Values\n{'*'*50}")
        plt.figure(figsize=(12,8))
        sns.heatmap(df.isnull(), cbar=False, cmap="viridis")
        plt.title("Missing Values Heatmap")
        plt.show()

# user code 
def explore_missing_values( df:pd.DataFrame):
    """
    Performs a complete missing values analysis by identifying and visualizing missing values.

    Args:
        df (pd.DataFrame): The dataframe to be analyzed.

    Returns:
        None
    """
    missing_values_analyzer = SimpleMissingValuesAnalysis()
    missing_values_analyzer.analyze(df)

if __name__ == "__main__":
    pass
        
        

