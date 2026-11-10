import hashlib


class User:
    """
    Базовый класс, представляющий пользователя.
    """
    users = []  # Список для хранения всех пользователей

    def __init__(self, username, email, password):
        self.username = username
        self.email = email
        self.password = self.hash_password(password)

    @staticmethod
    def hash_password(password):
        """Хеширование пароля с использованием SHA-256."""
        return hashlib.sha256(password.encode()).hexdigest()

    @staticmethod
    def check_password(stored_password, provided_password):
        """
        Проверка пароля.
        """
        return stored_password == hashlib.sha256(provided_password.encode()).hexdigest()

    def get_details(self):
        return f"Username: {self.username}, Email: {self.email}"

