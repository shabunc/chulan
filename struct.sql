
CREATE TABLE projects(
    name VARCHAR(200) NOT NULL,
    id SERIAL NOT NULL,
    PRIMARY KEY (id, name),
    UNIQUE(name)
)

