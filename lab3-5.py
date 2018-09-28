class shape:
    def __init__(self):
        print("shape constructor called")
    @staticmethod
    def printType():
        print("shape")

        class Rectangle(shape):
            def __init__(self):
                super().__init__()
                self.lenght=0
                self.width=0
                def draw(self):
                    print("draw rectangle")

                    class triangle(shape):
                        def __init__(self):
                            super().__init__()
                            self.a = 0
                            self.b = 0
                            self.c=0

                            def draw(self):
                                print("draw triangle")