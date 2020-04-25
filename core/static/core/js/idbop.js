

var dbPromise = idb.open('feeds-db', 1, function (upgradeDb) {
    upgradeDb.createObjectStore('feeds', { keyPath: 'pk' });
});


fetch('http://127.0.0.1:8000/getdata').then(function (response) {
    return response.json();
}).then(function (jsondata) {
    dbPromise.then(function (db) {
        var tx = db.transaction('feeds', 'readwrite');
        var feedsStore = tx.objectStore('feeds');
        for (var key in jsondata) {
            if (jsondata.hasOwnProperty(key)) {
                feedsStore.put(jsondata[key]);
            }
        }
    });
});



// $( "#myInput" ).keyup(function() {
//     var inp = $(this).val()
//     if (inp.length < 1) {
//         $('tr').show();
//     }

//   });


