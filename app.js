const express = require('express');
const app = express();

const sqlite3 = require('sqlite3').verbose();
const db = new sqlite3.Database('./test.db');

db.get("SELECT name FROM sqlite_master WHERE type='table' AND name='items'", (error, table) => {

    if ( !table ) {

        db.serialize( () => {
            db.run('CREATE TABLE items (name TEXT, desc TEXT, weight INT, dmg INT, healAmt INT)');
            const stmt = db.prepare('INSERT INTO items VALUES (?, ?, ?, ?, ?)');

            stmt.run('Apple', 'Red', 0.5, 1, 10);
            stmt.run('Watermellon', 'Green', 2.5, 1, 20);
            stmt.run('Ninja Star', 'Silver', 0.2, 5, 0);
            stmt.run('Cricket Bat', 'Brown', 1.5, 3, 0);

            stmt.finalize();

            db.each('SELECT rowid AS id, name FROM items', (err, row) => {
                console.log('Loaded: ', row.id + ': ' + row.name);
            })
        })
    }
});


    // db.close();
app.get('/', (req, res) => {
    res.send( '<h1>Future home of the Zombie API! </h1>' +
        '<ul>' +
        '<li> <a href="/items">All Test Data</a> </li>' +
        '<li> <a href="/items/3">Single Test Data with Id: 3</a> </li>' +
        '</ul>' );
});

app.get('/items', (req, res) => {
    db.all('SELECT rowid AS id, name, desc, weight, dmg, healAmt FROM items', (err, row) => {
        res.send( JSON.stringify( row ) );
    });
});

app.get('/items/:id', (req, res) => {
    db.get('SELECT rowid AS id, name FROM items WHERE rowid=?', req.params.id.toString(), (err, row) => {
        if( err || !row ){
            res.status(404).send( `This item was not found in the DataBase. <br /> ${ err }`);
        } else {
            res.send( JSON.stringify( row ) );
        }
    });
});

/**
 * Start the Server
 * @param  {Number} 3000 Port to listen on
 * @param  {Function} Callback
 */
app.listen(3000, () => {
  console.log('Zombie API listening on port 3000...');
})
