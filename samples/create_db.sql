DROP TABLE demo;
CREATE TABLE demo(
    Id      INTEGER PRIMARY KEY AUTOINCREMENT,
    Type    TEXT NOT NULL,
    Color   TEXT NOT NULL,
    Name    TEXT NOT NULL
);

INSERT INTO demo(
    Type, Color, Name
) VALUES (
    'alma', 'red', 'jonatan'
);

INSERT INTO demo(
    Type, Color, Name
) VALUES (
    'pear', 'yellow', 'golden'
);

INSERT INTO demo(
    Type, Color, Name
) VALUES (
    'grape', 'green', 'nova'
);