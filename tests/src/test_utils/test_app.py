from App import App


class TestApp(App):
    def __init__(self):
        super().__init__()
        self.config.update(TESTING=True)
        self.client = self.test_client()

    def drop_tables(self):
        self.db.drop_all_tables()

    def create_tables(self):
        print("creating tables")
        self.db.create_all_tables()
