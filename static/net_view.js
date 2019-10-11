jQuery.ajaxSettings.traditional = true;
$(document).ready(function () {
    $("#scan_button").addClass("loading");
    populate_hosts();
    $("#scan_button").click(function(){
        $("#scan_button").addClass("loading");
        $('#net_view_body').empty()
        populate_hosts();
    });
});

function populate_hosts(){
    $.getJSON("/hosts",{},function(hosts){
        $.each(hosts, function(index){
            $('#net_view_table').append('<tr><td>'+index+'</td><<td>'+hosts[index]+'</td></tr>');
        })
        $("#scan_button").removeClass("loading");
    });
}
