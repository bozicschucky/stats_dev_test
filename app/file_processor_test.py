import unittest
from file_processor import RecipeAnalyzer

class TestRecipeAnalyzer(unittest.TestCase):
    def setUp(self):
        # create a test instance of the class with some dummy data
        self.data = [
            {
                "postcode": "10224",
                "recipe": "Creamy Dill Chicken",
                "delivery": "Wednesday 1AM - 7PM"
            },
            {
                "postcode": "10208",
                "recipe": "Speedy Steak Fajitas",
                "delivery": "Thursday 7AM - 5PM"
            },
            {
                "postcode": "10120",
                "recipe": "Cherry Balsamic Pork Chops",
                "delivery": "Thursday 7AM - 9PM"
            },
            {
                "postcode": "10186",
                "recipe": "Cherry Balsamic Pork Chops",
                "delivery": "Saturday 1AM - 8PM"
            },
            {
                "postcode": "10127",
                "recipe": "Grilled Cheese and Veggie Jumble",
                "delivery": "Saturday 8AM - 1PM"
            },
            {
                "postcode": "10117",
                "recipe": "Speedy Steak Fajitas",
                "delivery": "Monday 10AM - 9PM"
            },
            {
                "postcode": "10124",
                "recipe": "Melty Monterey Jack Burgers",
                "delivery": "Wednesday 9AM - 6PM"
            },
            {
                "postcode": "10198",
                "recipe": "Korean-Style Chicken Thighs",
                "delivery": "Wednesday 3AM - 11PM"
            },
        ]
        self.analyzer = RecipeAnalyzer(self.data)
        self.analyzer.analyze()

    def test_count_unique_recipes(self):
        # test the count of unique recipes
        expected = 6
        actual = self.analyzer.unique_recipe_count
        self.assertEqual(expected, actual)

    def test_count_per_recipe(self):
        # test the count per recipe list
        expected = [
            {
                "recipe": "Cherry Balsamic Pork Chops",
                "count": 2
            },
            {
                "recipe": "Creamy Dill Chicken",
                "count": 1
            },
            {
                "recipe": "Grilled Cheese and Veggie Jumble",
                "count": 1
            },
            {
                "recipe": "Korean-Style Chicken Thighs",
                "count": 1
            },
            {
                "recipe": "Melty Monterey Jack Burgers",
                "count": 1
            },
            {
                "recipe": "Speedy Steak Fajitas",
                "count": 2
            }
        ]
        actual = self.analyzer.count_per_recipe
        self.assertEqual(expected, actual)

    def test_find_busiest_postcode(self):
        # test the busiest postcode dictionary
        expected = {
            'postcode': '10224',
            'delivery_count': 1
        }
        actual = self.analyzer.busiest_postcode
        self.assertEqual(expected, actual)

    def test_match_by_name(self):
        # test the match by name list
        expected = [
            'Grilled Cheese and Veggie Jumble',
        ]
        actual = self.analyzer.match_by_name
        self.assertEqual(expected, actual)

if __name__ == "__main__":
    unittest.main()
