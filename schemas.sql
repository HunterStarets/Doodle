CREATE TABLE IF NOT EXISTS app_user (
    user_id SERIAL PRIMARY KEY,
    email VARCHAR(255) UNIQUE NOT NULL,
    username VARCHAR(255) UNIQUE NOT NULL,
    password VARCHAR(255) NOT NULL,
    first_name VARCHAR(255) NOT NULL,
    last_name VARCHAR(255) NOT NULL,
    bio TEXT NOT NULL
);

CREATE TABLE IF NOT EXISTS post (
    post_id SERIAL PRIMARY KEY,
    title VARCHAR(255) NOT NULL,
    content TEXT NOT NULL,
    timestamp TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
    author_id INT NOT NULL REFERENCES app_user(user_id),
    community_name VARCHAR(255) NOT NULL
);

CREATE TABLE IF NOT EXISTS comment (
    comment_id SERIAL PRIMARY KEY,
    content TEXT NOT NULL,
    timestamp TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
    post_id INT NOT NULL REFERENCES post(post_id),
    author_id INT NOT NULL REFERENCES app_user(user_id)
);

--VOTES--
CREATE TABLE IF NOT EXISTS post_vote (
    vote_id SERIAL PRIMARY KEY,
    post_id INT NOT NULL REFERENCES post(post_id),
    voter_id INT NOT NULL REFERENCES app_user(user_id),
    is_upvote BOOLEAN NOT NULL,
    timestamp TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE IF NOT EXISTS comment_vote (
    vote_id SERIAL PRIMARY KEY,
    comment_id INT NOT NULL REFERENCES comment(comment_id),
    voter_id INT NOT NULL REFERENCES app_user(user_id),
    is_upvote BOOLEAN NOT NULL,
    timestamp TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP
);