<script>
        $(document).ready(function(){
            $('#searchForm').on('submit', function(event){
                event.preventDefault();

                $.ajax({
                    type: 'POST',
                    url: "{% url 'home' %}",
                    data: $(this).serialize(),
                    success: function(response){
                        $('#message').text('');
                        $('#results').html('');
                        if (response.message){
                            $("#message").text(response.message);

                        }else {
                            let table = '<table><caption><span>Licence</span> en Science de la vie et de terre </caption><thead><tr><td>ID</td><td>UE</td><td>Semestre</td><td>Crédit</td><td>Télécharger</td></tr></thead><tbody>';
                            $.each(response.results, function(index, result){
                                table += '<tr><td class = "td-1"><span>1</span></td><td class="td2">' + result.ue + '</td><td class="td-3">Semestre ' + result.semestre + '</td><td class="td-4>" ' + result.credit + '</td><td class="td-5"><href="#">Télécharger</a></td></tr>';
                            });
                            table += '</tbody></table>';
                            $('#results').html(table);
                        }
                    },
                    error: function(response){
                        console.log("error",response)
                    }
                })
            })
        })
   </script>