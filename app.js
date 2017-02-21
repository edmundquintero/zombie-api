const fs = require('fs');
const express = require('express');
const app = express();

const sqlite3 = require('sqlite3').verbose();

const db = new sqlite3.Database('./test.db');

db.get("SELECT name FROM sqlite_master WHERE type='table' AND name='item'", (error, table) => {
    if ( !table ) {
        fs.readFile('./testData.sql', 'utf8', ( err, data ) => {
            db.exec( data, () => {
                db.each('SELECT rowid, * FROM item', (err, row) => {
                    console.log('Loaded: ', row.rowid + ': ' + row.name);
                })
            } );
            // FOREIGN KEY(trackartist) REFERENCES artist(artistid)
        });
    }
});
/**
 * Check for existemce of Player table in db. If not present create it with default values.
 */
db.get("SELECT name FROM sqlite_master WHERE type='table' AND name='inventory'", (error, table) => {
    if ( !table ) {
        fs.readFile('./data/inventory.sql', 'utf8', ( err, data ) => {
            db.exec( data, () => {
                db.each('SELECT rowid, * FROM inventory', (err, row) => {
                    console.log('Loaded: ', row.rowid + ': ' + row.name);
                })
            } );
        });
    }
});
/**
 * Check for existemce of Player table in db. If not present create it with default values.
 */
db.get("SELECT name FROM sqlite_master WHERE type='table' AND name='player'", (error, table) => {
    if ( !table ) {
        fs.readFile('./data/player.sql', 'utf8', ( err, data ) => {
            db.exec( data, () => {
                db.each('SELECT rowid, * FROM player', (err, row) => {
                    console.log('Loaded: ', row.rowid + ': ' + row.name);
                })
            } );
        });
    }
});

    // db.close();
app.get('/', (req, res) => {
    res.send( '<h1>Future home of the Zombie API! </h1>' +
        '<ul>' +
        '<li> <a href="/item">All Items</a> </li>' +
        '<li> <a href="/item/3">Single Test Data with Id: 3</a> </li>' +
        '<li> <a href="/player">All Players</a> </li>' +
        '</ul>' );
});
// Items
app.get('/item', (req, res) => {
    db.all('SELECT rowid, * FROM item', (err, row) => {
        res.send( JSON.stringify( row ) );
    });
});

app.get('/item/:id', (req, res) => {
    db.get('SELECT rowid, * FROM item WHERE rowid=?', req.params.id.toString(), (err, row) => {
        if( err || !row ){
            res.status(404).send( `This item was not found in the DataBase. <br /> ${ err }`);
        } else {
            res.send( JSON.stringify( row ) );
        }
    });
});
// Player
app.get('/player', (req, res) => {
    const players = [];
    const promises = [];
    const playerPromise = new Promise((playerRes, playerRej) => {
        db.each('SELECT rowid, * FROM player', (err, row) => {
            const player = row;
            const temp = 'SELECT rowid, * FROM inventory WHERE rowid = '+ player.inventory;
            promises.push(
                new Promise((invRes, invRej) => {
                    db.each(temp, (err, inven) => {
                        player.inventory = inven;
                        players.push(player);
                    }, () => {
                        invRes("test");
                    });
                })
            ); //end push
        }, () => {
            playerRes();
        });
    });

    playerPromise.then(() => {
        Promise.all(promises).then( (data) => {
            res.send( players );
        });
    });



});

app.get('/player/:id', (req, res) => {
    db.get('SELECT player.rowid, * FROM player WHERE player.rowid=?', req.params.id.toString(), (err, row) => {
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
