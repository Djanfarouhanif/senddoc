const button = document.querySelector('#searchButton');
const loader = document.querySelector(".loader");
let isRunning = false;







function Syncho(){
    $(document).ready(function(){
        $('#searchForm').on('submit', function(event){
            event.preventDefault();
    
            $.ajax({
                type: 'POST',
                url: "http://127.0.0.1:8000/",
                data: $(this).serialize(),
                success: function(response){
                    $('#message').text('');
                    $('#results').html('');
                    if (response.message){
                        $("#message").text(response.message);
    
                    }else {
                        let table = '<table><caption><span>Licence </span> en Science de la vie et de la terre</caption><thead><tr><td>ID</td><td>UE</td><td>Semestre</td><td>Crédit</td><td>Télécharger</td></tr></thead><tbody>';
                        $.each(response.results, function(index, result){
                            table += '<tr><td class="td-1"><span>1</span></td><td class="td-2">' + result.ue + '</td><td class="td-3">Semestre ' + result.semestre + '</td><td class="td-4">' + result.credit + '</td><td class="td-5"><a href="#">Télécharger</a></td></tr>';
                        });
                        table += '</tbody></table>';
                        $('#results').html(table);
                    }
                },
                error: function(response){
                    console.log("error",response)
                }
            });
        });
    });
}


button.addEventListener('click', (event)=>{
    event.preventDefault();

    if(!isRunning){
        isRunning = true;
        loader.style.display = 'block';

        setTimeout(()=>{
            loader.style.display = 'none';
            isRunning = false;
            Syncho()
        }, 3000
               
        )
    }
   
})


