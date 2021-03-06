

// A $( document ).ready() block.
$( document ).ready(function() {

    var dbPromise = idb.open('feeds-db', 1, function (upgradeDb) {
        upgradeDb.createObjectStore('feeds', { keyPath: 'pk' });
    });
    
    
    fetch('/getdata').then(function (response) {
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
    
    $('tr').each(function() {
        $(this).show();

        
    });

    $('#decom').click(function(e){
        e.preventDefault();
        var pass = $('#pass_me').val();
        var inp = $('#id_where').val();
        var inp1 = $('#id_what').val();
        var decrypted = CryptoJS.AES.decrypt(inp, pass);
        var decrypted1 = CryptoJS.AES.decrypt(inp1, pass);
        $('#id_where').val(decrypted.toString(CryptoJS.enc.Utf8));
        $('#id_what').val(decrypted1.toString(CryptoJS.enc.Utf8));

    });

    
    $('#password').keyup(function() {
        var pass = $('#password').val()
        if (pass.length > 4) {
            $('#subbutton').attr("disabled", false);
        } else {
            $('#subbutton').attr("disabled", true);
        }

        });

        $('#decrytAll').click(function(){
            $('.passed').each(function() {
                var inp = $(this).html()
                var pass = $('#repass').val()
                var decrypted = CryptoJS.AES.decrypt(inp, pass);
                console.log(decrypted.toString(CryptoJS.enc.Utf8));
                
                $(this).next().html(decrypted.toString(CryptoJS.enc.Utf8))
    
                
            });
    

        });


        $('#myInput').keyup(function(){
            
              var input, filter, table, tr, td, i, txtValue;
              input = document.getElementById("myInput");
              filter = input.value.toUpperCase();
              if (filter.length > 2) {
                  table = document.getElementById("myTable");
                  tr = table.getElementsByTagName("tr");
                  for (i = 0; i < tr.length; i++) {
                  td = tr[i].getElementsByTagName("td")[0];
                  if (td) {
                      txtValue = td.textContent || td.innerText;
                      if (txtValue.toUpperCase().indexOf(filter) > -1) {
                      tr[i].style.display = "";
                      } else {
                      tr[i].style.display = "none";
                      }
                  }       
                  }
              } else{

                $('tr').show();
              }
      
        });

        
    // $('#crypt').change(function() {
    //     if ($('#crypt').is(':checked')) {
    //         var inp = $('#id_where').val()
    //         var pass = $('#password').val()
    //         var encrypted = CryptoJS.AES.encrypt(inp, pass);
    //         var decrypted = CryptoJS.AES.decrypt(encrypted, pass);
    //         $('#id_where').val(encrypted)
            
    //     } else {
    //         var inp = $('#id_where').val()
    //         var pass = $('#password').val()
    //         var decrypted = CryptoJS.AES.decrypt(inp, pass);
    //         $('#id_where').val(decrypted.toString(CryptoJS.enc.Utf8))
    //     }
    //   });



    //   $( "#repass" ).keyup(function() {
    //     $('.passed').each(function() {
    //         var inp = $(this).next().html()
    //         var pass = $('#repass').val()
    //         var decrypted = CryptoJS.AES.decrypt(inp, pass);
    //         $(this).html(decrypted.toString(CryptoJS.enc.Utf8))

            
    //     });
    //   });

      $("#subbutton").click(function(e){
        e.preventDefault();

        var inp = $('#id_where').val();
        var pass = $('#password').val();
        var inp2 = $('#id_what').val();
        var encrypted = CryptoJS.AES.encrypt(inp, pass);
        var encrypted2 = CryptoJS.AES.encrypt(inp2, pass);
        $('#id_where').val(encrypted);
        $('#id_what').val(encrypted2);
        $('#myform').submit();

     });



});

