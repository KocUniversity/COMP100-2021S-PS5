import json
from country import Country
from datetime import datetime

class Covid19Analyzer:

  def __init__(self):

    # This is your database. Keys are the country codes.
    self.db = {}

    with open("data.json") as f:
      data = json.load(f)

      for record in data['records']:

        #################################################
        #             YOUR CODE GOES HERE               #
        #################################################


    ## END OF LOADING DATA.JSON

    with open("agecases.json") as f:
      agecases = json.load(f)

      for record in agecases:

    #################################################
    #             YOUR CODE GOES HERE               #
    #################################################




  def process_big_data(self):

    most_exp_age_group_cnts = {}
    least_exp_age_group_cnts = {}

    top_case_cnt = 0
    top_death_cnt = 0
    top_case_country = ""
    top_death_country = ""

    #################################################
    #             YOUR CODE GOES HERE               #
    #################################################



    return top_death_country, top_death_cnt, top_case_country, top_case_cnt, most_age_group, least_age_group


  def print_summary(self):

    """
    Prints a tabulated summary of the processed data.

    :return:
    """
    print(f"Listing {len(self.db.keys())} countries.")

    for keys, values in self.db.items():
      print("===================================================")

      values.print_summary()


if __name__ == "__main__":
  analyzer = Covid19Analyzer()
  top_death_country, top_death_cnt, top_case_country, top_case_cnt, most_age_group, least_age_group = analyzer.process_big_data()

  print("Deaths per 1M Highest Country: ", top_death_country, " with ", top_death_cnt, " deaths/million")
  print("Cases per 1M Highest Country: ", top_case_country, " with ", top_case_cnt, " cases/million")
  print("Most Exposed Age Group In EU: ", most_age_group)
  print("Least Exposed Age Group In EU: ", least_age_group)

  analyzer.print_summary()