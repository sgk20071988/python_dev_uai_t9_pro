from classes.user import User


class Admin(User):
    """
    Класс, представляющий администратора, наследующий класс User.
    """
    def __init__(self, username, email, password, admin_level):
        super().__init__(username, email, password)
        self.admin_level = admin_level

    def get_details(self):
        return f"Admin | {super().get_details()}, Admin Level: {self.admin_level}"

    @staticmethod
    def list_users():
        """
        Выводит список всех пользователей.
        """
        if not User.users:
            print("Список пользователей пуст.")
            return
        print("Список всех пользователей:")
        for user in User.users:
            print(f" - {user.get_details()}")

    @staticmethod
    def delete_user(username):
        """
        Удаляет пользователя по имени пользователя.
        """
        for user in User.users:
            if user.username == username:
                User.users.remove(user)
                return f"Пользователь '{username}' успешно удалён."
        return f"Пользователь '{username}' не найден."