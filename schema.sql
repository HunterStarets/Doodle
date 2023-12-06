CREATE TABLE IF NOT EXISTS app_user (
    user_id SERIAL PRIMARY KEY,
    email VARCHAR(255) UNIQUE NOT NULL,
    username VARCHAR(255) UNIQUE NOT NULL,
    password VARCHAR(255) NOT NULL,
    first_name VARCHAR(255) NOT NULL,
    last_name VARCHAR(255) NOT NULL,
    profile_picture TEXT NOT NULL,
    summary TEXT NOT NULL
)

CREATE TABLE IF NOT EXISTS post (
    post_id SERIAL PRIMARY KEY,
    title VARCHAR(255) NOT NULL,
    content TEXT NOT NULL,
    timestamp TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
    author_id INT NOT NULL REFERENCES app_user(user_id),
    community_name VARCHAR(255) NOT NULL
)


--NOT IMPLEMENTED IN SQLALCHEMY YET
CREATE TABLE IF NOT EXISTS comment (
    comment_id SERIAL PRIMARY KEY,
    post_id INT NOT NULL REFERENCES post(post_id),
    author_id INT NOT NULL REFERENCES app_user(user_id),
    content TEXT NOT NULL,
    timestamp TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP
);

--A vote is a boolean and related to a post
CREATE TABLE IF NOT EXISTS vote (
    vote_id SERIAL PRIMARY KEY,
    post_id INT post(post_id),
    comment_id INT comment(comment_id),
    user_id INT NOT NULL REFERENCES app_user(user_id),
    is_upvote BOOLEAN NOT NULL,
    timestamp TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP
);


