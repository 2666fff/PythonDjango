var levelvar = document.getElementById("level").value;
var towerlevelvar = document.getElementById("towerlevel").value;
var state = document.getElementById("state").value;
function LevelUp()
{
    var n = noty({
        text: 'Congratulations, you have leveled up to level '+levelvar,
        type: 'warning',
      dismissQueue: false,
        layout: 'center',
        theme: 'defaultTheme'
    })

}
function TowerUp()
{
    var n = noty({
        text: 'Congratulations, you have advanced up the tower and gained some exp!<br>You are now in tower level '+towerlevelvar,
        type: 'warning',
      dismissQueue: false,
        layout: 'center',
        theme: 'defaultTheme'
    })
}
function Mercy()
{
    var n = noty({
        text: 'You have been shown mercy, HP +100',
        type: 'warning',
      dismissQueue: false,
        layout: 'center',
        theme: 'defaultTheme'
    })

}
function Sure()
{
	var n = noty({
		text: 'Are you sure?',
		type: 'confirm',
		dismissQueue: false,
		layout: 'center',
		theme: 'defaultTheme',
buttons: [
    {addClass: 'btn btn-primary', text: 'Ok', onClick: function($noty) {
        $noty.close();
      }
    },
    {addClass: 'btn btn-danger', text: 'Cancel', onClick: function($noty) {
        $noty.close();
      }
    }
  ]

	})


}
function PurchaseFail(){

    var n = noty({
        text: 'Sorry, it appears you have insufficient funds',
        type: 'error',
      dismissQueue: false,
        layout: 'bottom',
        theme: 'defaultTheme'
    })
}
function PurchaseSuccess(){

    var n = noty({
	   text:'You have successfully purchased an item!',
        type: 'warning',
      dismissQueue: false,
        layout: 'bottom',
        theme: 'defaultTheme'
    })
}
function TowerState(){
	if(state == 1){
    var n = noty({
	text:'You found some money on the floor!',
        type: 'warning',
      dismissQueue: false,
        layout: 'bottom',
        theme: 'defaultTheme'
    })
	}

	if(state == 2){
    var n = noty({
	text:'You moved forward.',
        type: 'warning',
      dismissQueue: false,
        layout: 'bottom',
        theme: 'defaultTheme'
})
}

if(state == 3){
    var n = noty({
	text:'You encounter a monster!',
        type: 'warning',
      dismissQueue: false,
        layout: 'bottom',
        theme: 'defaultTheme'
})
}


}
function Add(){

    var n = noty({
	   text:'Task Added!',
        type: 'warning',
      dismissQueue: false,
        layout: 'bottom',
        theme: 'defaultTheme'
    })
}
function Delete(){

    var n = noty({
	   text:'Task Deleted!',
        type: 'error',
      dismissQueue: false,
        layout: 'bottom',
        theme: 'defaultTheme'
    })
}
function Complete(){

    var n = noty({
	   text:'Task Completed!',
        type: 'success',
      dismissQueue: false,
        layout: 'bottom',
        theme: 'defaultTheme'
    })
}
function ErrorDate(){

    var n = noty({
	   text: 'Incorrect date inputted!',
        type: 'error',
      dismissQueue: false,
        layout: 'bottom',
        theme: 'defaultTheme'
    })
}
function GroupNoMember(){


	    var n = noty({
		text:'User does not exist!',
	        type: 'error',
	      dismissQueue: false,
	        layout: 'bottom',
	        theme: 'defaultTheme'
	})
}
function GroupNoName(){
    var n = noty({
		text:'You need to name your group!',
	        type: 'error',
	      dismissQueue: false,
	        layout: 'bottom',
	        theme: 'defaultTheme'
	})
}
function GroupCreate(){
    var n = noty({
		text:'You successfully created a group!',
	        type: 'success',
	      dismissQueue: false,
	        layout: 'bottom',
	        theme: 'defaultTheme'
	})	
}	
function RequestSent(){
    var n = noty({
		text:'Request Sent!',
	        type: 'success',
	      dismissQueue: false,
	        layout: 'bottom',
	        theme: 'defaultTheme'
	})	
}	
function MessageSent(){
    var n = noty({
		text:'Message Sent!',
	        type: 'success',
	      dismissQueue: false,
	        layout: 'bottom',
	        theme: 'defaultTheme'
	})	
}	
function MessageDelete(){
	doIt=confirm('Are you sure you want to delete this message?');
	  if(doIt){
		  alert("Message Deleted!");
	  }
}
function ConfirmationDelete(){
	  doIt=confirm('Are you sure you want to delete this task?');
	  if(doIt){
		  alert("Task Deleted!");
	  }
	}
function ConfirmSend(){
	  doIt=confirm('Are you sure this task is completed?');
	  if(doIt){
		  alert("Request to verify sent to group leader!");
	  }
	}
function Join(){
	  doIt=confirm('Are you sure you want to join?');
	  if(doIt){
		  alert("Request to join sent to group leader!");
	  }
	}
function Kick(){
	  doIt=confirm('Are you sure you want to kick him/her?');
	  if(doIt){
		  alert("User removed!");
	  }
	}