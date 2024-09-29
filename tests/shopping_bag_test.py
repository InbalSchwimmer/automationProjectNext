from pages.home_category_page import HomeCategory


class ViewEditBag:
    def test_add_two_product_to_bag(self):
        shopper = HomeCategory(self.drive)
        shopper.open_living_room_subcategory()
