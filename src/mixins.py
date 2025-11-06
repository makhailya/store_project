class CreationLoggerMixin:
    """Миксин, логирующий создание объектов."""

    def __init__(self, *args, **kwargs):
        class_name = self.__class__.__name__
        print(f"{class_name} создан с параметрами: {args}, {kwargs}")
        super().__init__(*args, **kwargs)
