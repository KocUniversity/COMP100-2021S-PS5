class Country:

  def __init__(self, name, population):

    self.name = name
    self.population = population
    self.population_by_agegroup = {'<15yr': -1, '15-24yr':-1, '25-49yr':-1, '50-64yr':-1, '65-79yr':-1, '80+yr':-1}
    self.daily_records = []
    self.weekly_records = {'<15yr' : [], '15-24yr': [], '25-49yr': [], '50-64yr': [], '65-79yr':[], '80+yr':[]}

  def daily_records_to_string(self, idxs):

    output_str = ""
    for idx in idxs:
      record = self.daily_records[idx]
      output_str += f"Date: {record['date']}, Cases: {record['cases']}, Deaths: {record['deaths']} \n"

    return output_str

  def save_daily_data(self, date, cases, deaths):

    """
    Saves daily data.
    :param date: (string) e.g. (27/03/2021).
    :param cases: (int) e.g.(3221)
    :param deaths: (int) e.g. (231)
    :return: None
    """

    self.daily_records.append({'date': date, 'cases': cases, 'deaths': deaths})

  def save_weekly_data(self, age_group, year_week, new_cases):

    self.weekly_records[age_group].append({'year_week': year_week, 'new_cases': new_cases}),

  def get_total_cases(self):

    #################################################
    #             YOUR CODE GOES HERE               #
    #################################################

    return case_cnt

  def get_total_deaths(self):

    #################################################
    #             YOUR CODE GOES HERE               #
    #################################################

    return death_cnt

  def total_cases_and_deaths_per_1m(self):

    #################################################
    #             YOUR CODE GOES HERE               #
    #################################################

    return int(case_cnt), int(death_cnt)

  def sort_records_by(self, param):

    # Gives you a list of cases or deaths depending on param
    nums = [record[param] for record in self.daily_records]

    #################################################
    #             YOUR CODE GOES HERE               #
    #################################################

    return indexes

  def find_top_k_cases(self, k):

    idxs = self.sort_records_by("cases")[-k:]
    out = self.daily_records_to_string(idxs)

    return out

  def find_top_k_deaths(self, k):

    idxs = self.sort_records_by("cases")[-k:]
    out = self.daily_records_to_string(idxs)

    return out

  def calc_exposure_per_age_group(self):

    #################################################
    #             YOUR CODE GOES HERE               #
    #################################################

    pass

  def find_most_exposed_age_group(self):

    #################################################
    #             YOUR CODE GOES HERE               #
    #################################################

    pass

  def find_least_exposed_age_group(self):

    #################################################
    #             YOUR CODE GOES HERE               #
    #################################################

    pass

  def calc_prob_of_cases_per_age_group(self):

    #################################################
    #             YOUR CODE GOES HERE               #
    #################################################

    pass

  def distribute_deaths_to_age_groups(self):
    case_probs = self.calc_prob_of_cases_per_age_group()
    death_probs = [0.05, 0.05, 0.1, 0.2, 0.25, 0.35]
    conditionals = {}

    #################################################
    #             YOUR CODE GOES HERE               #
    #################################################

    return death_cnt, conditionals

  def print_summary(self):


    print("Country name: ", self.name)
    print("Showing data between: ", self.daily_records[-1]['date'], " - ", self.daily_records[0]['date'] )
    cases1m, deaths1m = self.total_cases_and_deaths_per_1m()
    print(f"Total cases per 1M: {cases1m}, total deaths per 1M: {deaths1m}")
    print("Most exposed age group: ", self.find_most_exposed_age_group())
    print("Least exposed age group: ", self.find_least_exposed_age_group())
    print('')
    print("Top 5 Cases:")
    print(self.find_top_k_cases(5))
    print("Top 5 Deaths:")
    print(self.find_top_k_deaths(5))

    deaths, distribution = self.distribute_deaths_to_age_groups()
    print("Total deaths: ", deaths)
    print("Estimated distribution: ", distribution)