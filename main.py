import StudiKasus2
import os

if __name__ == "__main__":
    case = StudiKasus2.StudiKasus2("localhost", "3306", "root", os.environ["MySQL_Pswd"])
    df = case.import_csv("covid.csv")
    print(case.create_db("covidCase1"))
    print(case.create_table("covidCase1", "case1", df))
    print(case.load_data("covidCase1", "case1"))
    print(help(StudiKasus2))
