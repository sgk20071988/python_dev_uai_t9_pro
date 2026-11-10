from classes.admin import Admin
from classes.authservice import AuthenticationService
from classes.customer import Customer


def main():
    auth_service = AuthenticationService()

    print("=== Регистрация ===")
    print(auth_service.register(Customer, "alice", "alice@mail.com", "pass123", "ул. Ленина, 1"))
    print(auth_service.register(Admin, "bob", "bob@mail.com", "adminpass", 1))
    print(auth_service.register(Customer, "alice", "alice2@mail.com", "pass456", "ул. Мира, 5"))  # дубликат

    print("\n=== Аутентификация ===")
    print(auth_service.login("alice", "wrongpass"))   # неверный пароль
    print(auth_service.login("alice", "pass123"))     # успех
    print(auth_service.get_current_user())

    print("\n=== Управление сессией ===")
    print(auth_service.logout())
    print(auth_service.get_current_user())

    print("\n=== Административные функции ===")
    print(auth_service.login("bob", "adminpass"))
    print(auth_service.get_current_user())

    print("\n--- Список пользователей (доступно админу) ---")
    Admin.list_users()

    print("\n--- Удаление пользователя ---")
    print(Admin.delete_user("alice"))
    Admin.list_users()

    print("\n--- Удаление несуществующего пользователя ---")
    print(Admin.delete_user("charlie"))

if __name__ == "__main__":
    main()