class RecipeAnalyzer:
    def __init__(self, data):
        self.data = data
        self.unique_recipe_count = 0
        self.count_per_recipe = []
        self.busiest_postcode = {}
        self.match_by_name = []

    def analyze(self):
        # perform the analysis and update the attributes
        self.get_count_unique_recipes()
        self.get_count_per_recipe()
        self.find_busiest_postcode()
        self.get_match_by_name()

    def get_count_unique_recipes(self):
        recipe_set = set()
        for item in self.data:
            recipe_set.add(item["recipe"])
        self.unique_recipe_count = len(recipe_set)

    def get_count_per_recipe(self):
        # `RecipeAnalyzer` class. This method counts the number of occurrences for each unique recipe
        # name in the given data, and then sorts the results alphabetically by recipe name.
        recipe_dict = {}
        for item in self.data:
            recipe = item["recipe"]
            if recipe not in recipe_dict:
                recipe_dict[recipe] = 0
            recipe_dict[recipe] += 1
        # sort the dictionary by key (recipe name) and convert to a list of dictionaries
        sorted_list = sorted(recipe_dict.items(), key=lambda x: x[0])
        for name, count in sorted_list:
            self.count_per_recipe.append({"recipe": name, "count": count})

    def find_busiest_postcode(self):
        # find the postcode with most delivered recipes
        postcode_dict = {}
        for item in self.data:
            postcode = item["postcode"]
            if postcode not in postcode_dict:
                postcode_dict[postcode] = 0
            postcode_dict[postcode] += 1

        # find the maximum value and the corresponding key in the dictionary
        max_count = 0
        max_postcode = None
        for postcode, count in postcode_dict.items():
            if count > max_count:
                max_count = count
                max_postcode = postcode
        self.busiest_postcode = {
            "postcode": max_postcode, "delivery_count": max_count}

    def get_match_by_name(self):
        # list the recipe names (alphabetically ordered) that contain in their name one of the following words: Potato, Veggie ,Mushroom
        keywords = ["Potato", "Veggie", "Mushroom"]
        for item in self.data:
            recipe = item["recipe"]
            for word in keywords:
                if word in recipe and recipe not in self.match_by_name:
                    self.match_by_name.append(recipe)
                    break  # avoid duplicates
        # sort the list alphabetically
        self.match_by_name.sort()

    def get_output(self):
        # return a dictionary with the expected output format
        output = {
            "unique_recipe_count": str(self.unique_recipe_count),
            "count_per_recipe": self.count_per_recipe,
            "busiest_postcode": self.busiest_postcode,
            "match_by_name": self.match_by_name
        }
        return output
