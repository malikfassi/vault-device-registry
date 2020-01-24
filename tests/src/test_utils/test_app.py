from App import App


class TestApp(App):
    def __init__(self):
        super().__init__()
        self.client = self.test_client()

    def clear_database(self):
        # self.db.db_instance.drop_tables(self.tables, cascade=True)
        pass

    def create_tables(self):
        # self.db.db_instance.create_tables(self.tables, safe=True)
        pass
