const consoel = console;

const express = require('express');
const app = express();
var fs = require('fs');

const sqlite3 = require('sqlite3').verbose();
const db = new sqlite3.Database('./test.db');

db.get("SELECT name FROM sqlite_master WHERE type='table' AND name='lorem'", (error, table) => {
    console.log(table);
    if ( !table ) {

        db.serialize( () => {
          db.run('CREATE TABLE lorem (info TEXT)');
          const stmt = db.prepare('INSERT INTO lorem VALUES (?)');

          for (var i = 0; i < 100; i++) {
            stmt.run('Ipsum ' + i);
          }

          stmt.finalize();

          db.each('SELECT rowid AS id, info FROM lorem', (err, row) => {
            console.log('Loaded: ', row.id + ': ' + row.info);
          })
        })
    }
});


    // db.close();


app.get('/', (req, res) => {
    res.send( '<h1>Future home of the Zombie API! </h1>' +
        '<ul>' +
        '<li> <a href="/test">All Test Data</a> </li>' +
        '<li> <a href="/test/3">Single Test Data with Id: 3</a> </li>' +
        '</ul>' );
});

app.get('/test', (req, res) => {
    const returnData = [];
    db.each('SELECT rowid AS id, info FROM lorem', (err, row) => {
        returnData.push({
            id: row.id,
            info: row.info
        });
    }, () => {
        res.send( JSON.stringify( returnData ) );
    });
});

app.get('/test/:id', (req, res) => {
    db.get('SELECT rowid AS id, info FROM lorem WHERE rowid=?', req.params.id.toString(), (err, row) => {
        if( err || !row ){
            res.send( err || 404);
        } else {
            res.send({
                id: row.id,
                info: row.info
            });
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