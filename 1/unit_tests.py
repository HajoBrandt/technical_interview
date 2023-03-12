import unittest
import random
from main import Append_GDP_To_Dataframe, Calculate_Mean_Of_Age1stCode_Per_Country
class Correlation_Test(unittest.TestCase):
    def Correlation_Test(self):
        Mean_Of_Age1stCode_Per_Country = Calculate_Mean_Of_Age1stCode_Per_Country()
        Base_Data = Append_GDP_To_Dataframe(Mean_Of_Age1stCode_Per_Country)
        n = random.randint(10, 50)
        random_state = random.randint(10, 50)
        sample_df = Base_Data.sample(n=n, random_state=random_state)
        self.assertAlmostEqual(sample_df['GDP'].corr(sample_df['Age1stCode']), 0, delta=0.3)
if __name__ == '__main__':
    unittest.main()