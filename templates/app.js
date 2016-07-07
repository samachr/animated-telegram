function search(song) {
  var searchsong = song || $('#search_text').val()
  $("#response").html("loading...");
  $("#submit_button").html('<span class="glyphicon glyphicon-time"></span>');
  $("#response").load("/api/input_example?search="+encodeURIComponent(searchsong), function(){
    $("#submit_button").html('<span class="glyphicon glyphicon-search"></span>');
  });
}

$(function(){
  $('#search_text').keydown(function (event) {
      var keypressed = event.keyCode || event.which;
      if (keypressed == 13) {
          search()
      }
  });
});
