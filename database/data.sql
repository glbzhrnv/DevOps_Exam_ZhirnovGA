-- Таблица книг
INSERT INTO books (id, title, author, publisher) VALUES
    (1, 'Война и мир', 'Толстой Л.Н.', 'ЭКСМО'),
    (2, 'Гибкое сознание', 'Кэрол Дуэк', 'МИФ'),
    (3, 'Благословение небожителей', 'Мосян Тунсю', 'Комильфо'),
    (4, 'Человек-невидимка', 'Герберт Уэллс', 'ЛЕНИЗДАТ');

-- Таблица пользователей
INSERT INTO users (id, username, password) VALUES 
    (1, 'xxxnagibator', 'qwerty'),
    (2, 'osoznanie', 'resurs'),
    (3, 'normis', 'ponpon');

-- Таблица взятых книг
INSERT INTO borrowed_books (user_id, book_id, borrow_date, return_date) VALUES
    (1, 1, '2025-01-01', '2025-01-15'),
    (2, 2, '2025-01-02', '2025-01-16'),
    (3, 4, '2025-01-03', '2025-01-17');
