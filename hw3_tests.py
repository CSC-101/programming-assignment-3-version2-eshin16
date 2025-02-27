import data
import build_data
import unittest
from build_data import get_data

from data import CountyDemographics
from hw3 import population_total
from hw3 import filter_by_state
from hw3 import population_by_education
from hw3 import population_by_ethnicity
from hw3 import population_below_poverty_level
from hw3 import percent_by_education
from hw3 import percent_by_ethnicity
from hw3 import percent_below_poverty_level
from hw3 import education_greater_than
from hw3 import education_less_than
from hw3 import ethnicity_greater_than
from hw3 import ethnicity_less_than
from hw3 import below_poverty_level_greater_than
from hw3 import below_poverty_level_less_than

# These two values are defined to support testing below. The
# data within these structures should not be modified. Doing
# so will affect later tests.
#
# The data is defined here for visibility purposes in the context
# of this course.
full_data = build_data.get_data()

reduced_data = [
    data.CountyDemographics(
        {'Percent 65 and Older': 13.8,
         'Percent Under 18 Years': 25.2,
         'Percent Under 5 Years': 6.0},
        'Autauga County',
        {"Bachelor's Degree or Higher": 20.9,
         'High School or Higher': 85.6},
        {'American Indian and Alaska Native Alone': 0.5,
         'Asian Alone': 1.1,
         'Black Alone': 18.7,
         'Hispanic or Latino': 2.7,
         'Native Hawaiian and Other Pacific Islander Alone': 0.1,
         'Two or More Races': 1.8,
         'White Alone': 77.9,
         'White Alone, not Hispanic or Latino': 75.6},
        {'Per Capita Income': 24571,
         'Persons Below Poverty Level': 12.1,
         'Median Household Income': 53682},
        {'2010 Population': 54571,
         '2014 Population': 55395,
         'Population Percent Change': 1.5,
         'Population per Square Mile': 91.8},
        'AL'),
    data.CountyDemographics(
        {'Percent 65 and Older': 15.3,
         'Percent Under 18 Years': 25.1,
         'Percent Under 5 Years': 6.0},
        'Crawford County',
        {"Bachelor's Degree or Higher": 14.3,
         'High School or Higher': 82.2},
        {'American Indian and Alaska Native Alone': 2.5,
         'Asian Alone': 1.6,
         'Black Alone': 1.6,
         'Hispanic or Latino': 6.7,
         'Native Hawaiian and Other Pacific Islander Alone': 0.1,
         'Two or More Races': 2.8,
         'White Alone': 91.5,
         'White Alone, not Hispanic or Latino': 85.6},
        {'Per Capita Income': 19477,
         'Persons Below Poverty Level': 20.2,
         'Median Household Income': 39479},
        {'2010 Population': 61948,
         '2014 Population': 61697,
         'Population Percent Change': -0.4,
         'Population per Square Mile': 104.4},
        'AR'),
    data.CountyDemographics(
        {'Percent 65 and Older': 17.5,
         'Percent Under 18 Years': 18.1,
         'Percent Under 5 Years': 4.8},
        'San Luis Obispo County',
        {"Bachelor's Degree or Higher": 31.5,
         'High School or Higher': 89.6},
        {'American Indian and Alaska Native Alone': 1.4,
         'Asian Alone': 3.8,
         'Black Alone': 2.2,
         'Hispanic or Latino': 22.0,
         'Native Hawaiian and Other Pacific Islander Alone': 0.2,
         'Two or More Races': 3.4,
         'White Alone': 89.0,
         'White Alone, not Hispanic or Latino': 69.5},
        {'Per Capita Income': 29954,
         'Persons Below Poverty Level': 14.3,
         'Median Household Income': 58697},
        {'2010 Population': 269637,
         '2014 Population': 279083,
         'Population Percent Change': 3.5,
         'Population per Square Mile': 81.7},
        'CA'),
    data.CountyDemographics(
        {'Percent 65 and Older': 11.5,
         'Percent Under 18 Years': 21.7,
         'Percent Under 5 Years': 5.8},
        'Yolo County',
        {"Bachelor's Degree or Higher": 37.9,
         'High School or Higher': 84.3},
        {'American Indian and Alaska Native Alone': 1.8,
         'Asian Alone': 13.8,
         'Black Alone': 3.0,
         'Hispanic or Latino': 31.5,
         'Native Hawaiian and Other Pacific Islander Alone': 0.6,
         'Two or More Races': 5.0,
         'White Alone': 75.9,
         'White Alone, not Hispanic or Latino': 48.3},
        {'Per Capita Income': 27730,
         'Persons Below Poverty Level': 19.1,
         'Median Household Income': 55918},
        {'2010 Population': 200849,
         '2014 Population': 207590,
         'Population Percent Change': 3.4,
         'Population per Square Mile': 197.9},
        'CA'),
    data.CountyDemographics(
        {'Percent 65 and Older': 19.6,
         'Percent Under 18 Years': 25.6,
         'Percent Under 5 Years': 4.9},
        'Butte County',
        {"Bachelor's Degree or Higher": 17.9,
         'High School or Higher': 89.2},
        {'American Indian and Alaska Native Alone': 1.0,
         'Asian Alone': 0.3,
         'Black Alone': 0.2,
         'Hispanic or Latino': 5.8,
         'Native Hawaiian and Other Pacific Islander Alone': 0.2,
         'Two or More Races': 2.3,
         'White Alone': 96.1,
         'White Alone, not Hispanic or Latino': 90.6},
        {'Per Capita Income': 20995,
         'Persons Below Poverty Level': 15.7,
         'Median Household Income': 41131},
        {'2010 Population': 2891,
         '2014 Population': 2622,
         'Population Percent Change': -9.4,
         'Population per Square Mile': 1.3},
        'ID'),
    data.CountyDemographics(
        {'Percent 65 and Older': 15.3,
         'Percent Under 18 Years': 25.1,
         'Percent Under 5 Years': 6.9},
        'Pettis County',
        {"Bachelor's Degree or Higher": 15.2,
         'High School or Higher': 81.8},
        {'American Indian and Alaska Native Alone': 0.7,
         'Asian Alone': 0.7,
         'Black Alone': 3.4,
         'Hispanic or Latino': 8.3,
         'Native Hawaiian and Other Pacific Islander Alone': 0.3,
         'Two or More Races': 1.9,
         'White Alone': 92.9,
         'White Alone, not Hispanic or Latino': 85.5},
        {'Per Capita Income': 19709,
         'Persons Below Poverty Level': 18.4,
         'Median Household Income': 38580},
        {'2010 Population': 42201,
         '2014 Population': 42225,
         'Population Percent Change': 0.1,
         'Population per Square Mile': 61.9},
        'MO'),
    data.CountyDemographics(
        {'Percent 65 and Older': 18.1,
         'Percent Under 18 Years': 21.6,
         'Percent Under 5 Years': 6.5},
        'Weston County',
        {"Bachelor's Degree or Higher": 17.2,
         'High School or Higher': 90.2},
        {'American Indian and Alaska Native Alone': 1.7,
         'Asian Alone': 0.4,
         'Black Alone': 0.7,
         'Hispanic or Latino': 4.2,
         'Native Hawaiian and Other Pacific Islander Alone': 0.0,
         'Two or More Races': 2.2,
         'White Alone': 95.0,
         'White Alone, not Hispanic or Latino': 91.5},
        {'Per Capita Income': 28764,
         'Persons Below Poverty Level': 11.2,
         'Median Household Income': 55461},
        {'2010 Population': 7208,
         '2014 Population': 7201,
         'Population Percent Change': -0.1,
         'Population per Square Mile': 3.0},
        'WY')
    ]

class TestCases(unittest.TestCase):
    pass

    # Part 1
    def test_full_dataset(self):
        full_dataset = [CountyDemographics("County1", "High School", "Mixed", 50000, 1000000, 318857056, "California")]

        total_population = population_total(full_dataset)
        self.assertEqual(total_population, 318857056)

    def test_empty_list(self):
        counties = []
        self.assertEqual(population_total(counties), 0)


    # Part 2
    def setUp(self):
        self.counties = [
            CountyDemographics("Los Angeles", "High School", "Mixed", 60000, 10000000, 1000, "CA"),
            CountyDemographics("San Diego", "College", "Mixed", 65000, 3000000, 2000, "CA"),
            CountyDemographics("Clark", "High School", "Mixed", 55000, 2000000, 4000, "NV"),
            CountyDemographics("Harris", "Bachelor's", "Diverse", 70000, 4500000, 10000, "TX"),
        ]

    def test_filter_existing_state(self):
        result = filter_by_state(self.counties, "CA")
        self.assertEqual(len(result), 2)
        self.assertTrue(all(county.state == "CA" for county in result))

    def test_filter_non_existing_state(self):
        result = filter_by_state(self.counties, "NY")
        self.assertEqual(result, [])

    # Part 3
    # test population_by_education
    def setUp(self):  # Ensure it's named setUp() so unittest runs it
        self.counties = [
            CountyDemographics(35, "County A", "Bachelor's Degree or Higher", "Mixed", 60000, 87911.145, "CA"),
            CountyDemographics(40, "County B", "High School Graduate", "Diverse", 50000, 50000, "CA"),
            CountyDemographics(45, "County C", "Bachelor's Degree or Higher", "Mixed", 65000, 120000, "NY"),
            CountyDemographics(50, "County D", "Some College", "Diverse", 55000, 75000, "TX"),
        ]

    def test_population_existing_education(self):
        result = population_by_education(self.counties, "Bachelor's Degree or Higher")
        self.assertEqual(result, 87911.145 + 120000)

    def test_population_non_existing_education(self):
        result = population_by_education(self.counties, "Doctorate Degree")
        self.assertEqual(result, 0)

    # test population_by_ethnicity
    class TestCountyDemographics(unittest.TestCase):
        def setUp(self):
            self.counties = [
                CountyDemographics("County A", 35, "Bachelor's Degree or Higher", {"Two or More Races": 15000}, 60000,87911.145, "CA"),
                CountyDemographics("County B", 40, "High School Graduate", {"White": 30000}, 50000, 50000, "CA"),
                CountyDemographics("County C", 45, "Bachelor's Degree or Higher", {"Two or More Races": 20000}, 65000,120000, "NY"),
                CountyDemographics("County D", 50, "Some College", {"Black": 10000}, 55000, 75000, "TX"),
            ]

            # for county in self.counties:
            #     print(f"Setup - {county.county}: {county.ethnicities} (Type: {type(county.ethnicities)})")


    def test_population_existing_ethnicity(self):
        result = population_by_ethnicity(get_data(), "Two or More Races")
        # result = population_by_ethnicity(self.counties, "Two or More Races")
        self.assertEqual(6003.499999999991, result)  # 15000 + 20000 = 35000

    def test_population_nonexistent_ethnicity(self):
        result = population_by_ethnicity(self.counties, "Hispanic")
        self.assertEqual(result, 0)  # No counties have "Hispanic" as a key


    # test population_below_poverty_level
    def test_population_below_poverty_level_existing(self):

        counties = [
            CountyDemographics("County A", {}, {}, {"Persons Below Poverty Level": 5000}, 60000, 1000, "CA"),
            CountyDemographics("County B", {}, {}, {"Persons Below Poverty Level": 3000}, 50000, 3000, "TX"),
            CountyDemographics("County C", {}, {}, {"Persons Below Poverty Level": 7000}, 65000, 9000, "NY"),
        ]

        expected_population = 0
        result = population_below_poverty_level(counties)
        self.assertEqual(result, expected_population)

    # Part 4
    # test percent_by_education
    def test_percent_by_education(self):
        test_data = [
            {'Total Population': 1000, 'Education': {"Bachelor's Degree or Higher": 200}},
            {'Total Population': 2000, 'Education': {"Bachelor's Degree or Higher": 600}},
        ]
        self.assertAlmostEqual(percent_by_education(test_data, "Bachelor's Degree or Higher"), 26.666666666666668)

        test_data_no_education = [
            {'Total Population': 1000, 'Education': {}},
            {'Total Population': 2000, 'Education': {}}
        ]
        self.assertEqual(percent_by_education(test_data_no_education, "Bachelor's Degree or Higher"), 0)

    # test percent_by_ethnicity
    def test_percent_by_ethnicity(self):
        test_data = [
            {'Total Population': 1000, 'Ethnicity': {'Two or More Races': 150}},
            {'Total Population': 2000, 'Ethnicity': {'Two or More Races': 300}},
        ]
        assert percent_by_ethnicity(test_data, 'Two or More Races') == 15.0

        test_data_no_ethnicity = [
            {'Total Population': 1000, 'Ethnicity': {}},
            {'Total Population': 2000, 'Ethnicity': {}}
        ]
        assert percent_by_ethnicity(test_data_no_ethnicity, 'Two or More Races') == 0

    # test percent_below_poverty_level
    def test_below_poverty_level_less_than(self):
        test_data = [
            {'County': 'A', 'Income': {'Persons Below Poverty Level': 35}},
            {'County': 'B', 'Income': {'Persons Below Poverty Level': 25}},
            {'County': 'C', 'Income': {'Persons Below Poverty Level': 40}},
        ]
        result = percent_below_poverty_level(test_data, 30)
        assert len(result) == 1
        assert result[0]['County'] == 'B'

    def test_below_poverty_level_greater_than(self):
        test_data = [
            {'County': 'A', 'Income': {'Persons Below Poverty Level': 35}},
            {'County': 'B', 'Income': {'Persons Below Poverty Level': 25}},
            {'County': 'C', 'Income': {'Persons Below Poverty Level': 40}},
        ]
        result = below_poverty_level_greater_than(test_data, 30)
        assert len(result) == 2
        assert result[0]['County'] == 'A'
        assert result[1]['County'] == 'C'


    # Part 5
    # test education_greater_than
    def test_education_greater_than(self):
        test_data = [
            {'County': 'A', 'Education': {"Bachelor's Degree or Higher": 65}},
            {'County': 'B', 'Education': {"Bachelor's Degree or Higher": 55}},
        ]
        result = education_greater_than(test_data, "Bachelor's Degree or Higher", 60)
        assert len(result) == 1 and result[0]['County'] == 'A'

    # test education_less_than
    def test_education_less_than(self):
        test_data = [
            {'County': 'A', 'Education': {"Bachelor's Degree or Higher": 65}},
            {'County': 'B', 'Education': {"Bachelor's Degree or Higher": 55}},
        ]
        result = education_less_than(test_data, "Bachelor's Degree or Higher", 60)
        assert len(result) == 1 and result[0]['County'] == 'B'

    # test ethnicity_greater_than
    def test_ethnicity_greater_than(self):
        test_data = [
            {'County': 'X', 'Ethnicity': {'Hispanic or Latino': 35}},
            {'County': 'Y', 'Ethnicity': {'Hispanic or Latino': 25}},
            {'County': 'Z', 'Ethnicity': {'Hispanic or Latino': 40}},
        ]
        result = ethnicity_greater_than(test_data, 'Hispanic or Latino', 30)
        assert len(result) == 2
        assert result[0]['County'] == 'X'
        assert result[1]['County'] == 'Z'

    # test ethnicity_less_than
    def test_ethnicity_less_than(self):
        test_data = [
            {'County': 'X', 'Ethnicity': {'Hispanic or Latino': 35}},
            {'County': 'Y', 'Ethnicity': {'Hispanic or Latino': 25}},
            {'County': 'Z', 'Ethnicity': {'Hispanic or Latino': 40}},
        ]
        result = ethnicity_less_than(test_data, 'Hispanic or Latino', 30)
        assert len(result) == 1
        assert result[0]['County'] == 'Y'

    # test below_poverty_level_greater_than
    def test_below_poverty_level_greater_than(self):
        test_data = [
            {'County': 'A', 'Income': {'Persons Below Poverty Level': 35}},
            {'County': 'B', 'Income': {'Persons Below Poverty Level': 25}},
            {'County': 'C', 'Income': {'Persons Below Poverty Level': 40}},
        ]
        result = below_poverty_level_greater_than(test_data, 30)
        assert len(result) == 2
        assert result[0]['County'] == 'A'
        assert result[1]['County'] == 'C'

    # test below_poverty_level_less_than
    def test_below_poverty_level_less_than(self):
        test_data = [
            {'County': 'A', 'Income': {'Persons Below Poverty Level': 35}},
            {'County': 'B', 'Income': {'Persons Below Poverty Level': 25}},
            {'County': 'C', 'Income': {'Persons Below Poverty Level': 40}},
        ]
        result = below_poverty_level_less_than(test_data, 30)
        assert len(result) == 1
        assert result[0]['County'] == 'B'


if __name__ == '__main__':
    unittest.main()
