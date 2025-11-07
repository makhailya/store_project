class CreationLoggerMixin:
    """Миксин, логирующий создание объектов и предоставляющий repr."""

    def __init__(self, *args, **kwargs):
        class_name = self.__class__.__name__
        print(f"{class_name} создан с параметрами: {args}, {kwargs}")
        super().__init__(*args, **kwargs)

    def __repr__(self):
        """Возвращает строковое представление объекта."""
        class_name = self.__class__.__name__
        attrs = ", ".join(f"{k}={v!r}" for k, v in self.__dict__.items())
        return f"{class_name}({attrs})"
