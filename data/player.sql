
CREATE TABLE player (name TEXT, health REAL, inventory INT, FOREIGN KEY(inventory) REFERENCES inventory(rowid));

INSERT INTO player VALUES ('Player 1', 100, 1);
INSERT INTO player VALUES ('Player 2', 98, 1);
