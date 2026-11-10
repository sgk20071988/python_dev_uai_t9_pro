import uuid

from classes.user import User


class AuthenticationService:
    """
    Сервис для управления регистрацией и аутентификацией пользователей.
    """
    def __init__(self):
        self.current_user = None
        self.session_token = None

    def register(self, user_class, username, email, password, *args):
        """
        Регистрация нового пользователя.
        """
        # Проверка уникальности имени пользователя
        for user in User.users:
            if user.username == username:
                return f"Ошибка: пользователь с именем '{username}' уже существует."

        # Создание нового пользователя (пароль хешируется в конструкторе)
        try:
            new_user = user_class(username, email, password, *args)
        except TypeError as e:
            return f"Ошибка при создании пользователя: {e}"

        User.users.append(new_user)
        return f"Пользователь '{username}' успешно зарегистрирован."

    def login(self, username, password):
        """
        Аутентификация пользователя.
        """
        for user in User.users:
            if user.username == username:
                if User.check_password(user.password, password):
                    self.current_user = user
                    self.session_token = str(uuid.uuid4())
                    return (f"Пользователь '{username}' успешно вошёл в систему. "
                            f"Токен сессии: {self.session_token}")
                return "Ошибка: неверный пароль."
        return f"Ошибка: пользователь '{username}' не найден."

    def logout(self):
        """
        Выход пользователя из системы.
        """
        if self.current_user is None:
            return "Ошибка: нет активной сессии."
        username = self.current_user.username
        self.current_user = None
        self.session_token = None
        return f"Пользователь '{username}' вышел из системы."

    def get_current_user(self):
        """
        Возвращает текущего вошедшего пользователя.
        """
        if self.current_user is None:
            return "Ошибка: нет активной сессии."
        return f"Текущий пользователь: {self.current_user.get_details()}"