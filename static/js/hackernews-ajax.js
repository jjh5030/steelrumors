jQuery(document).ready(function($) 
    {
	$(".vote_form").submit(function(e) 
		{
		    e.preventDefault(); 
		    var btn = $("button", this);
		    var l_id = $(".hidden_id", this).val();

		    var votes_count = $(".link_votes_count", this);

		    btn.attr('disabled', true);
		    $.post("/vote/", $(this).serializeArray(),
			  function(data) {
			      if(data["voteobj"]) {
				  btn.text("-");
				  votes_count.text(+votes_count.text() + 1);
			      }
			      else {
				  btn.text("+");
				  votes_count.text(+votes_count.text() - 1);
			      }
			      
			  });
		    btn.attr('disabled', false);
		});
    });