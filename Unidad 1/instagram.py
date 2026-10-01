class user:

    def __init__(self, name, __password, number, age, email):
        self.name = name
        self.__password = __password
        self.number = number
        self.age = age
        self.email = email

    def exception(self, name):
        for character in name:
            if character.isdigit():
                raise ValueError("Name cannot contain numbers")
            else:
                print(f"Name: {self.name} approved")

    def create_post(self, title, content):
        self.title = title
        self.content = content


class Post:
    def __init__(self, text, date, images, likes):
        self.text = text
        self.date = date
        self.images = images
        self.likes = likes

    def badword(self, text):
        bad_words = ["badword1", "badword2", "badword3"]
        for word in bad_words:
            if word in text:
                raise ValueError("Text contains inappropriate language")
        print(f"Text: {self.text} approved")


class Comment:
    def __init__(self, text, date, likes, author, receiver):
        self.text = text
        self.date = date
        self.likes = likes
        self.author = author
        self.receiver = receiver

    def badword(self, text):
        bad_words = ["badword1", "badword2", "badword3"]
        for word in bad_words:
            if word in text:
                raise ValueError("Text contains inappropriate language")
        print(f"Text: {self.text} approved")


class Message:
    def __init__(self, text, link, images, date, stickers):
        self.text = text
        self.link = link
        self.images = images
        self.date = date
        self.stickers = stickers

    def limit(self, text):
        if len(text) > 1000:
            raise ValueError("Text exceeds character limit")
        print(f"Text: {self.text} approved")

    def badword(self, text):
        bad_words = ["badword1", "badword2", "badword3"]
        for word in bad_words:
            if word in text:
                raise ValueError("Text contains inappropriate language")
        print(f"Text: {self.text} approved")


user1 = user("John Doe", "password123", "1234567890",
             25, "john.doe@example.com")
user2 = user("Jane Smith", "password456", "0987654321",
             30, "jane.smith@example.com")

post1 = user1.create_post("Hi everyone!", "I'm an IT engineer")
post1.show()
