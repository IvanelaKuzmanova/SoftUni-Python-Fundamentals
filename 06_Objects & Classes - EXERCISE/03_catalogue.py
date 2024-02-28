class Catalogue:
    def __init__(self, name:str):
        self.name = name
        self.products = []

    def add_product(self, product_name: str):
        self.products.append(product_name)

    def get_by_letter(self, first_letter: str):
        filtered_list = [item for item in self.products if item[0] == first_letter]
        return filtered_list

    def __repr__(self):
        item_name = "\n".join(sorted(self.products))        #defining helping variable for the list from which each item needs to be printed on new row; and sorting the list as per description
        return f'Items in the {self.name} catalogue:\n{item_name}'


# catalogue = Catalogue("Furniture")
# catalogue.add_product("Sofa")
# catalogue.add_product("Mirror")
# catalogue.add_product("Desk")
# catalogue.add_product("Chair")
# catalogue.add_product("Carpet")
# print(catalogue.get_by_letter("C"))
# print(catalogue)
