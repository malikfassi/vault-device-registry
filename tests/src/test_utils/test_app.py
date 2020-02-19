from App import App



class TestApp(App):
    def __init__(self):
        super().__init__()
        self.config.update(TESTING=True)
        self.client = self.test_client()

    def create_tables(self):
        from src.common.base_model import Base
        Base.metadata.create_all(self.db.get_engine())

    def drop_tables(self):
        from src.common.base_model import Base
        self.db.session.remove()
        Base.metadata.drop_all(self.db.get_engine())
