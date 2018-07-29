$('#beqa').click(function(){
   $('form').hide();
   $('#cMessage').css('visibility', 'visible');
   $('#confirmForm').animate({height: "toggle", opacity: "toggle"}, "slow")
});

$('.message a').click(function(){
   $('form').animate({height: "toggle", opacity: "toggle"}, "slow");
});
