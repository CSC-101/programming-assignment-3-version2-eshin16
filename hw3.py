from data import CountyDemographics
from build_data import get_data

# Part 1: the purpose of the function is to sum up the values of the 2014 population value from each object
# Inputs: list[CountyDemographics]
# Outputs: int of the total population value

def population_total(counties: list[CountyDemographics]) -> int:
    return sum(county.population for county in counties)

###############################################################################################################
# Part 2: the purpose of the function is to extract and return a list of demographic objects that belong to a state
# Input: list[CountyDemographics], str (2 letter abbreviation)
# Output: list[CountyDemographics]

def filter_by_state(counties: list[CountyDemographics], state_abbr: str) -> list[CountyDemographics]:
    return [county for county in counties if county.state == state_abbr]

###############################################################################################################
# Part 3:

# population_by_education: the purpose of the function is to calculate the total number of people with a specific education level across a specific county demographic
# Input: list[CountyDemographics], str
# Output: float

def population_by_education(counties: list[CountyDemographics], education_key: str) -> float:
    return sum(county.population for county in counties if county.education == education_key)

# population_by_ethnicity: the purpose of the function is to calculate the total 2014 population for a specific ethnic group
# Input: list[CountyDemographics], str
# Output: float (total sub-population)

# def population_by_ethnicity(counties: list[CountyDemographics], ethnicity_key: str) -> int:
#     return sum(county.ethnicities.get(ethnicity_key, 0) if isinstance(county.ethnicities, dict) else 0 for county in counties)

def population_by_ethnicity(counties: list[CountyDemographics], ethnicity_key: str) -> int:
    total = 0
    for county in counties:
        sub_population = county.ethnicities.get(ethnicity_key, 0) if isinstance(county.ethnicities, dict) else 0
        print(f"Checking {county.county}: {county.ethnicities}, Ethnicity: {ethnicity_key}, Sub-population: {sub_population}")
        total += sub_population
    print(f"Total for {ethnicity_key}: {total}")
    return total

# population_below_poverty_level: the purpose is to calculate the total number of people living below the poverty level
# Input: list[CountyDemographics]
# Output: total population below poverty level

def population_below_poverty_level(counties: list[CountyDemographics]) -> float:
    total_poverty_population = 0

    for county in counties:
        if isinstance(county.income, dict) and 'Persons Below Poverty Level' in county.income:
            total_poverty_population += county.income['Persons Below Poverty Level']

    return total_poverty_population

###############################################################################################################
# Part 4:

# percent_by_education: the purpose of this function is to calculate the percentage of people who have received a certain level of education in 2014
# Input: list[CountyDemographics], str
# Output: percentage of specified education level population out of total population

def percent_by_education(county_demographics, education_key):
    total_population = sum(county.get('Total Population', 0) for county in county_demographics)

    # Debugging print statement
    for county in county_demographics:
        print("Checking county data:", county)

    education_population = sum(county.get('Education', {}).get(education_key, 0) for county in county_demographics)

    if total_population == 0:
        return 0

    return (education_population / total_population) * 100

# percent_by_ethnicity: the purpose of the function is to calculate the percentage of a specific ethnic group compared to the total population
# Input: list[CountyDemographics], str (ethnicity key of interest)
# Output: percentage of the specified ethnicity population out of the total population

def percent_by_ethnicity(county_demographics, ethnicity_key):

    total_population = sum(county.get('Total Population', 0) for county in county_demographics)
    ethnicity_population = sum(county.get('Ethnicity', {}).get(ethnicity_key, 0) for county in county_demographics)

    if total_population == 0:
        return 0

    return (ethnicity_population / total_population) * 100

# percent_below_poverty_level: the purpose of the function is to calculate the percentage of the population below poverty level across counties
# Input: list[CountyDemographics]
# Output: float (percentage of the population below poverty level out of the total population)

def percent_below_poverty_level(county_demographics):
    total_population = sum(county.get('Total Population', 0) for county in county_demographics)
    poverty_population = population_below_poverty_level(county_demographics)

    if total_population == 0:
        return 0

    return (poverty_population / total_population) * 100

###############################################################################################################
# Part 5

# education_greater_than: the purpose of the function is to return a list of counties where the specified education level percentage is greater than the threshold
# Inputs: list of dictionaries containing county demographic data, the key representing the education level of interest, and the numeric threshold value.
# Outputs: list of county demographics objects that exceed the threshold.

def education_greater_than(county_demographics, education_key, threshold):
    return [county for county in county_demographics if county.get('Education', {}).get(education_key, 0) > threshold]

# education_less_than: the purpose of the function is to return a list of counties where the specified education level percentage is less than the threshold
# Inputs: list of dictionaries containing county demographic data, the key representing the education level of interest, the numeric threshold value.
# Output: list of county demographics objects that fall below the threshold.

def education_less_than(county_demographics, education_key, threshold):
    return [county for county in county_demographics if county.get('Education', {}).get(education_key, 0) < threshold]

# ethnicity_greater_than: the purpose of the function is to return a list of counties where the percentage of a specified ethnicity exceeds a given threshold.
# Inputs: list of dictionaries containing county demographic data, the key representing the ethnicity of interest, the numeric threshold value
# Outputs: list of county demographics objects that exceed the threshold

def ethnicity_greater_than(county_demographics, ethnicity_key, threshold):
    return [county for county in county_demographics if county.get('Ethnicity', {}).get(ethnicity_key, 0) > threshold]

# ethnicity_less_than: the purpose of the function is to return a list of counties where the percentage of a specified ethnicity is below a given threshold
# Inputs: list of dictionaries containing county demographic data, the key representing the ethnicity of interest, the numeric threshold value
# Outputs: list of county demographics objects that fall below the threshold.

def ethnicity_less_than(county_demographics, ethnicity_key, threshold):
    return [county for county in county_demographics if county.get('Ethnicity', {}).get(ethnicity_key, 0) < threshold]

# below_poverty_level_greater_than: the purpose of the function is to return a list of counties where the population below the poverty level is greater than the threshold
# Inputs: list of dictionaries containing county demographic data, the numeric threshold value
# Outputs: list of county demographics objects that exceed the threshold

def below_poverty_level_greater_than(county_demographics, threshold):
    return [county for county in county_demographics if
            county.get('Income', {}).get('Persons Below Poverty Level', 0) > threshold]

# below_poverty_level_less_than: the purpose of the function is to return a list of counties where the population below the poverty level is less than the threshold
# Inputs: list of dictionaries containing county demographic data, the numeric threshold value
# Outputs: list of county demographics objects that fall below the threshold

def below_poverty_level_less_than(county_demographics, threshold):
    return [county for county in county_demographics if
            county.get('Income', {}).get('Persons Below Poverty Level', 0) < threshold]
