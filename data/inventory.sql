CREATE TABLE inventory (name TEXT, slot0 INT, FOREIGN KEY(slot0) REFERENCES item(rowid));

INSERT INTO inventory VALUES ('Back Pack', 2);