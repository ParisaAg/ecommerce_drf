

class TestCategoryModel:
    def test_str_method(self,category_factory):
        x=category_factory()
        assert x.__str__()=='test_category'