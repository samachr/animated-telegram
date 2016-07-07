function search(song) {
  var searchsong = song || $('#search_text').val()
  $("#guitartabcontent").html("loading...");
  $("#submit_button").html('<span class="glyphicon glyphicon-time"></span>');
  $("#guitartabcontent").load("/api/input_example?search="+encodeURIComponent(searchsong), function(){
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
