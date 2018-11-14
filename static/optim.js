// function that builds a grid in the "container"
var ox_coord = 0, oy_coord = 0, oprev_x = -1, oprev_y = -1;
// #9c412e dark red
function getClass(a) {
	switch (a) {
		case "D":
			return "fa-arrow-down";
		case "U":
			return "fa-arrow-up";
		case "L":
			return "fa-arrow-left";
		case "R":
			return "fa-arrow-right";
		default:

	}
}
function mark(i,j,m) {
	var grid = $(".gridO");
	// if (grid[i * gridsz + j].flg) {
	// 	m = " | " + m ;
	// }

	grid.children()[i * gridsz + j].classList.add(getClass(m)) ;

	// grid[i * gridsz + j].flg = 1;
}
function moveUpO() {
	if(oy_coord == 0){
		alert("invalid move by agent ") ;
		console.log("invalid move by agent ");
	}
	else{
		oy_coord --;
        color(oy_coord ,ox_coord ,gridsz, "#e6c889", ".gridO", "U");
		mark(oy_coord + 1, ox_coord , "U");
		// color(oprev_y ,oprev_x ,gridsz, "light#e6c889", ".gridO");
        // oprev_x = ox_coord, oprev_y = oy_coord;
		// console.log("coord : ", ox_coord, oy_coord);

	}
}

function moveDownO() {
	if(oy_coord == gridsz - 1){
		alert("invalid move by agent ") ;
		console.log("invalid move by agent ");
	}
	else{
		oy_coord ++;
        color(oy_coord ,ox_coord ,gridsz, "#e6c889", ".gridO", "D");
		mark(oy_coord - 1, ox_coord , "D");
        // color(oprev_y ,oprev_x ,gridsz, "light#e6c889", ".gridO");
        // oprev_x = ox_coord, oprev_y = oy_coord;	}
	}
		// console.log("coord : ", ox_coord, oy_coord);
}

function moveRightO() {
	if(ox_coord == gridsz - 1){
		alert("invalid move by agent ") ;
		console.log("invalid move by agent ");
	}
	else{
		ox_coord ++;
        color(oy_coord ,ox_coord ,gridsz, "#e6c889", ".gridO", "R");
		mark(oy_coord, ox_coord - 1, "R");
        // color(oprev_y ,oprev_x ,gridsz, "light#e6c889", ".gridO");
        // oprev_x = ox_coord, oprev_y = oy_coord;	}
	}
		// console.log("coord : ", ox_coord, oy_coord);
}

function moveLeftO() {
	if(ox_coord == 0){
		alert("invalid move by agent ") ;
		console.log("invalid move by agent ");
	}
	else{
		ox_coord --;
        color(oy_coord ,ox_coord ,gridsz, "#e6c889", ".gridO", "L");
		mark(oy_coord, ox_coord + 1, "L");
        // color(oprev_y ,oprev_x ,gridsz, "light#e6c889", ".gridO");
        // oprev_x = ox_coord, oprev_y = oy_coord;	}
	}
		// console.log("coord : ", ox_coord, oy_coord);
}



function makeActions(actions){
	console.log(y_coord, x_coord);
	for(x = 0; x < actions.length; x++){
		switch (actions[x]) {
			case 0:
				// console.log("up");
				moveUpO();
				break;
			case 1:
			// console.log("down");
				moveDownO();
				break;
			case 2:
			// console.log("right");
				moveRightO();
				break;
			case 3:
			// console.log("left");
				moveLeftO();
				break;


		}
	}
	var grid = $(".gridO") ;
	console.log("check : ", y_end * gridsz + x_end);
	grid.children()[y_end * gridsz + x_end].classList.add("fa-flag-checkered") ;

	// $(".gridO")[gridsz*gridsz - 1].classList.add("fa-arrow-up");
}


function createGridO(x) {
    for (var rows = 0; rows < x; rows++) {
        for (var columns = 0; columns < x; columns++) {
            $("#containerO").append("<div class='gridO'><p class = 'fa'></p></div>");
        };
    };
    $(".gridO").width(720/x);
    $(".gridO").height(720/x);
	var mgt = (360/x - 20) + 'px';
	$('.gridO').children().css({'margin-top':mgt});
	// console.log("aaa : ",document.getElementsByClassName('gridO').length);

};
