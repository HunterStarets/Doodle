CREATE TABLE IF NOT EXISTS app_user (
user_id SERIAL,
email VARCHAR(255) UNIQUE NOT NULL,
username VARCHAR(255) UNIQUE NOT NULL,
password VARCHAR(255) NOT NULL,
first_name VARCHAR(255) NOT NULL,
last_name VARCHAR(255) NOT NULL,
PRIMARY KEY (user_id)
);

CREATE TABLE IF NOT EXISTS post (
    post_id SERIAL,
    title VARCHAR(255) NOT NULL,
    content TEXT NOT NULL,
    community_name VARCHAR(255),
    timestamp TIMESTAMP NOT NULL,
    points INT DEFAULT 0,
    author_id INT,
    PRIMARY KEY (post_id),
    FOREIGN KEY (author_id) REFERENCES app_user(user_id)
);

CREATE TABLE IF NOT EXISTS comment (
    comment_id SERIAL,
    timestamp TIMESTAMP NOT NULL,
    content TEXT NOT NULL,
    points INT DEFAULT 0,
    author_id INT,
    post_id INT,
    PRIMARY KEY (comment_id),
    FOREIGN KEY (author_id) REFERENCES app_user(user_id)
    FOREIGN KEY (post_id) REFERENCES post(post_id)
);

