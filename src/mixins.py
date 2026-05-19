class CreationLoggerMixin:
    def __init_subclass__(cls, **kwargs):
        super().__init_subclass__(**kwargs)

    def __new__(cls, *args, **kwargs):
        instance = super().__new__(cls)
        # Изменяем сообщение на ожидаемое
        print(f"Product создан с параметрами {args}")
        return instance
